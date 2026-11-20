// Page-side client of the Pyodide worker. One interpreter is shared by all
// editors on a page and is downloaded lazily, only when a student first needs it.

import type { RunnerRequest, RunnerResponse } from "./protocol";

/** Pinned Pyodide release (Python 3.14). Change only together with a manual check of the exercises. */
export const PYODIDE_VERSION = "314.0.7";
const PYODIDE_INDEX_URL = `https://cdn.jsdelivr.net/pyodide/v${PYODIDE_VERSION}/full/`;

export type RunnerState = "idle" | "loading" | "ready" | "running" | "error";

export type RunHandlers = {
  onOutput: (stream: "stdout" | "stderr", text: string) => void;
  onTruncated: () => void;
};

export type RunResult =
  | { status: "ok" | "error" }
  | { status: "stopped" }
  | { status: "unavailable"; message: string };

type ActiveRun = {
  id: number;
  owner: string;
  handlers: RunHandlers;
  resolve: (result: RunResult) => void;
};

class PythonRunner extends EventTarget {
  private worker: Worker | undefined;
  private readyPromise: Promise<void> | undefined;
  private activeRun: ActiveRun | undefined;
  private nextRunId = 1;
  private currentState: RunnerState = "idle";

  get state() {
    return this.currentState;
  }

  /** Identifier of the editor whose program is currently running. */
  get activeOwner() {
    return this.activeRun?.owner;
  }

  /** Starts downloading the interpreter in the background without running anything. */
  preload() {
    void this.ensureReady().catch(() => undefined);
  }

  async run(
    owner: string,
    code: string,
    inputMessage: string,
    files: Record<string, string>,
    handlers: RunHandlers
  ): Promise<RunResult> {
    if (this.activeRun) return { status: "unavailable", message: "busy" };

    try {
      await this.ensureReady();
    } catch (error) {
      return { status: "unavailable", message: error instanceof Error ? error.message : String(error) };
    }

    if (this.activeRun || !this.worker) return { status: "unavailable", message: "busy" };

    return new Promise<RunResult>((resolve) => {
      const id = this.nextRunId++;
      this.activeRun = { id, owner, handlers, resolve };
      this.setState("running");
      this.send({ type: "run", id, code, inputMessage, files });
    });
  }

  /** Terminates the worker. This is the only reliable way to interrupt an endless loop without cross-origin isolation. */
  stop() {
    const run = this.activeRun;
    this.worker?.terminate();
    this.worker = undefined;
    this.readyPromise = undefined;
    this.activeRun = undefined;
    this.setState("idle");
    run?.resolve({ status: "stopped" });
  }

  private ensureReady() {
    if (this.readyPromise) return this.readyPromise;

    this.setState("loading");
    const worker = new Worker(new URL("./worker.ts", import.meta.url), { type: "module" });
    this.worker = worker;

    this.readyPromise = new Promise<void>((resolve, reject) => {
      worker.addEventListener("message", (event: MessageEvent<RunnerResponse>) => {
        const message = event.data;

        if (message.type === "ready") {
          this.setState("ready");
          resolve();
          return;
        }

        if (message.type === "init-error") {
          this.failInit(worker, message.message, reject);
          return;
        }

        this.handleRunMessage(message);
      });

      worker.addEventListener("error", (event) => {
        this.failInit(worker, event.message || "Worker error", reject);
      });
    });

    this.send({ type: "init", indexURL: PYODIDE_INDEX_URL });
    return this.readyPromise;
  }

  private failInit(worker: Worker, message: string, reject: (error: Error) => void) {
    worker.terminate();
    if (this.worker === worker) {
      this.worker = undefined;
      this.readyPromise = undefined;
    }
    this.setState("error");
    reject(new Error(message));
  }

  private handleRunMessage(message: RunnerResponse) {
    const run = this.activeRun;
    if (!run || !("id" in message) || message.id !== run.id) return;

    if (message.type === "output") run.handlers.onOutput(message.stream, message.text);
    if (message.type === "truncated") run.handlers.onTruncated();
    if (message.type === "done") {
      this.activeRun = undefined;
      this.setState("ready");
      run.resolve({ status: message.ok ? "ok" : "error" });
    }
  }

  private send(message: RunnerRequest) {
    this.worker?.postMessage(message);
  }

  private setState(state: RunnerState) {
    this.currentState = state;
    this.dispatchEvent(new CustomEvent<RunnerState>("statechange", { detail: state }));
  }
}

let sharedRunner: PythonRunner | undefined;

/** Returns the single runner instance shared by all editors on the page. */
export function getPythonRunner() {
  sharedRunner ??= new PythonRunner();
  return sharedRunner;
}

export type { PythonRunner };
