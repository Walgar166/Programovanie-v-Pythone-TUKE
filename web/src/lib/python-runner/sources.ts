// Build-time access to the code shown in in-browser editors.
// Source files live next to the other exercise starters:
//   exercises/exercise-XX/playground/task_YY.{sk,en}.py      starter code (required)
//   exercises/exercise-XX/playground/solution_YY.{sk,en}.py  sample solution (optional)
// Keeping them as real .py files means `npm run validate` checks their syntax.

import type { LocalizedString } from "@shared/i18n";

const sourceFiles = import.meta.glob<string>("../../../../exercises/*/playground/*.py", {
  query: "?raw",
  import: "default",
  eager: true
});

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
