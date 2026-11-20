// Web Worker that owns the Pyodide interpreter (CPython compiled to WebAssembly).
// Running Python off the main thread keeps the page responsive; an endless loop
// can be stopped by terminating this worker from runner.ts.

import { OUTPUT_LIMIT, type RunnerRequest, type RunnerResponse } from "./protocol";

type StreamHandler = { write: (buffer: Uint8Array) => number; isatty?: boolean };

type PyProxyFunction = ((...args: unknown[]) => unknown) & { destroy?: () => void };

type PyodideInterface = {
  version: string;
  runPython: (code: string) => unknown;
  globals: { get: (name: string) => unknown };
  setStdout: (options: StreamHandler) => void;
  setStderr: (options: StreamHandler) => void;
};

type PyodideModule = {
  loadPyodide: (options: { indexURL: string }) => Promise<PyodideInterface>;
};

// The project compiles with the DOM lib; describe only the worker scope API used here.
type WorkerScope = {
  postMessage: (message: RunnerResponse) => void;
  addEventListener: (type: "message", listener: (event: MessageEvent<RunnerRequest>) => void) => void;
};

const scope = self as unknown as WorkerScope;

// Runs one student program in a fresh `__main__` namespace and prints the
// traceback without the frame of this helper, so the output looks like `python main.py`.
// Before every run the working directory of Pyodide's in-memory file system is
// recreated from the exercise's test files, so programs that move or create files
// always start from the same state and never touch the student's real disk.
const RUN_HELPER = `
import json
import linecache
import os
import shutil
import sys
import traceback

FILENAME = "main.py"
WORKSPACE = "/home/pyodide/workspace"


def _prepare_workspace(files_json):
    os.chdir("/")
    shutil.rmtree(WORKSPACE, ignore_errors=True)
    os.makedirs(WORKSPACE)
    for relative_path, content in json.loads(files_json).items():
        path = os.path.join(WORKSPACE, relative_path)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as file:
            file.write(content)
    os.chdir(WORKSPACE)
    sys.argv = [FILENAME]


def _course_run(source, input_message, files_json):
    def _input(prompt=""):
        raise RuntimeError(input_message)

    _prepare_workspace(files_json)
    # Lets tracebacks show the offending source lines, as with a real file.
    linecache.cache[FILENAME] = (len(source), None, source.splitlines(True), FILENAME)
    namespace = {"__name__": "__main__", "input": _input}
    try:
        code = compile(source, FILENAME, "exec")
        exec(code, namespace)
    except SystemExit as error:
        # Same as the python command: a text code is printed, a non-zero number only fails the run.
        sys.stdout.flush()
        if error.code is None or error.code == 0:
            return True
        if not isinstance(error.code, int):
            print(error.code, file=sys.stderr)
        return False
    except BaseException as error:
        sys.stdout.flush()
        report = traceback.TracebackException.from_exception(error)
        report.stack = traceback.StackSummary.from_list(
            [frame for frame in report.stack if frame.filename == FILENAME]
        )
        print("".join(report.format()), end="", file=sys.stderr)
        return False
    finally:
        sys.stdout.flush()
        sys.stderr.flush()
    return True
`;

let pyodide: PyodideInterface | undefined;
let runProgram: PyProxyFunction | undefined;
let currentRunId = 0;
let forwardedChars = 0;
let truncated = false;

function post(message: RunnerResponse) {
  scope.postMessage(message);
}

function streamHandler(stream: "stdout" | "stderr"): StreamHandler {
  const decoder = new TextDecoder();

  return {
    isatty: false,
    write(buffer) {
      if (truncated) return buffer.length;

      let text = decoder.decode(buffer, { stream: true });
      const remaining = OUTPUT_LIMIT - forwardedChars;
      if (text.length > remaining) {
        text = text.slice(0, remaining);
        truncated = true;
      }

      forwardedChars += text.length;
      if (text) post({ type: "output", id: currentRunId, stream, text });
      if (truncated) post({ type: "truncated", id: currentRunId });
      return buffer.length;
    }
  };
}

async function init(indexURL: string) {
  try {
    const module = (await import(/* @vite-ignore */ `${indexURL}pyodide.mjs`)) as PyodideModule;
    pyodide = await module.loadPyodide({ indexURL });
    pyodide.setStdout(streamHandler("stdout"));
    pyodide.setStderr(streamHandler("stderr"));
    pyodide.runPython(RUN_HELPER);
    runProgram = pyodide.globals.get("_course_run") as PyProxyFunction;

    const pythonVersion = String(pyodide.runPython("import sys; sys.version.split()[0]"));
    post({ type: "ready", pythonVersion });
  } catch (error) {
    post({ type: "init-error", message: error instanceof Error ? error.message : String(error) });
  }
}

function run(id: number, code: string, inputMessage: string, files: Record<string, string>) {
  if (!runProgram) {
    post({ type: "done", id, ok: false });
    return;
  }

  currentRunId = id;
  forwardedChars = 0;
  truncated = false;

  let ok = false;
  try {
    ok = runProgram(code, inputMessage, JSON.stringify(files)) === true;
  } catch (error) {
    // Errors are normally printed by the Python helper; this is a last-resort fallback.
    post({ type: "output", id, stream: "stderr", text: `${error instanceof Error ? error.message : String(error)}\n` });
  }

  post({ type: "done", id, ok });
}

scope.addEventListener("message", (event) => {
  const message = event.data;
  if (message.type === "init") void init(message.indexURL);
  if (message.type === "run") run(message.id, message.code, message.inputMessage, message.files);
});
