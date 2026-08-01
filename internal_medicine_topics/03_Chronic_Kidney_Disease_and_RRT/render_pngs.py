#!/usr/bin/env python3
"""Render slides/*.html -> slides/png/slide-XX.png at 960x540 using Playwright."""
import os
import sys
from playwright.sync_api import sync_playwright

BASE = os.path.dirname(os.path.abspath(__file__))
SLIDES = os.path.join(BASE, 'slides')
PNG = os.path.join(SLIDES, 'png')
os.makedirs(PNG, exist_ok=True)

N = int(sys.argv[1]) if len(sys.argv) > 1 else 32
START = int(sys.argv[2]) if len(sys.argv) > 2 else 1

with sync_playwright() as p:
    browser = p.chromium.launch(args=['--no-sandbox', '--disable-dev-shm-usage'])
    page = browser.new_page(viewport={'width': 960, 'height': 540})
    for i in range(START, N + 1):
        num = f'{i:02d}'
        html = os.path.join(SLIDES, f'slide-{num}.html')
        out = os.path.join(PNG, f'slide-{num}.png')
        page.goto(f'file://{html}')
        page.wait_for_timeout(250)
        page.screenshot(path=out)
        print(f'rendered {num}', flush=True)
    browser.close()
print('DONE')
