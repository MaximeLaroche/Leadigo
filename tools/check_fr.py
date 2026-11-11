import re
from pathlib import Path
from bs4 import BeautifulSoup

DOCS = Path(__file__).resolve().parents[1] / "docs"
PROPER = (
    "Leadigo", "Maxime", "Phil Kirkeiner", "Sunny Stuart", "Baton", "Fithive",
    "@", "http", "Calendly", "YouTube", "LinkedIn", "Instagram"
)
ACRONYMS = {"FAQ", "ROI", "ICP", "SPF", "DKIM", "DMARC", "DNS", "B2B", "SaaS", "LTV"}


def texts(path):
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
    for tag in soup(["script", "style"]):
        tag.decompose()
    return [t.strip() for t in soup.stripped_strings if t.strip()]


def allowed_same(s):
    if any(p in s for p in PROPER):
        return True
    words = re.findall(r"[A-Za-zÀ-ÿ]+", s)
    if not words:
        return True
    if all(w in ACRONYMS or w.isupper() or len(w) <= 2 for w in words):
        return True
    return False


bad = 0
for name in ["index", "roi_calculator", "strategy_call"]:
    en = texts(DOCS / f"{name}.html")
    fr = texts(DOCS / f"{name}-fr.html")
    print(f"{name}: en={len(en)} fr={len(fr)}")
    for i, (a, b) in enumerate(zip(en, fr)):
        if a == b and re.search(r"[A-Za-z]{3,}", a) and not allowed_same(a):
            bad += 1
            print(f"  SAME[{i}]: {a!r}")
    if len(en) != len(fr):
        print(f"  LENGTH MISMATCH for {name}")
print(f"potentially untranslated text nodes: {bad}")
