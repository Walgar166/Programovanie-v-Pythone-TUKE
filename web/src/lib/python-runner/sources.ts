// Build-time access to the code shown in in-browser editors.
// Source files live next to the other exercise starters:
//   exercises/exercise-XX/playground/task_YY.{sk,en}.py      starter code (required)
//   exercises/exercise-XX/playground/solution_YY.{sk,en}.py  sample solution (optional)
//   exercises/exercise-XX/playground/workspace.json          test files for the editor (optional)
// Keeping them as real .py files means `npm run validate` checks and runs them.
//
// workspace.json lists paths relative to exercises/exercise-XX/ that are copied into
// the editor's working directory before every run, e.g. { "copy": ["subory"] }.
// The same test data is used by the starter ZIP, the editor and the validation.

import type { LocalizedString } from "@shared/i18n";

type WorkspaceConfig = { copy?: string[] };

const sourceFiles = import.meta.glob<string>("../../../../exercises/*/playground/*.py", {
  query: "?raw",
  import: "default",
  eager: true
});

const workspaceConfigs = import.meta.glob<WorkspaceConfig>("../../../../exercises/*/playground/workspace.json", {
  import: "default",
  eager: true
});

// Test data must be text; dot files such as .gitkeep keep empty directories.
const exerciseFiles = import.meta.glob<string>(["../../../../exercises/*/**/*", "../../../../exercises/*/**/.*"], {
  query: "?raw",
  import: "default",
  eager: true
});

/** Returns the files copied into the editor's working directory: relative path -> content. */
export function getPlaygroundWorkspace(exercise: string): Record<string, string> {
  const exerciseRoot = `/exercises/exercise-${exercise}/`;
  const config = Object.entries(workspaceConfigs).find(([path]) => path.endsWith(`${exerciseRoot}playground/workspace.json`))?.[1];
  const files: Record<string, string> = {};

  for (const entry of config?.copy ?? []) {
    const prefix = `${exerciseRoot}${entry.replace(/\/$/, "")}`;
    const matches = Object.entries(exerciseFiles).filter(([path]) => path.endsWith(prefix) || path.includes(`${prefix}/`));
    if (matches.length === 0) throw new Error(`workspace.json cvičenia ${exercise} odkazuje na neexistujúcu cestu: ${entry}`);

    for (const [path, content] of matches) {
      const relativePath = path.slice(path.indexOf(exerciseRoot) + exerciseRoot.length);
      files[relativePath] = content.replace(/\r\n/g, "\n");
    }
  }

  return files;
}

function readFile(exercise: string, fileName: string) {
  const suffix = `/exercises/exercise-${exercise}/playground/${fileName}`;
  const entry = Object.entries(sourceFiles).find(([path]) => path.endsWith(suffix));
  return entry?.[1].replace(/\r\n/g, "\n").replace(/\n+$/, "\n");
}

function readStarter(exercise: string, task: string, language: "sk" | "en") {
  const code = readFile(exercise, `task_${task}.${language}.py`);
  if (code === undefined) {
    throw new Error(`Chýba starter kód editora: exercises/exercise-${exercise}/playground/task_${task}.${language}.py`);
  }
  return code;
}

/** Returns the SK and EN starter code for one exercise task. Both language versions are required. */
export function getPlaygroundStarter(exercise: string, task: string): LocalizedString {
  return {
    sk: readStarter(exercise, task, "sk"),
    en: readStarter(exercise, task, "en")
  };
}

/** Returns the SK and EN sample solution, or undefined when the task has none. */
export function getPlaygroundSolution(exercise: string, task: string): LocalizedString | undefined {
  const sk = readFile(exercise, `solution_${task}.sk.py`);
  const en = readFile(exercise, `solution_${task}.en.py`);
  if (sk === undefined && en === undefined) return undefined;
  if (sk === undefined || en === undefined) {
    throw new Error(`Riešenie úlohy ${exercise}/${task} musí mať SK aj EN verziu (solution_${task}.sk.py a .en.py).`);
  }
  return { sk, en };
}
