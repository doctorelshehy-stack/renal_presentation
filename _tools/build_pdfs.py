#!/usr/bin/env python3
"""Build one PDF per top-level topic folder. Each page = one slide PNG at exact image size."""
import pathlib, re, sys
import img2pdf

ROOT = pathlib.Path(__file__).resolve().parent.parent

def natural_key(p: pathlib.Path):
    return [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", p.name)]

def collect_pngs(folder: pathlib.Path):
    """All slides/png/*.png across topics, in topic order then natural slide order."""
    topics = sorted([d for d in folder.iterdir() if d.is_dir() and not d.name.startswith("_")])
    files = []
    for t in topics:
        png_dir = t / "slides" / "png"
        if png_dir.is_dir():
            files.extend(sorted(png_dir.glob("*.png"), key=natural_key))
    return files

def main():
    for folder in sorted([d for d in ROOT.iterdir() if d.is_dir() and d.name.endswith("_topics")]):
        files = collect_pngs(folder)
        if not files:
            print(f"SKIP {folder.name}: no slide PNGs")
            continue
        # sanity check all are the same size (PDF requirement: page = image size)
        sizes = {}
        for f in files:
            with open(f, "rb") as fh:
                head = fh.read(33)
                if head[:8] == b"\x89PNG\r\n\x1a\n":
                    w, h = int.from_bytes(head[16:20], "big"), int.from_bytes(head[20:24], "big")
                    sizes[(w, h)] = sizes.get((w, h), 0) + 1
        out = ROOT / f"{folder.name.replace('_topics', '').title()}_Slides.pdf"
        with open(out, "wb") as f:
            f.write(img2pdf.convert([str(f) for f in files]))
        print(f"OK {out.name}: {len(files)} pages, sizes={sizes}")

if __name__ == "__main__":
    sys.exit(main())
