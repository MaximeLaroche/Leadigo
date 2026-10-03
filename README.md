# Leadigo Website

Source for [leadigo.io](https://leadigo.io). Static site, no build step — plain HTML/CSS/JS served by GitHub Pages from the `docs/` folder on the `main` branch.

## Layout

```
docs/
  index.html            Homepage (VSL page)
  roi_calculator.html   ROI calculator (also embedded in the homepage)
  strategy_call.html    Strategy call page
  language.js           Language + flag-switcher logic (loaded by every page)
  locales/
    fr.json             French translations
    es.json             Spanish translations
```

## How the language system works

- Each page exists **once**, in English. The English text in the HTML is the source of truth.
- The flag buttons (🇬🇧 🇫🇷 🇪🇸) call `language.js`, which fetches `locales/<lang>.json` and swaps matching text on the page — no reload, and the embedded ROI calculator switches too (parent page passes the language into the iframe).
- Each JSON file is a simple map: **English source text → translated text**.

```json
"But none of those channels are predictable.": "Mais aucun de ces canaux n’est prévisible.",
```

- If a sentence on the page has **no matching key** in the JSON, it simply stays in English. Nothing breaks.
- The visitor's choice is remembered in `localStorage` (`leadigo-lang`). First visit picks the browser language when it's French or Spanish.

## Editing a translation

1. Open `docs/locales/fr.json` (or `es.json`).
2. Find the English sentence as the **key** (left side) and edit the **value** (right side).
3. Save, push — done.

Rules that matter:

- **Never edit a key.** The key must match the English text in the HTML *exactly*, character for character — including punctuation, apostrophes, and capitalization — or the lookup silently misses and the text stays English.
- Curly apostrophes (`’`) and accented characters are fine; the files are UTF-8.
- Keep it valid JSON: every line ends with a comma except the last, and any double quote inside a value must be escaped (`\"`). If the site suddenly stops translating after an edit, a missing comma is almost always the cause — paste the file into [jsonlint.com](https://jsonlint.com) to check.
- The `"__theme"` block at the top of each file translates the theme switcher's tooltip ("Theme: System/Light/Dark"). Same rules apply.

## Changing page text

When you edit English copy in an HTML file:

1. Change the text in the HTML.
2. In **both** `fr.json` and `es.json`, find the old sentence key, replace it with the new English sentence (exactly as it now appears in the HTML), and update the translation.
3. Any key whose English no longer exists on the page is harmless dead weight, but it's good hygiene to remove it.

Adding brand-new text follows the same pattern: write the English in the HTML, then add a new entry with that exact sentence as the key in each locale file.

Special case — the `.scrub-words` animation: the sentence "But none of those channels are predictable." is split into per-word spans by a scroll animation. `language.js` handles it as a whole sentence and re-splits after translating, so it translates like any other text — just keep the JSON key matching the full sentence.

## Testing locally

From the repo root:

```
python -m http.server 8123 --directory docs
```

Then open <http://localhost:8123/> and click the flags. (Any static server works; this one just needs Python.)

## Publishing

Push to `main` and GitHub Pages redeploys automatically (usually under a minute). If the site looks unchanged after a deploy, do one hard refresh (Ctrl+Shift+R) to clear cached JavaScript — after that, language switches are instant.

## Themes

The site has light/dark/system themes (toggle next to the flags), independent of language. Default is `system`, which follows the visitor's OS setting.
