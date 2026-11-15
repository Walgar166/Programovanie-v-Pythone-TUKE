// Small Python syntax highlighter for the in-browser editor and its sample solutions.
// It runs both at build time (solution blocks) and in the browser (live editor),
// so it has no dependencies and works on the whole text to support multi-line strings.

export type TokenKind =
  | "keyword"
  | "control"
  | "constant"
  | "builtin"
  | "type"
  | "function"
  | "decorator"
  | "string"
  | "number"
  | "comment"
  | "self"
  | "plain";

export type Token = { kind: TokenKind; text: string };

// Declarations and operators (blue) vs. control flow (purple), as in common editor themes.
const KEYWORDS = new Set(["def", "class", "lambda", "and", "or", "not", "in", "is", "del", "global", "nonlocal", "async", "await"]);
const CONTROL = new Set([
  "if", "elif", "else", "for", "while", "break", "continue", "return", "yield", "try", "except", "finally",
  "raise", "with", "as", "import", "from", "pass", "assert", "match", "case"
]);
const CONSTANTS = new Set(["True", "False", "None", "NotImplemented", "Ellipsis", "__name__"]);
const BUILTINS = new Set([
  "print", "len", "range", "sorted", "reversed", "sum", "min", "max", "abs", "round", "enumerate", "zip", "map",
  "filter", "any", "all", "isinstance", "issubclass", "getattr", "setattr", "hasattr", "open", "input", "iter",
  "next", "repr", "format", "id", "hash", "vars", "dir", "super", "callable", "divmod", "pow", "chr", "ord"
]);
const TYPES = new Set([
  "int", "float", "str", "bool", "list", "dict", "set", "tuple", "frozenset", "bytes", "object", "type",
  "Exception", "BaseException", "ValueError", "TypeError", "KeyError", "IndexError", "RuntimeError",
  "ZeroDivisionError", "AttributeError", "NameError", "SystemExit", "StopIteration", "FileNotFoundError"
]);
const STRING_PREFIX = /^(?:[rRbBuUfF]|[rR][bBfF]|[bBfF][rR])$/;

const NUMBER = /0[xX][0-9a-fA-F_]+|0[oO][0-7_]+|0[bB][01_]+|(?:\d[\d_]*\.?[\d_]*|\.\d[\d_]*)(?:[eE][+-]?\d[\d_]*)?[jJ]?/y;
const IDENTIFIER = /[\p{L}_][\p{L}\p{N}_]*/uy;

function readString(code: string, start: number) {
  const quote = code[start];
  const triple = code.startsWith(quote.repeat(3), start);
  const closing = triple ? quote.repeat(3) : quote;
  let index = start + closing.length;

  while (index < code.length) {
    const char = code[index];
    if (char === "\\") {
      index += 2;
      continue;
    }
    if (!triple && char === "\n") return index;
    if (code.startsWith(closing, index)) return index + closing.length;
    index += 1;
  }

  return code.length;
}

function nextNonSpace(code: string, start: number) {
  let index = start;
  while (code[index] === " " || code[index] === "\t") index += 1;
  return code[index];
}

function atLineStart(code: string, index: number) {
  let cursor = index - 1;
  while (cursor >= 0 && (code[cursor] === " " || code[cursor] === "\t")) cursor -= 1;
  return cursor < 0 || code[cursor] === "\n";
}

export function tokenizePython(code: string): Token[] {
  const tokens: Token[] = [];
  let index = 0;
  let pendingName: "function" | "type" | undefined;

  const push = (kind: TokenKind, text: string) => {
    const last = tokens[tokens.length - 1];
    if (last && last.kind === kind && kind === "plain") last.text += text;
    else tokens.push({ kind, text });
  };

  while (index < code.length) {
    const char = code[index];

    if (char === "#") {
      const end = code.indexOf("\n", index);
      const stop = end === -1 ? code.length : end;
      push("comment", code.slice(index, stop));
      index = stop;
      continue;
    }

    if (char === `"` || char === "'") {
      const end = readString(code, index);
      push("string", code.slice(index, end));
      index = end;
      continue;
    }

    if (char === "@" && atLineStart(code, index)) {
      IDENTIFIER.lastIndex = index + 1;
      const match = IDENTIFIER.exec(code);
      if (match) {
        let end = index + 1 + match[0].length;
        while (code[end] === ".") {
          IDENTIFIER.lastIndex = end + 1;
          const part = IDENTIFIER.exec(code);
          if (!part) break;
          end += 1 + part[0].length;
        }
        push("decorator", code.slice(index, end));
        index = end;
        continue;
      }
    }

    if (/[0-9]/.test(char) || (char === "." && /[0-9]/.test(code[index + 1] ?? ""))) {
      NUMBER.lastIndex = index;
      const match = NUMBER.exec(code);
      if (match && match[0]) {
        push("number", match[0]);
        index += match[0].length;
        continue;
      }
    }

    IDENTIFIER.lastIndex = index;
    const identifier = IDENTIFIER.exec(code);
    if (identifier) {
      const word = identifier[0];
      const end = index + word.length;
      const following = code[end];

      // String prefixes such as f"..." or rb'...' belong to the string token.
      if ((following === `"` || following === "'") && STRING_PREFIX.test(word)) {
        const stringEnd = readString(code, end);
        push("string", code.slice(index, stringEnd));
        index = stringEnd;
        continue;
      }

      let kind: TokenKind = "plain";
      if (pendingName) {
        kind = pendingName;
        pendingName = undefined;
      } else if (KEYWORDS.has(word)) {
        kind = "keyword";
        if (word === "def") pendingName = "function";
        if (word === "class") pendingName = "type";
      } else if (CONTROL.has(word)) {
        kind = "control";
      } else if (CONSTANTS.has(word)) {
        kind = "constant";
      } else if (word === "self" || word === "cls") {
        kind = "self";
      } else if (TYPES.has(word)) {
        kind = "type";
      } else if (nextNonSpace(code, end) === "(") {
        kind = BUILTINS.has(word) ? "builtin" : "function";
      }

      push(kind, word);
      index = end;
      continue;
    }

    push("plain", char);
    index += 1;
  }

  return tokens;
}

function escapeHtml(value: string) {
  return value.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
}

function tokenHtml(kind: TokenKind, text: string) {
  const escaped = escapeHtml(text);
  return kind === "plain" || !text ? escaped : `<span class="py-${kind}">${escaped}</span>`;
}

/** Highlighted HTML that keeps the original line breaks (used under the editor textarea). */
export function highlightPython(code: string) {
  return tokenizePython(code)
    .map((token) => tokenHtml(token.kind, token.text))
    .join("");
}

/** Highlighted HTML wrapped in `.code-line` spans, the markup used by CopyCodeBlock. */
export function highlightPythonLines(code: string) {
  const lines: string[] = [""];

  for (const token of tokenizePython(code)) {
    token.text.split("\n").forEach((part, partIndex) => {
      if (partIndex > 0) lines.push("");
      lines[lines.length - 1] += tokenHtml(token.kind, part);
    });
  }

  return lines.map((line) => `<span class="code-line">${line}</span>`).join("");
}
