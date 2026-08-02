import re, html, json, sys
from pathlib import Path

def extract_text(path):
    content = path.read_text(encoding='utf-8')
    m = re.search(r'<div class="slide-content"(.*?)</div>\s*</body>', content, re.S)
    if not m:
        m = re.search(r'<body>(.*?)</body>', content, re.S)
    body = m.group(1) if m else content
    body = re.sub(r'<svg.*?</svg>', ' ', body, flags=re.S)
    texts = re.findall(r'>([^<>]+)<', body)
    out = []
    for t in texts:
        t = html.unescape(t).strip()
        t = re.sub(r'\s+', ' ', t)
        if t: out.append(t)
    return ' | '.join(out)

def group_title(path):
    content = path.read_text(encoding='utf-8')
    # try to find title patterns
    m = re.search(r'font-size:(?:28|30|34|40|50|62)px[^>]*>([^<]+)<', content)
    return m.group(1).strip() if m else path.name

if __name__ == '__main__':
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')
    out = []
    for slides_dir in sorted(root.glob('*/slides')):
        group = slides_dir.parent.name
        slides = sorted(slides_dir.glob('slide-*.html'))
        entries = []
        for s in slides:
            txt = extract_text(s)
            entries.append({'slide': s.name, 'text': txt})
        out.append({'group': group, 'slides': entries})
    print(json.dumps(out, ensure_ascii=False, indent=1))
