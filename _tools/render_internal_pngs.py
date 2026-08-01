#!/usr/bin/env python3
"""Render every slide in internal_medicine_topics deck HTMLs to 960x540 PNGs."""
import re, pathlib, sys
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
TOPIC = ROOT / "internal_medicine_topics"

HIDE_CHROME = "#counter,#progress,.deck-nav{display:none!important}"

def deck_slides(html: pathlib.Path):
    """Return list of data-n values in DOM order."""
    text = html.read_text(encoding="utf-8")
    return [m.group(1) for m in re.finditer(r'<section class="slide[^"]*" data-n="(\d+)"', text)]

def main():
    decks = sorted([p for p in TOPIC.glob("0*/*.html") if p.is_file()])
    # group decks by topic folder so numbering is continuous per folder
    from collections import OrderedDict
    groups = OrderedDict()
    for d in decks:
        groups.setdefault(d.parent, []).append(d)
    total = 0
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        for topic_dir, deck_list in groups.items():
            out_dir = topic_dir / "slides" / "png"
            out_dir.mkdir(parents=True, exist_ok=True)
            n = 0
            for deck in deck_list:
                data_n = deck_slides(deck)
                if not data_n:
                    print(f"SKIP {deck.name}: no slides")
                    continue
                page = browser.new_page(viewport={"width": 960, "height": 540})
                uri = deck.resolve().as_uri()
                for dn in data_n:
                    n += 1
                    page.goto(uri + f"#{dn}", wait_until="load")
                    page.wait_for_timeout(120)
                    page.add_style_tag(content=HIDE_CHROME)
                    page.wait_for_timeout(120)
                    out = out_dir / f"slide-{n:03d}.png"
                    page.screenshot(path=str(out))
                page.close()
                print(f"OK {deck.relative_to(TOPIC)}  -> {len(data_n)} slides")
            print(f"TOPIC {topic_dir.name}: {n} slides total")
        browser.close()
    print(f"DONE: {total} slides rendered")

if __name__ == "__main__":
    sys.exit(main())
