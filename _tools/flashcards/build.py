#!/usr/bin/env python3
"""Build all flashcard decks + index page."""
import sys, html as H
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from gen import build_deck, THEMES, OUT
from cards_im import ALL_IM
from cards_ped import ALL_PED
from cards_uro import ALL_URO

def main():
    built = []  # (course, group_id, title, n)
    for gid, title, cards in ALL_IM:
        fname = build_deck(THEMES['im'], 'Internal Medicine', 'im_' + gid, title, '', cards)
        built.append(('im', 'im_' + gid, title, len(cards)))
        print('built', fname.name, len(cards))
    for gid, title, cards in ALL_PED:
        fname = build_deck(THEMES['ped'], 'Pediatrics', 'ped_' + gid, title, '', cards)
        built.append(('ped', 'ped_' + gid, title, len(cards)))
        print('built', fname.name, len(cards))
    for gid, title, cards in ALL_URO:
        fname = build_deck(THEMES['uro'], 'Urology', 'uro_' + gid, title, '', cards)
        built.append(('uro', 'uro_' + gid, title, len(cards)))
        print('built', fname.name, len(cards))

    total = sum(b[3] for b in built)
    # ---- index page ----
    course_meta = {
        'im': ('Internal Medicine · Nephrology', '5 topic decks — glomerular disease to electrolytes', THEMES['im']),
        'ped': ('Pediatric Nephrology', '9 topic decks — anatomy to UTIs in children', THEMES['ped']),
        'uro': ('Urology', '5 topic decks — oncology to trauma', THEMES['uro']),
    }
    order = ['im', 'ped', 'uro']
    cards_html = ''
    for c in order:
        name, desc, th = course_meta[c]
        decks = [b for b in built if b[0] == c]
        n_cards = sum(b[3] for b in decks)
        deck_items = ''.join(
            f'<a class="deck" href="{gid}.html"><span class="dnum">{i+1:02d}</span><span class="dtitle">{H.escape(t)}</span><span class="dcount">{n} cards</span></a>'
            for i, (_, gid, t, n) in enumerate(decks)
        )
        cards_html += f'''
        <section>
          <div class="chead">
            <span class="cbadge" style="background:{th['accent']}">{name}</span>
            <span class="cdesc">{desc} · <b>{n_cards}</b> cards total</span>
          </div>
          <div class="decklist">{deck_items}</div>
        </section>'''

    index = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Nephro-Urology Flashcards — Index</title>
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: 'Times New Roman', Georgia, serif; background: #F5EFE4; color: #2E2318; padding: 28px; }}
.hero {{ background: linear-gradient(135deg,#2E2318,#6B4A28 60%,#B0722F); color: #FBF3E4; border-radius: 16px; padding: 30px 34px; margin-bottom: 26px; }}
.hero h1 {{ font-size: 30px; letter-spacing: 1px; }}
.hero p {{ margin-top: 8px; font-size: 15px; opacity: .92; max-width: 900px; line-height: 1.5; }}
.hero .stat {{ display: inline-block; margin-top: 14px; background: rgba(255,255,255,.12); border: 1px solid rgba(255,255,255,.25); padding: 5px 14px; border-radius: 20px; font-size: 13.5px; margin-right: 8px; }}
section {{ margin-bottom: 26px; }}
.chead {{ display: flex; align-items: baseline; gap: 14px; margin-bottom: 12px; flex-wrap: wrap; }}
.cbadge {{ color: #fff; padding: 5px 16px; border-radius: 20px; font-size: 15px; font-weight: 700; letter-spacing: 1px; }}
.cdesc {{ font-size: 14px; color: #5A4A33; }}
.decklist {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 12px; }}
.deck {{ display: flex; align-items: center; gap: 12px; background: #fff; border: 1px solid #E0D2B8; border-left: 5px solid var(--ac,#B0722F); border-radius: 12px; padding: 13px 16px; text-decoration: none; color: #2E2318; transition: transform .12s, box-shadow .12s; }}
.deck:hover {{ transform: translateY(-2px); box-shadow: 0 8px 18px rgba(0,0,0,.12); }}
.deck[data-c="ped"] {{ border-left-color: #2E7D8C; }}
.deck[data-c="uro"] {{ border-left-color: #4F7A3A; }}
.dnum {{ font-size: 18px; font-weight: 700; color: var(--ac,#B0722F); min-width: 30px; }}
.deck[data-c="ped"] .dnum {{ color: #2E7D8C; }}
.deck[data-c="uro"] .dnum {{ color: #4F7A3A; }}
.dtitle {{ font-size: 16px; font-weight: 700; flex: 1; }}
.dcount {{ font-size: 12.5px; color: #7A6A50; background: #F5EFE4; padding: 3px 10px; border-radius: 12px; white-space: nowrap; }}
footer {{ margin-top: 26px; font-size: 12.5px; color: #8A7A60; }}
</style>
</head>
<body>
<div class="hero">
  <h1>Nephro-Urology Flashcards</h1>
  <p>Interactive flip-card decks generated from the course slide presentations (Internal Medicine — Nephrology, Pediatric Nephrology, Urology). Click a deck, click the card to reveal the answer, and use the arrow keys or on-screen buttons to navigate. Use <b>Shuffle</b> for self-testing and the category chips to focus on one chapter at a time.</p>
  <div class="stat">🗂 {len(built)} topic decks</div>
  <div class="stat">🃏 {total} flashcards</div>
  <div class="stat">⌨️ Space = flip · ← → = navigate · S = shuffle</div>
</div>
{cards_html}
<footer>Flashcards are study aids derived from the course slides — always verify details against the original lecture materials. Decks: open each .html file in any browser (no internet needed).</footer>
</body>
</html>'''
    (OUT / 'index.html').write_text(index, encoding='utf-8')
    print('built index.html — total cards:', total)

if __name__ == '__main__':
    main()
