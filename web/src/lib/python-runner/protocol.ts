// Messages exchanged between the page (runner.ts) and the Pyodide Web Worker (worker.ts).

export type RunnerRequest =
  | { type: "init"; indexURL: string }
  | { type: "run"; id: number; code: string; inputMessage: string };

export type RunnerResponse =
  | { type: "ready"; pythonVersion: string }
  | { type: "init-error"; message: string }
  | { type: "output"; id: number; stream: "stdout" | "stderr"; text: string }
  | { type: "truncated"; id: number }
  | { type: "done"; id: number; ok: boolean };

/** Maximum number of output characters forwarded from one run. Protects the page from runaway print loops. */
export const OUTPUT_LIMIT = 200_000;
