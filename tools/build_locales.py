import json
from pathlib import Path
from bs4 import BeautifulSoup

DOCS = Path(__file__).resolve().parents[1] / "docs"
PAGES = ["index", "roi_calculator", "strategy_call"]
LANGS = {"fr": "fr", "es": "es"}

MANUAL = {
    "fr": {
        "Theme: system, light, or dark": "Thème : système, clair ou sombre",
        "ROI Calculator": "Calculateur de ROI",
        "Phil Kirkeiner Case Study": "Étude de cas Phil Kirkeiner",
        "Sunny Stuart Case Study": "Étude de cas Sunny Stuart",
        "Maxime - Founder of Leadigo": "Maxime — fondateur de Leadigo",
        "Infinite": "Infini",
        "__theme": {
            "themePrefix": "Thème : ",
            "clickSuffix": " (cliquez pour changer)",
            "System": "Système",
            "Light": "Clair",
            "Dark": "Sombre",
        },
    },
    "es": {
        "Theme: system, light, or dark": "Tema: sistema, claro u oscuro",
        "ROI Calculator": "Calculadora de ROI",
        "Phil Kirkeiner Case Study": "Caso de estudio de Phil Kirkeiner",
        "Sunny Stuart Case Study": "Caso de estudio de Sunny Stuart",
        "Maxime - Founder of Leadigo": "Maxime — fundador de Leadigo",
        "Infinite": "Infinito",
        "__theme": {
            "themePrefix": "Tema: ",
            "clickSuffix": " (haz clic para cambiar)",
            "System": "Sistema",
            "Light": "Claro",
            "Dark": "Oscuro",
        },
    },
}


def texts(path):
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()
    return [t.strip() for t in soup.stripped_strings if t.strip()]


out = {lang: dict(MANUAL[lang]) for lang in LANGS}
for page in PAGES:
    en = texts(DOCS / f"{page}.html")
    for lang in LANGS:
        other = texts(DOCS / f"{page}-{lang}.html")
        if len(en) != len(other):
            raise SystemExit(f"Text node count mismatch on {page} ({lang}): {len(en)} vs {len(other)}")
        for source, translated in zip(en, other):
            if source == translated:
                continue
            if source in out[lang] and out[lang][source] != translated:
                print(f"conflict [{lang}] {source!r}: keeping {out[lang][source]!r}, ignoring {translated!r}")
                continue
            out[lang][source] = translated

(DOCS / "locales").mkdir(exist_ok=True)
for lang, mapping in out.items():
    (DOCS / "locales" / f"{lang}.json").write_text(json.dumps(mapping, ensure_ascii=False, indent=2), encoding="utf-8")
    print(lang, len(mapping) - 1, "text mappings")
