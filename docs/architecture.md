# Architektúra

## Rozhodnutie po prerobení

Projekt používa jednoduchú architektúru vhodnú pre jeden univerzitný predmet a jedného správcu:

- statický web v Astro;
- spoločné metadata v `shared/`;
- izolované adresáre týždňov v `weeks/`;
- editovateľné PowerPoint prezentácie v jednom priečinku;
- rovnaký webový viewer nad odvodenými obrázkami slajdov.

Prednáška na webe zostáva primárny formát pre študenta. Študent po otvorení konkrétnej prednášky vidí priamo slajd, nie stránku s metadátami, kartami alebo dodatočnou navigáciou.

## Tok dát

```text
weeks/week-XX-*/week.config.ts
  -> shared/weeks.ts
  -> /prednasky, /cvicenia a navigácia obsahu

presentations/01-uvod-ku-pythonu.sk.pptx
  -> scripts/render-presentations.mjs
  -> web/static/generated/presentations/
  -> shared/presentations.ts
  -> /prednasky/01-uvod-ku-pythonu/
```

## Zdroje pravdy

- `shared/course.config.ts`: názov predmetu, univerzita, fakulta, program, základná navigácia.
- `weeks/*/week.config.ts`: číslo, slug, názov, anotácia, status a dostupnosť materiálov.
- `presentations/*.sk.pptx` a `presentations/*.en.pptx`: editovateľné zdroje slajdov.
- `scripts/render-presentations.mjs`: vytvára odvodené PNG náhľady pre webový viewer.
- `web/src/styles/global.css`: spoločný vizuálny systém webu a slajdov.

## Python v prehliadači (Pyodide)

Úlohy cvičení môžu mať editor, v ktorom študent spustí Python priamo na stránke. Kód beží v prehliadači cez [Pyodide](https://pyodide.org/), teda CPython skompilovaný do WebAssembly. Nič sa neposiela na server, takže web zostáva statický.

```text
exercises/exercise-XX/playground/task_YY.sk.py / .en.py   začiatočný kód (overuje ho npm run validate)
exercises/exercise-XX/playground/workspace.json           voliteľné testovacie súbory pre pracovný priečinok
  -> web/src/lib/python-runner/sources.ts                  načíta ich pri builde
  -> web/src/components/PythonPlayground.astro             editor, tlačidlá, výstup
  -> web/src/lib/python-runner/runner.ts                   jeden zdieľaný interpreter na stránku
  -> web/src/lib/python-runner/worker.ts                   Pyodide vo Web Workeri
```

Použitie v stránke cvičenia, na konci sekcie úlohy:

```astro
<PythonPlayground exercise="01" task="03" />
```

Rozhodnutia:

- Pyodide sa sťahuje z jsDelivr CDN až pri prvom zameraní editora alebo spustení. Verzia je pripnutá v `runner.ts` (`PYODIDE_VERSION`).
- Interpreter beží vo Web Workeri, aby nekonečný cyklus nezamrazil stránku. Tlačidlo „Zastaviť“ worker ukončí a ďalšie spustenie ho vytvorí znova. Prerušenie cez `SharedArrayBuffer` by vyžadovalo COOP/COEP hlavičky, ktoré GitHub Pages nenastaví.
- Každé spustenie má nový menný priestor `__main__`, takže úlohy sa navzájom neovplyvňujú a funguje vzor `if __name__ == "__main__":`.
- `input()` nie je podporovaný; vstupné dáta sú priamo v kóde úlohy.
- Program beží v pracovnom priečinku virtuálneho súborového systému Pyodide (`/home/pyodide/workspace`), ktorý sa pred každým spustením vytvorí nanovo. Ak cvičenie pracuje so súbormi, `playground/workspace.json` určí, ktoré cesty z `exercises/exercise-XX/` sa doň skopírujú, napr. `{ "copy": ["subory"] }` v Cvičení 02. Ide o tie isté testovacie dáta ako v starter ZIP, presuny v editore nemenia súbory na disku študenta a validácia spúšťa kód editora s rovnakou kópiou.
- Príkazový riadok v editore nie je. Úlohy s `argparse` volajú `parse_args()` so zoznamom argumentov, napr. `parse_args(["subory", "--vykonat"])`.
- Editor vie zobraziť vzorové riešenie tlačidlom „Zobraziť riešenie“, ak v `playground/` existuje `solution_YY.{sk,en}.py`. Momentálne je to vypnuté: riešenia Cvičenia 01 sú iba lokálne v neverejnom `solutions/exercise-01/` (ignorované Gitom), takže sa tlačidlo nezobrazí. Zapnúť sa dá presunutím týchto súborov späť do `playground/`, ak to vyučujúci schváli.
- Rozpracovaný kód sa ukladá iba do `localStorage` (`python-course.exercise.XX.task.YY.code`). Nezmenený začiatočný kód sa pri prepnutí jazyka prepne na druhú jazykovú verziu.

## Čo tu zámerne nie je

Nie je tu backend, databáza, admin rozhranie, CMS, autentifikácia, serverové vyhľadávanie ani komplexný prezentačný framework. Projekt má zostať priamo editovateľný a ľahko pochopiteľný.

## Výstupy

Statický web sa builduje do:

```text
dist/web/
```

Zdrojové PPTX súbory sú v:

```text
presentations/
```

PDF a obrázkové preview sú odvodené build artefakty a necommitujú sa. Renderovanie používa LibreOffice a `pdftoppm`.
