#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Glomerular Diseases — Full-Content Slide Deck Builder
Light mode · Brown background · Harmony (analogous warm) palette
Contrast (burgundy/terracotta) reserved for important information.
No summarization: every heading, bullet, table cell and note is preserved.
"""
import os

# ============================================================
# THEME — Harmony warm-brown palette (light mode)
# ============================================================
C = {
    'page':   '#1F1207',   # page surround (outside the slide)
    'bg':     '#F2E4CE',   # slide background — light warm brown (light mode)
    'card':   '#FBF3E4',   # cream card
    'cardT':  '#F4E8D2',   # deeper tan card
    'ink':    '#3A2A18',   # main text — dark brown
    'soft':   '#6B5238',   # secondary text
    'deep':   '#4A2F16',   # headings / top band / table header
    'brown':  '#7A5233',   # primary accent — medium brown
    'caramel':'#B0722F',   # caramel accent
    'gold':   '#A86E1C',   # golden highlight (contrast-safe on light bg)
    'terra':  '#B5522E',   # terracotta — warnings
    'burg':   '#8E3B2B',   # burgundy — IMPORTANT / high contrast
    'olive':  '#5F6B2E',   # olive — notes / N.B.
    'cream':  '#FBF3E4',   # light text on dark panels
    'white':  '#FFFFFF',
}

FONT = "Times New Roman, serif"

PAGE = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
html, body {{ margin:0; padding:0; width:100%; height:100%; overflow:hidden; display:flex; justify-content:center; align-items:center; background:#1F1207; }}
.slide-content {{ width:960px; height:540px; position:relative; transform-origin:center center; }}
</style>
<script>
function scaleSlide(){{const s=document.querySelector('.slide-content');if(!s)return;const sx=window.innerWidth/960;const sy=window.innerHeight/540;const sc=Math.min(sx,sy);s.style.width='960px';s.style.height='540px';s.style.transform='scale('+sc+')';s.style.transformOrigin='center center';s.style.flexShrink='0';}}
window.addEventListener('load',scaleSlide);window.addEventListener('resize',scaleSlide);
</script>
</head>
<body>
<div class="slide-content" style="width:960px;height:540px;background:{C['bg']};font-family:'{FONT}';overflow:hidden;">
{{CONTENT}}
</div>
</body>
</html>
"""

def badge(num, right=28):
    return f'''<svg style="position:absolute;right:{right}px;bottom:20px;width:46px;height:34px;z-index:100;" aria-hidden="true">
  <rect x="0" y="0" width="46" height="34" rx="7" fill="{C['caramel']}"/>
  <rect x="2.5" y="2.5" width="41" height="29" rx="5.5" fill="none" stroke="{C['cream']}" stroke-width="1"/>
  <text x="23" y="23" font-family="{FONT}" font-size="15.5" font-weight="700" fill="{C['white']}" text-anchor="middle">{num}</text>
</svg>'''

def wrap(body, num=None, foot=None, badge_right=28):
    b = badge(num, badge_right) if num else ''
    f = ''
    if foot:
        f = f'<div style="position:absolute;left:52px;bottom:24px;font-size:10.5px;color:{C["soft"]};font-style:italic;">{foot}</div>'
    return PAGE.replace('{CONTENT}', body + f + b)

# ---------- building blocks ----------

def top_band(tag, title, title_fs=28):
    """Title area for content slides."""
    return f'''<div style="position:absolute;top:0;left:0;width:960px;height:10px;background:linear-gradient(90deg,{C['deep']},{C['brown']},{C['caramel']},{C['gold']});"></div>
<div style="position:absolute;top:26px;left:52px;right:52px;">
  <p style="font-size:12px;color:{C['caramel']};letter-spacing:2.5px;font-weight:700;margin:0;text-transform:uppercase;">{tag}</p>
  <p style="font-size:{title_fs}px;color:{C['deep']};margin:1px 0 0 0;font-weight:700;line-height:1.1;">{title}</p>
  <div style="width:64px;height:4px;background:{C['caramel']};margin:6px 0 0 0;border-radius:2px;"></div>
</div>'''

def body(top=112, bottom=64):
    return f'<div style="position:absolute;top:{top}px;left:52px;right:52px;bottom:{bottom}px;">'

def card(html, accent='brown', bg=None, pad='12px 14px', left='5px', title=None, title_fs=16, title_color=None, fs=13, lh=1.45):
    col = C[accent]
    bkg = bg or C['card']
    tc = title_color or C['deep']
    t = ''
    if title:
        t = f'<p style="font-size:{title_fs}px;font-weight:700;color:{tc};margin:0 0 6px 0;">{title}</p>'
    return f'''<div style="background:{bkg};border:1px solid #E2CFAD;border-left:{left}px solid {col};border-radius:10px;padding:{pad};">
{t}<div style="font-size:{fs}px;color:{C['ink']};line-height:{lh};">{html}</div>
</div>'''

def grid(cols, gap=14):
    return f'<div style="display:grid;grid-template-columns:{cols};gap:{gap}px;">'

def imp(html, title=None):
    """High-contrast IMPORTANT box — burgundy."""
    t = f'<b style="color:{C["burg"]};">⚠ Important:</b> ' if not title else f'<b style="color:{C["burg"]};">{title}:</b> '
    return f'''<div style="background:rgba(142,59,43,0.09);border:1.5px solid {C['burg']};border-radius:8px;padding:8px 12px;">
<p style="font-size:13px;color:{C['ink']};margin:0;line-height:1.45;">{t}{html}</p></div>'''

def warn(html, title='Warning'):
    t = f'<b style="color:{C["terra"]};">{title}:</b> '
    return f'''<div style="background:rgba(181,82,46,0.10);border:1.5px solid {C['terra']};border-radius:8px;padding:8px 12px;">
<p style="font-size:13px;color:{C['ink']};margin:0;line-height:1.45;">{t}{html}</p></div>'''

def note(html, title='N.B.', fs=12.5):
    t = f'<b style="color:{C["olive"]};">{title}:</b> ' if title else ''
    return f'''<div style="background:rgba(95,107,46,0.10);border-left:4px solid {C['olive']};border-radius:6px;padding:7px 12px;">
<p style="font-size:{fs}px;color:{C['ink']};margin:0;line-height:1.4;">{t}{html}</p></div>'''

def key(html):
    """Golden highlight chip for key terms/numbers."""
    return f'<span style="background:rgba(168,110,28,0.16);border:1px solid #D3A75B;color:{C["deep"]};font-weight:700;border-radius:14px;padding:0.5px 8px;font-size:95%;">{html}</span>'

def b(html, color=None):
    col = color or C['burg']
    return f'<b style="color:{col};">{html}</b>'

def e(html, color=None):
    """Emphasized text (caramel brown)."""
    col = color or C['caramel']
    return f'<b style="color:{col};">{html}</b>'

def ul(items, fs=13, gap='3px', pad='18px'):
    lis = ''
    for it in items:
        lis += f'<li style="margin:0 0 {gap} 0;">{it}</li>'
    return f'<ul style="margin:0;padding-left:{pad};font-size:{fs}px;color:{C["ink"]};line-height:1.45;">{lis}</ul>'

def tbl(headers, rows, widths=None, fs=12.5, hfs=13, tpad=5):
    n = len(headers)
    w = widths or [100.0/n]*n
    wc = ''.join(f'<col style="width:{x}%;">' for x in w)
    thr = ''.join(f'<th style="padding:{tpad}px 9px;font-size:{hfs}px;text-align:left;background:{C["deep"]};color:{C["cream"]};font-weight:700;border:1px solid #3A2A18;">{h}</th>' for h in headers)
    trs = []
    for i, row in enumerate(rows):
        bgc = '#FDF7EB' if i % 2 == 0 else '#F5E9D3'
        tds = ''.join(f'<td style="padding:{tpad}px 9px;font-size:{fs}px;border:1px solid #D9C4A4;color:{C["ink"]};line-height:1.4;vertical-align:top;">{c}</td>' for c in row)
        trs.append(f'<tr style="background:{bgc};">{tds}</tr>')
    return f'<table style="width:100%;border-collapse:collapse;border:1px solid #D9C4A4;border-radius:8px;overflow:hidden;box-shadow:0 1px 3px rgba(74,47,22,0.12);"><colgroup>{wc}</colgroup><tr>{thr}</tr>{"".join(trs)}</table>'

# ============================================================
# SLIDES
# ============================================================
slides = []  # list of (raw_body, foot, show_badge)

def add(body_html, num=None, foot=None, badge_right=28):
    slides.append((body_html, foot, True, badge_right))

# ------------------------------------------------------------
# 1 — COVER
# ------------------------------------------------------------
cover = f'''<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:linear-gradient(135deg,#3E2A16 0%,#6B4A28 55%,#8A6238 100%);"></div>
<div style="position:absolute;top:0;left:0;width:26px;height:540px;background:linear-gradient(180deg,#B0722F,#D3A75B);"></div>
<div style="position:absolute;bottom:0;left:26px;width:934px;height:14px;background:linear-gradient(90deg,#B0722F,#A86E1C);"></div>
<svg style="position:absolute;top:-90px;right:-70px;width:520px;height:420px;z-index:1;" aria-hidden="true">
  <circle cx="260" cy="210" r="205" fill="#B0722F" opacity="0.16"/>
  <circle cx="260" cy="210" r="150" fill="#D3A75B" opacity="0.12"/>
</svg>
<svg style="position:absolute;bottom:-80px;left:120px;width:420px;height:300px;z-index:1;" aria-hidden="true">
  <ellipse cx="200" cy="150" rx="220" ry="120" fill="#3E2A16" opacity="0.35"/>
</svg>
<div style="position:absolute;top:88px;left:70px;right:70px;z-index:10;">
  <div style="width:84px;height:5px;background:#D3A75B;border-radius:2px;margin-bottom:18px;"></div>
  <p style="font-size:20px;color:#D3A75B;margin:0;font-weight:400;letter-spacing:5px;">INTERNAL MEDICINE · NEPHROLOGY</p>
  <p style="font-size:62px;color:#FBF3E4;margin:10px 0 0 0;font-weight:700;line-height:1.05;">Glomerular Diseases</p>
  <p style="font-size:40px;color:#E8C98A;margin:4px 0 0 0;font-weight:700;">Principles of Glomerulopathies</p>
  <div style="width:64px;height:4px;background:#B0722F;margin:22px 0 16px 0;border-radius:2px;"></div>
  <p style="font-size:21px;color:#FBF3E4;margin:0;font-weight:400;">Acute GN · Nephrotic Syndrome · Anti-GBM · PSGN · Lupus Nephritis · Diabetic Nephropathy</p>
</div>
<div style="position:absolute;bottom:34px;left:70px;z-index:10;">
  <p style="font-size:16px;color:#FBF3E4;margin:0;opacity:0.95;">Dr. Hassan Abd-Elhady — Professor of Internal Medicine &amp; Nephrology</p>
  <p style="font-size:13px;color:#E8C98A;margin:3px 0 0 0;opacity:0.9;">Menoufia University · Principles of Nephrology</p>
</div>'''
add(cover, None)

# ------------------------------------------------------------
# 2 — TOC
# ------------------------------------------------------------
toc_items = [
    ('01', 'Principles of Glomerulopathies'),
    ('02', 'Acute Glomerulonephritis (Nephritic Syndrome)'),
    ('03', 'Nephrotic Syndrome'),
    ('04', 'Anti-GBM Disease &amp; Goodpasture Syndrome'),
    ('05', 'Post-Streptococcal Glomerulonephritis (PSGN)'),
    ('06', 'Lupus Nephritis'),
    ('07', 'Diabetic Nephropathy'),
]
toc_cells = ''
for num, t in toc_items:
    toc_cells += f'''<div style="display:flex;align-items:center;gap:14px;padding:11px 14px;background:{C['card']};border:1px solid #E2CFAD;border-left:5px solid {C['brown']};border-radius:10px;">
  <span style="font-size:19px;font-weight:700;color:{C['caramel']};min-width:34px;">{num}</span>
  <span style="font-size:16.5px;color:{C['deep']};font-weight:600;">{t}</span>
</div>'''
toc_body = f'''{top_band('Glomerular Diseases · Module Map', 'Table of Contents')}
{body(108, 78)}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">{toc_cells}</div>
<div style="margin-top:16px;">{note('All 7 chapters reproduced in full — definitions, classifications, tables, investigations, treatment protocols and course notes. Light-mode brown harmony theme; burgundy = important, terracotta = warning.', 'No summarization')}</div>
</div>'''
add(toc_body, 2)

# ------------------------------------------------------------
# 3 — SECTION DIVIDER helper
# ------------------------------------------------------------
def divider(num, title, subtitle, page):
    h = f'''<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:linear-gradient(120deg,#5A3D22 0%,#7A5233 70%,#8A6238 100%);"></div>
<div style="position:absolute;top:0;right:0;width:430px;height:540px;background:#B0722F;opacity:0.14;"></div>
<svg style="position:absolute;top:-70px;right:-60px;width:430px;height:430px;z-index:1;" aria-hidden="true">
  <circle cx="215" cy="215" r="200" fill="#D3A75B" opacity="0.12"/>
</svg>
<div style="position:absolute;top:0;left:0;width:16px;height:540px;background:linear-gradient(180deg,#D3A75B,#A86E1C);"></div>
<div style="position:absolute;top:128px;left:86px;z-index:10;">
  <p style="font-size:104px;font-weight:700;color:#D3A75B;margin:0;line-height:0.9;">{num}</p>
  <div style="width:86px;height:5px;background:#E8C98A;margin:14px 0 16px 0;border-radius:2px;"></div>
  <p style="font-size:37px;font-weight:700;color:#FBF3E4;margin:0;line-height:1.15;">{title}</p>
  <p style="font-size:19px;color:#E8C98A;margin:10px 0 0 0;">{subtitle}</p>
</div>
<div style="position:absolute;bottom:30px;left:86px;z-index:10;">
  <p style="font-size:12.5px;color:#F4E8D2;margin:0;opacity:0.85;">PRINCIPLES OF NEPHROLOGY · {page}</p>
</div>'''
    slides.append((h, None, False))

divider('01', 'Principles of Glomerulopathies', 'Definition · Causes · Pathology · Syndromes · Investigations · Treatment', 'Page 1–6')

# ------------------------------------------------------------
# 4 — CH1 · Definition & Clinical Features
# ------------------------------------------------------------
s4 = f'''{top_band('Ch 01 · Principles of Glomerulopathies', 'Definition & Clinical Features')}
{body(112, 54)}
{card('Term used to describe a group of glomerular disorders characterized by:', title='Definition', title_fs=16, pad='9px 14px')}
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;margin-top:8px;">
  <div style="background:#F4E8D2;border:1px solid #E2CFAD;border-radius:10px;padding:7px 11px;border-top:4px solid #7A5233;">
    <p style="font-size:13px;font-weight:700;color:#4A2F16;margin:0 0 2px 0;">Clinically</p>
    <p style="font-size:11.5px;color:#3A2A18;margin:0;line-height:1.35;">Presence of the following features, either singly or in combination.</p>
  </div>
  <div style="background:#F4E8D2;border:1px solid #E2CFAD;border-radius:10px;padding:7px 11px;border-top:4px solid #B0722F;">
    <p style="font-size:13px;font-weight:700;color:#4A2F16;margin:0 0 2px 0;">Pathologically</p>
    <p style="font-size:11.5px;color:#3A2A18;margin:0;line-height:1.35;">Involvement of both kidneys, either symmetrically.</p>
  </div>
  <div style="background:#F4E8D2;border:1px solid #E2CFAD;border-radius:10px;padding:7px 11px;border-top:4px solid #A86E1C;">
    <p style="font-size:13px;font-weight:700;color:#4A2F16;margin:0 0 2px 0;">Etiologically</p>
    <p style="font-size:11.5px;color:#3A2A18;margin:0;line-height:1.35;">Unknown (primary GN) or secondary to various causes (secondary GN).</p>
  </div>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:8px;">
  {card(ul(['<b style="color:#B0722F;">1. Proteinuria</b>', '<b style="color:#B0722F;">2. Hematuria</b>', '<b style="color:#B0722F;">3. Oliguria</b>', '<b style="color:#B0722F;">4. Hypertension</b>', '<b style="color:#B0722F;">5. Edema</b>'], fs=13), title='Five cardinal features', title_fs=14.5, pad='9px 12px')}
  {card('<b style="color:#5F6B2E;">Both kidneys are involved, either symmetrically.</b><br><br>• <b style="color:#8E3B2B;">Unknown cause</b> → <b>Primary GN</b> (idiopathic).<br>• <b style="color:#8E3B2B;">Secondary to various causes</b> → <b>Secondary GN</b>.', title='Involvement &amp; classification', title_fs=14.5, pad='9px 12px')}
</div>
<div style="margin-top:8px;">{imp('The term <b>glomerulopathy</b> covers a group of glomerular disorders recognized clinically (features), pathologically (symmetric bilateral kidney involvement) and etiologically (primary vs secondary).', 'Key')}</div>
</div>'''
add(s4, 4, foot='PRINCIPLES OF NEPHROLOGY — Page 1')

# ------------------------------------------------------------
# 5 — CH1 · Causes I (Primary + Infections + Multisystem)
# ------------------------------------------------------------
s5 = f'''{top_band('Ch 01 · Principles of Glomerulopathies', 'Causes — I: Primary &amp; Secondary (Infections, Multisystem)')}
{body(112, 60)}
{card('<b style="color:#8E3B2B;">Primary = Unknown causes = Idiopathic.</b>', title='I. Primary', title_fs=16, accent='burg')}
<div style="margin-top:10px;">{card('', title='II. Secondary', title_fs=16)}</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:10px;">
  <div style="background:#FBF3E4;border:1px solid #E2CFAD;border-left:5px solid #7A5233;border-radius:10px;padding:11px 14px;">
    <p style="font-size:15px;font-weight:700;color:#4A2F16;margin:0 0 5px 0;">1. Infections (post-infectious)</p>
    <ul style="margin:0;padding-left:17px;font-size:12.5px;color:#3A2A18;line-height:1.5;">
      <li><b style="color:#B0722F;">Bacterial:</b><br>
        <span style="padding-left:10px;">– <b style="color:#8E3B2B;">Streptococcal:</b> B-hemolytic (types 1, 4, 12, 49) → post-streptococcal GN<br>
        – Non-streptococcal: Staphylococci, Gonococci, Salmonella, Meningococcal, Secondary syphilis, Leprosy</span></li>
      <li><b style="color:#B0722F;">Virus:</b> HBV, HCV, HIV, EBV (infectious mononucleosis), Mumps, Measles, Coxsackie, Varicella</li>
      <li><b style="color:#B0722F;">Parasite:</b> Malaria, Schistosomiasis, Filariasis, Toxoplasmosis</li>
    </ul>
  </div>
  <div style="background:#FBF3E4;border:1px solid #E2CFAD;border-left:5px solid #7A5233;border-radius:10px;padding:11px 14px;">
    <p style="font-size:15px;font-weight:700;color:#4A2F16;margin:0 0 5px 0;">2. Multisystem diseases</p>
    <ul style="margin:0;padding-left:17px;font-size:12.5px;color:#3A2A18;line-height:1.55;">
      <li>SLE</li><li>Rheumatoid Arthritis</li><li>Dermatomyositis</li><li>Sjögren&rsquo;s syndrome</li>
      <li>Goodpasture&rsquo;s syndrome</li>
      <li>Vasculitis: <b>PAN</b>, Wegener&rsquo;s granulomatosis, Henoch-Schönlein purpura</li>
    </ul>
  </div>
</div>
</div>'''
add(s5, 5, foot='PRINCIPLES OF NEPHROLOGY — Page 1–2')

# ------------------------------------------------------------
# 6 — CH1 · Causes II
# ------------------------------------------------------------
items6 = [
    ('3. Malignant diseases &amp; Paraproteinemias', ['Carcinoma (lung, colon, melanoma)', 'Hematological malignancy: Lymphomas (HL, non-HL) and Leukemias', 'Paraproteinemias: MM, Amyloidosis, WM, Cryoglobulinemia']),
    ('4. Drugs &amp; Toxins', ['Penicillin', 'Heavy metals (Mercury, Gold)', 'Heroin', 'Captopril', 'Antivenom, Antitoxins', 'Contrast media']),
    ('5. Metabolic', ['Diabetes mellitus', 'Gout']),
    ('6. Heredofamilial', ['Thin basement membrane disease', "Alport's syndrome", "Fabry's disease", 'Nail-Patella syndrome', 'Sickle cell disease']),
    ('7. Others', ['Sarcoidosis', 'Pre-eclampsia', 'Thyrotoxicosis &amp; Myxedema', 'Serum Sickness', 'Chronic graft rejection', 'Allergic: bee stings, pollens, cow milk']),
]
c6 = ''
for t, its in items6:
    if t.startswith('7.'):
        inline = ' &nbsp;·&nbsp; '.join(its)
        c6 += f'''<div style="grid-column:1 / -1;background:#FBF3E4;border:1px solid #E2CFAD;border-left:5px solid #7A5233;border-radius:10px;padding:8px 13px;">
  <p style="font-size:13.5px;font-weight:700;color:#4A2F16;margin:0 0 3px 0;">{t}</p>
  <p style="font-size:11.5px;color:#3A2A18;margin:0;line-height:1.45;">{inline}</p>
</div>'''
    else:
        lis = ''.join(f'<li>{i}</li>' for i in its)
        c6 += f'''<div style="background:#FBF3E4;border:1px solid #E2CFAD;border-left:5px solid #7A5233;border-radius:10px;padding:9px 12px;">
  <p style="font-size:13.5px;font-weight:700;color:#4A2F16;margin:0 0 3px 0;">{t}</p>
  <ul style="margin:0;padding-left:16px;font-size:12px;color:#3A2A18;line-height:1.45;">{lis}</ul>
</div>'''
s6 = f'''{top_band('Ch 01 · Principles of Glomerulopathies', 'Causes — II: Secondary GN (continued)')}
{body(112, 60)}
{grid('1fr 1fr', 12)}{c6}</div>
</div>'''
add(s6, 6, foot='PRINCIPLES OF NEPHROLOGY — Page 2')

# ------------------------------------------------------------
# 7 — CH1 · Pathology (Macroscopic + Microscopic)
# ------------------------------------------------------------
s7 = f'''{top_band('Ch 01 · Principles of Glomerulopathies', 'Pathology')}
{body(112, 60)}
{card('<b>Macroscopic:</b> of no value (can be evaluated by Ultrasound).', title='Macroscopic examination', title_fs=15)}
<div style="margin-top:10px;">
{tbl(['', 'In acute GN', 'In chronic GN'], [
    ['<b>Size of kidney</b>', 'Normal or increased', 'Normal or decreased'],
    ['<b>Surface of kidney</b>', 'Punctate hemorrhage', 'Fine granular or cortical scars'],
], widths=[32, 34, 34], fs=13)}
</div>
<div style="margin-top:12px;">{card('Renal biopsy is the definitive tool — each modality answers a different question.', title='Microscopic: Renal biopsy', title_fs=15)}</div>
<div style="margin-top:10px;">
{tbl(['Method', 'Value'], [
    ['<b>LM</b> (light microscopy)', 'The histopathological type / The severity &amp; degree of disease'],
    ['<b>EM</b> (electron microscopy)', 'Define site of immune deposition: subendothelial, subepithelial, mesangial'],
    ['<b>IF</b> (immunofluorescence)', 'The type of immune deposition e.g. IgA, C3, C4.<br><b>IC GN</b> → deposits appear <b>diffuse granular</b> pattern.<br><b>Anti-GBM Ab</b> → deposits appear <b>smooth linear</b> pattern.'],
], widths=[16, 84], fs=12.5)}
</div>
</div>'''
add(s7, 7)

# ------------------------------------------------------------
# 8 — CH1 · Histopathological Types
# ------------------------------------------------------------
s8 = f'''{top_band('Ch 01 · Principles of Glomerulopathies', 'The Histopathological Types')}
{body(112, 58)}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  <div style="background:#FBF3E4;border:1px solid #E2CFAD;border-left:5px solid #7A5233;border-radius:10px;padding:11px 14px;">
    <p style="font-size:15px;font-weight:700;color:#4A2F16;margin:0 0 5px 0;">1. Minimal lesion GN <span style="font-size:12px;color:#B0722F;">(Minimal Change Disease — MCD)</span></p>
    <ul style="margin:0;padding-left:17px;font-size:12.5px;color:#3A2A18;line-height:1.5;">
      <li><b style="color:#B0722F;">LM:</b> Normal or mild increase in mesangial cells</li>
      <li><b style="color:#B0722F;">EM:</b> Fusion of foot processes of epithelial cells (podocytes)</li>
      <li><b style="color:#B0722F;">IF:</b> No deposits</li>
    </ul>
  </div>
  <div style="background:#FBF3E4;border:1px solid #E2CFAD;border-left:5px solid #7A5233;border-radius:10px;padding:11px 14px;">
    <p style="font-size:15px;font-weight:700;color:#4A2F16;margin:0 0 5px 0;">2. Membranous GN (MGN)</p>
    <p style="font-size:12.5px;color:#3A2A18;margin:0;line-height:1.5;"><b style="color:#B0722F;">LM:</b> Diffuse thickening of glomerular basement membrane.</p>
  </div>
  <div style="background:#FBF3E4;border:1px solid #E2CFAD;border-left:5px solid #A86E1C;border-radius:10px;padding:11px 14px;">
    <p style="font-size:15px;font-weight:700;color:#4A2F16;margin:0 0 5px 0;">3. Proliferative GN</p>
    <p style="font-size:12.5px;color:#3A2A18;margin:0 0 3px 0;"><b style="color:#B0722F;">• Diffuse proliferative:</b> proliferation of all glomerular cells (endothelial, epithelial &amp; mesangial)</p>
    <ul style="margin:0;padding-left:17px;font-size:12px;color:#3A2A18;line-height:1.45;">
      <li>a) Acute diffuse proliferative GN</li>
      <li>b) Diffuse proliferation with crescents (Crescentic GN, RPGN)</li>
      <li>c) Mesangio-proliferative (MPGN): increased mesangial cells &amp; matrix</li>
      <li>d) Mesangio-capillary GN (MCGN): proliferation of mesangial cells &amp; matrix + thickening of glomerular BM</li>
    </ul>
    <p style="font-size:12.5px;color:#3A2A18;margin:4px 0 0 0;"><b style="color:#B0722F;">• Focal proliferative:</b></p>
    <ul style="margin:0;padding-left:17px;font-size:12px;color:#3A2A18;line-height:1.45;">
      <li>a) Focal segmental GN (FSGN): cellular proliferation of some segments in some glomeruli</li>
    </ul>
  </div>
  <div style="background:#FBF3E4;border:1px solid #E2CFAD;border-left:5px solid #8E3B2B;border-radius:10px;padding:11px 14px;">
    <p style="font-size:15px;font-weight:700;color:#4A2F16;margin:0 0 5px 0;">4. Focal segmental glomerulo-sclerosis (FSGS)</p>
    <p style="font-size:12.5px;color:#3A2A18;margin:0;line-height:1.5;">Sclerosis of some segments in some glomeruli.</p>
    <p style="font-size:12px;color:#8E3B2B;margin:8px 0 0 0;"><b>Contrast:</b> FSGS = <i>sclerosis</i> (scarring) vs FSGN = <i>cellular proliferation</i> of segments.</p>
  </div>
</div>
</div>'''
add(s8, 8, foot='PRINCIPLES OF NEPHROLOGY — Page 3')

# ------------------------------------------------------------
# 9 — CH1 · Clinical Presentations (5 syndromes)
# ------------------------------------------------------------
syn = [
    ('Acute GN (acute nephritic syndrome)', 'Relatively abrupt', 'Hematuria, Proteinuria, Oliguria, Edema, Hypertension', 'DPGN', 'Spontaneous resolution', ''),
    ('Nephrotic syndrome', 'Variable', 'Albumin &lt; 2.5 g/dl, Proteinuria ≥ 3+, Hyperlipidemia, Edema, Hypertension (MCGN)', 'Variable lesions', 'Variable', 'Variable onset, pathology &amp; course'),
    ('Chronic GN', 'Insidious / progressive', 'Proteinuria 0/1+, Hypertension, Urinary sediments +, Slow progressive decline in GFR', 'Glomerulosclerosis, chronic interstitial fibrosis', 'Progress to renal failure', 'The common pathway to ESRD'),
    ('Rapidly Progressive GN (RPGN)', 'Rapid decline in GFR', 'Hematuria, Proteinuria, Oliguria, Absent or mild hypertension', 'DPGN with crescents', 'Rapidly progresses to AKI', 'Renal emergency — intensive therapy'),
    ('Asymptomatic proteinuria ± hematuria', 'Insidious', 'Hematuria / proteinuria, Hypertension +/–, Normal GFR', 'FSGN', 'Persists or recurs', 'Accidentally discovered, relatively benign'),
]
cards9 = ''
for name, onset, feat, path, course, nts in syn:
    cards9 += f'''<div style="background:#FBF3E4;border:1px solid #E2CFAD;border-left:5px solid #7A5233;border-radius:10px;padding:9px 12px;">
  <p style="font-size:13.5px;font-weight:700;color:#4A2F16;margin:0 0 4px 0;">{name}</p>
  <p style="font-size:11.5px;color:#3A2A18;margin:0;line-height:1.42;">
    <b style="color:#B0722F;">Onset:</b> {onset}<br>
    <b style="color:#B0722F;">Features:</b> {feat}<br>
    <b style="color:#B0722F;">Pathology:</b> {path}<br>
    <b style="color:#B0722F;">Course:</b> {course}<br>
    {('<b style="color:#B0722F;">Notes:</b> ' + nts) if nts else ''}
  </p>
</div>'''
s9 = f'''{top_band('Ch 01 · Principles of Glomerulopathies', 'Clinical Presentations — The 5 Major Syndromes')}
{body(112, 60)}
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;">{cards9}</div>
<div style="margin-top:10px;">{imp('Every glomerulopathy presents as one (or more) of these 5 clinical syndromes: acute GN, nephrotic syndrome, chronic GN, RPGN, or asymptomatic proteinuria ± hematuria.', 'Key')}</div>
</div>'''
add(s9, 9, foot='PRINCIPLES OF NEPHROLOGY — Page 3–4')

# ------------------------------------------------------------
# 10 — CH1 · Investigations
# ------------------------------------------------------------
s10 = f'''{top_band('Ch 01 · Principles of Glomerulopathies', 'Investigations — I (Urine, Blood, Imaging, Biopsy)')}
{body(112, 60)}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card(ul(['Volume in 24 hours: may be decreased or normal', '24-hour urinary protein or urinary protein/creatinine ratio', 'Microscopic examination of urinary sediment:', '<span style="padding-left:10px;">– Red cells → may or may not be present</span>', '<span style="padding-left:10px;">– <b style="color:#8E3B2B;">Dysmorphic red cells</b> → strongly suggestive of GN</span>', '<span style="padding-left:10px;">– Casts → granular &amp; <b style="color:#8E3B2B;">red cell casts</b> (diagnostic of acute GN)</span>'], fs=12.5), title='1. Urine Examination', title_fs=16, pad='12px 14px')}
  {card(ul(['Blood urea', 'Serum creatinine', 'Serum electrolytes (Ca, PO4, K+, Na+)', 'Assessment of GFR (normal = 90–120 ml/min)'], fs=13), title='2. Blood Examination', title_fs=16, pad='12px 14px')}
  {card('<b>Ultrasound</b> (to exclude other renal pathology):<br><span style="padding-left:8px;">– Smooth renal outline</span><br><span style="padding-left:8px;">– Normal pelvicalyceal system and lower urinary tract</span>', title='3. Renal Imaging', title_fs=16, fs=13, pad='12px 14px')}
  {card(ul(['Accurate histopathological diagnosis', 'Assess severity &amp; response to treatment', 'Prognosis'], fs=13), title='4. Renal Biopsy — needed for:', title_fs=16, pad='12px 14px')}
</div>
<div style="margin-top:14px;">{imp('Renal biopsy gives the <b>histopathological diagnosis</b>, assesses <b>severity &amp; response to treatment</b>, and predicts <b>prognosis</b>.', 'Note')}</div>
</div>'''
add(s10, 10, foot='PRINCIPLES OF NEPHROLOGY — Page 4–5')

s10b = f'''{top_band('Ch 01 · Principles of Glomerulopathies', 'Investigations — II: Specific Investigations (determination of the cause)')}
{body(112, 60)}
{tbl(['Disease / cause', 'Specific investigation'], [
    ['Diabetes mellitus', 'Blood glucose'],
    ['Recent streptococcal infection', 'ASOT and throat or skin swab'],
    ['Systemic disease, e.g. SLE', 'ANA &amp; anti-ds DNA'],
    ["Goodpasture's disease", 'Anti-GBM antibody'],
    ["IgA nephropathy (Berger's disease)", 'Serum IgA antibody'],
], fs=13)}
<div style="margin-top:12px;">{card('<b style="color:#8E3B2B;">Serum complement is decreased in:</b><br><span style="padding-left:8px;">a) <b>Post-infection</b> — acute post-streptococcal GN (transient, 8 weeks), infective endocarditis, and shunt nephropathy</span><br><span style="padding-left:8px;">b) <b>SLE</b></span><br><span style="padding-left:8px;">c) <b>Cryoglobulinemia</b></span><br><span style="padding-left:8px;">d) <b>Serum sickness</b></span>', title='Low complement states', title_fs=15, fs=12.5, accent='terra')}</div>
</div>'''
add(s10b, 11, foot='PRINCIPLES OF NEPHROLOGY — Page 4–5')

# ------------------------------------------------------------
# 11 — CH1 · Treatment I (General)
# ------------------------------------------------------------
s11 = f'''{top_band('Ch 01 · Principles of Glomerulopathies', 'Principles of Treatment — I: General Measures')}
{body(108, 40)}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;">
  {card(ul(['Control of symptoms', 'Prevent complications', 'Slow progression of the disease'], fs=11), title='Aims of general treatment', title_fs=13.5, accent='burg', pad='8px 11px', lh=1.35)}
  {card('<b>Salt &amp; water restriction</b> for edematous and/or hypertensive patients, especially with oliguria.<br><br><b>Protein intake — remember:</b><br><span style="padding-left:8px;">– High protein intake → increases proteinuria in renal failure patients and causes nephron damage → <b style="color:#8E3B2B;">progression of renal disease</b>.</span><br><span style="padding-left:8px;">– Low protein intake → negative nitrogen balance and malnutrition.</span><br><br><b>Therefore:</b><br><span style="padding-left:8px;">• Normal GFR → physiological needs (1 mg/kg/day) + daily urinary protein loss</span><br><span style="padding-left:8px;">• ↓ GFR → moderate protein restriction (0.6–0.8 gm/kg/day) to control anorexia, nausea, vomiting</span>', title='Diet', title_fs=13.5, fs=10.8, pad='8px 11px', lh=1.35)}
  {card(ul(['Bed rest', 'Salt restriction (&lt; 2 gm/day) &amp; fluid restriction', 'Diuretics — preferably <b style="color:#8E3B2B;">loop diuretics</b>; thiazides can be combined', 'Salt-poor albumin (in resistant cases with hypoalbuminemia)', 'Ultrafiltration', 'Hemodialysis'], fs=10.8, gap='2px'), title='Control of Edema', title_fs=13.5, pad='8px 11px', lh=1.35)}
  {card('1. Avoid high-protein diet (0.8–1 gm/day + estimated daily loss)<br>2. Use of <b style="color:#8E3B2B;">ACEIs &amp; ARBs</b>:<br><span style="padding-left:8px;">Both compete with the vasoconstrictor (VC) effect of angiotensin II on the <b>efferent arterioles</b> → efferent arteriole vasodilation → decrease intraglomerular pressure → decrease GFR → decrease glomerular filtered protein → <b>decrease proteinuria</b>.</span><br><br><b style="color:#5F6B2E;">NB:</b> ACEIs are used in small doses in normotensive patients, and used cautiously in renal failure and in hyperkalemic patients.', title='Control of Proteinuria', title_fs=13.5, fs=10.8, pad='8px 11px', lh=1.35)}
</div>
</div>'''
add(s11, 11, foot='PRINCIPLES OF NEPHROLOGY — Page 5')

# ------------------------------------------------------------
# 12 — CH1 · Treatment II (HTN, Lipids, Hypercoagulability)
# ------------------------------------------------------------
s12 = f'''{top_band('Ch 01 · Principles of Glomerulopathies', 'Principles of Treatment — II: Hypertension, Lipids, Thrombosis')}
{body(112, 58)}
<div style="display:grid;grid-template-columns:3fr 2fr;gap:12px;">
  <div style="background:#FBF3E4;border:1px solid #E2CFAD;border-left:5px solid #8E3B2B;border-radius:10px;padding:11px 14px;">
    <p style="font-size:15px;font-weight:700;color:#4A2F16;margin:0 0 5px 0;">Control of Hypertension</p>
    <p style="font-size:12.5px;color:#3A2A18;margin:0 0 3px 0;"><b style="color:#B0722F;">Value of BP control:</b></p>
    <ul style="margin:0;padding-left:17px;font-size:12px;color:#3A2A18;line-height:1.45;">
      <li>Relief of symptoms</li>
      <li>Prevent hypertensive complications on other systems</li>
      <li>Decrease progression of renal disease (renoprotective)</li>
    </ul>
    <p style="font-size:12.5px;color:#3A2A18;margin:6px 0 3px 0;"><b style="color:#B0722F;">Target BP — according to degree of proteinuria:</b></p>
    <ul style="margin:0;padding-left:17px;font-size:12px;color:#3A2A18;line-height:1.45;">
      <li>If proteinuria <b style="color:#8E3B2B;">&gt; 1 gm/day</b> → target BP <b style="color:#8E3B2B;">&lt; 125/75</b> (mean BP &lt; 92)</li>
      <li>If proteinuria <b style="color:#8E3B2B;">&lt; 1 gm/day</b> → target BP <b style="color:#8E3B2B;">&lt; 130/80</b> (mean BP &lt; 98)</li>
    </ul>
    <p style="font-size:12.5px;color:#3A2A18;margin:6px 0 3px 0;"><b style="color:#B0722F;">Choice of antihypertensive agent:</b></p>
    <ul style="margin:0;padding-left:17px;font-size:12px;color:#3A2A18;line-height:1.45;">
      <li>ACEIs / ARBs</li>
      <li>Calcium-channel blockers (CCB)</li>
      <li>All have <b style="color:#8E3B2B;">renoprotective effect</b></li>
    </ul>
  </div>
  <div style="display:flex;flex-direction:column;gap:12px;">
    {card(ul(['Avoid high-fat diet', 'Physical activity', 'Use statins'], fs=12), title='Control of Hyperlipidemia', title_fs=15, accent='olive')}
    {card('<b>Prophylactic anticoagulation</b> should be employed in nephrotic syndrome patients at high risk of thromboembolism:<br><br><span style="padding-left:8px;">• Increased risk of <b style="color:#8E3B2B;">venous thrombosis</b> (albumin &lt; 2.5) → <b style="color:#8E3B2B;">anticoagulants</b></span><br><span style="padding-left:8px;">• Increased risk of <b style="color:#8E3B2B;">arterial thrombosis</b> → <b style="color:#8E3B2B;">aspirin</b></span>', title='Control of Hypercoagulability &amp; Thrombosis', title_fs=15, fs=12, accent='terra')}
  </div>
</div>
</div>'''
add(s12, 12, foot='PRINCIPLES OF NEPHROLOGY — Page 5–6')

# ------------------------------------------------------------
# 13 — CH1 · Specific Treatment + Course
# ------------------------------------------------------------
s13 = f'''{top_band('Ch 01 · Principles of Glomerulopathies', 'Specific Treatment &amp; Course')}
{body(112, 58)}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card(ul(['Immunosuppressive + Cytotoxic drugs', 'Other measures, e.g. <b style="color:#8E3B2B;">plasma exchange</b>'], fs=12.5), title='In Primary GN', title_fs=15)}
  {card('Treatment of the cause, e.g.: control of infection, treat malignancy, stop toxins &amp; drugs, control of disease activity (SLE, DM, Gout).', title='In Secondary GN', title_fs=15, fs=12.5)}
</div>
<div style="margin-top:12px;">{card('', title='Course — variable depending on renal pathology &amp; etiology', title_fs=15)}</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:10px;">
  <div style="background:rgba(142,59,43,0.09);border:1.5px solid #8E3B2B;border-radius:10px;padding:9px 13px;">
    <p style="font-size:12px;color:#3A2A18;margin:0;line-height:1.45;"><b style="color:#8E3B2B;">Anti-GBM &amp; ANCA-associated crescentic GN</b> → rapid progression to <b style="color:#8E3B2B;">ESRD unless treated</b>.</p>
    <p style="font-size:12px;color:#3A2A18;margin:7px 0 0 0;line-height:1.45;"><b style="color:#8E3B2B;">IgA nephropathy &amp; FSGS</b> → indolent but persistent course → renal failure.</p>
  </div>
  <div style="background:rgba(95,107,46,0.10);border:1px solid #5F6B2E;border-left:5px solid #5F6B2E;border-radius:10px;padding:9px 13px;">
    <p style="font-size:12px;color:#3A2A18;margin:0;line-height:1.45;"><b style="color:#5F6B2E;">Post-streptococcal GN</b> → tends to <b style="color:#5F6B2E;">resolve completely</b> with little risk of progression to ESRD.</p>
    <p style="font-size:12px;color:#3A2A18;margin:7px 0 0 0;line-height:1.45;"><b style="color:#5F6B2E;">MGN</b> → unpredictable: may remit spontaneously, persist / relapse, or progress over years to ESRD.</p>
  </div>
</div>
</div>'''
add(s13, 13, foot='PRINCIPLES OF NEPHROLOGY — Page 6')

# ------------------------------------------------------------
# 14 — DIVIDER 02
# ------------------------------------------------------------
divider('02', 'Acute Glomerulonephritis — Nephritic Syndrome', 'Definition · Clinical Features · Investigations · Treatment', 'Page 7–10')

# ------------------------------------------------------------
# 15 — CH2 · Definition
# ------------------------------------------------------------
s15 = f'''{top_band('Ch 02 · Acute GN (Nephritic Syndrome)', 'Definition')}
{body(112, 62)}
{card('Acute GN is a clinical syndrome characterized by <b style="color:#8E3B2B;">acute onset</b> of:', title='Definition', title_fs=17)}
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;margin-top:12px;">
  {card('<b>1. Hematuria</b><br><span style="font-size:11.5px;color:#6B5238;">Macroscopic or microscopic</span>', title_fs=16, fs=13, accent='burg')}
  {card('<b>2. Proteinuria</b><br><span style="font-size:11.5px;color:#6B5238;">&lt; 3.5 gm/d/1.73 m² body surface area</span>', title_fs=16, fs=13)}
  {card('<b>3. Hypertension</b>', title_fs=16, fs=13)}
  {card('<b>4. Edema</b>', title_fs=16, fs=13)}
  {card('<b>5. Oliguria</b><br><span style="font-size:11.5px;color:#6B5238;">&lt; 300 ml/day in severe cases</span>', title_fs=16, fs=13)}
  {card('<b style="color:#B0722F;">Nephritic vs Nephrotic</b><br><span style="font-size:11.5px;">Proteinuria is <b>non-nephrotic range</b> (&lt; 3.5 gm/day) in acute GN.</span>', title_fs=16, fs=12.5, accent='gold', bg='rgba(168,110,28,0.10)')}
</div>
<div style="margin-top:12px;">{imp('The <b>nephritic syndrome</b> (acute GN) is dominated by <b>hematuria</b>, whereas the <b>nephrotic syndrome</b> is dominated by heavy proteinuria ≥ 3.5 gm/day.', 'Contrast')}</div>
</div>'''
add(s15, 15, foot='PRINCIPLES OF NEPHROLOGY — Page 7')

# ------------------------------------------------------------
# 16 — CH2 · Clinical Features A: Hematuria + Proteinuria
# ------------------------------------------------------------
s16 = f'''{top_band('Ch 02 · Acute GN (Nephritic Syndrome)', 'Clinical Features — A. Manifestations of Acute Nephritis')}
{body(112, 60)}
{card('<b style="color:#8E3B2B;">1. Hematuria</b> — due to damage of the glomerular capillary walls. It may be:', title='Hematuria', title_fs=16)}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:10px;">
  <div style="background:#FBF3E4;border:1px solid #E2CFAD;border-top:4px solid #B0722F;border-radius:10px;padding:10px 13px;">
    <p style="font-size:14px;font-weight:700;color:#4A2F16;margin:0 0 4px 0;">Macroscopic hematuria</p>
    <p style="font-size:12px;color:#3A2A18;margin:0;line-height:1.5;">Color of urine depends on pH:<br><span style="padding-left:8px;">• <b style="color:#8E3B2B;">Red</b> urine → in alkaline urine</span><br><span style="padding-left:8px;">• <b style="color:#8E3B2B;">Smoky (or reddish brown)</b> urine → in acidic urine, due to denaturation of hemoglobin with formation of <b>acid haematine</b> and prolonged transit time through the nephron</span><br><span style="padding-left:8px;">• Formation of <b>methemoglobin</b> gives the smoky color of urine</span></p>
  </div>
  <div style="background:#FBF3E4;border:1px solid #E2CFAD;border-top:4px solid #7A5233;border-radius:10px;padding:10px 13px;">
    <p style="font-size:14px;font-weight:700;color:#4A2F16;margin:0 0 4px 0;">Microscopic hematuria</p>
    <p style="font-size:12px;color:#3A2A18;margin:0;line-height:1.5;">Characterized by the presence of <b style="color:#8E3B2B;">dysmorphic red cells</b>:<br><span style="padding-left:8px;">• Small &amp; distorted — due to <b>mechanical injury</b> of RBCs passing through the damaged glomerular capillary walls</span><br><span style="padding-left:8px;">• Have low hemoglobin content</span><br><span style="padding-left:8px;">• Best seen by <b>phase contrast microscopy</b></span></p>
  </div>
</div>
<div style="margin-top:10px;">{card('<b style="color:#8E3B2B;">2. Proteinuria</b> — glomerular origin (consists mainly of albumin); non-nephrotic range (&lt; 3.5 gm/day).<br><b>Due to:</b><br><span style="padding-left:8px;">• Increase of glomerular capillary permeability</span><br><span style="padding-left:8px;">• Mechanical disruption of glomerular capillary walls</span><br><span style="padding-left:8px;">• Altered glomerular hemodynamics</span>', title='Proteinuria', title_fs=16, fs=12.5)}</div>
</div>'''
add(s16, 16, foot='PRINCIPLES OF NEPHROLOGY — Page 7–8')

# ------------------------------------------------------------
# 17 — CH2 · Clinical Features A2 + B
# ------------------------------------------------------------
s17 = f'''{top_band('Ch 02 · Acute GN (Nephritic Syndrome)', 'Clinical Features — Edema, Hypertension, Oliguria &amp; Associated Disease')}
{body(112, 58)}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card('• <b>Early</b> → eyelids (puffiness) — as this area is of <b>low tissue pressure</b><br>• Then progresses to involve the legs and other parts<br><br><b>Due to salt and water retention because of:</b><br><span style="padding-left:8px;">– Increase reabsorption of filtered Na<sup>+</sup> at the distal tubules</span><br><span style="padding-left:8px;">– Decrease GFR → decrease salt delivery to tubules</span>', title='3. Edema', title_fs=15, fs=12.5)}
  {card('<b>Due to salt &amp; water retention</b>, i.e. <b style="color:#8E3B2B;">volume-dependent</b> hypertension.', title='4. Hypertension', title_fs=15, fs=13)}
  {card('Urine output <b style="color:#8E3B2B;">&lt; 300 ml/day</b>.<br><br><b>Due to decreased GFR.</b>', title='5. Oliguria', title_fs=15, fs=13)}
  {card('Manifestations of the associated specific disease, e.g.:<br><span style="padding-left:8px;">• <b>Infection</b> (PSGN)</span><br><span style="padding-left:8px;">• <b>SLE</b></span><br><span style="padding-left:8px;">• <b>Vasculitis</b></span><br><span style="padding-left:8px;">• <b>Malignancy</b></span>', title='B. Manifestations of the Associated Specific Disease', title_fs=15, fs=12.5, accent='olive')}
</div>
</div>'''
add(s17, 17, foot='PRINCIPLES OF NEPHROLOGY — Page 8')

# ------------------------------------------------------------
# 18 — CH2 · Investigations
# ------------------------------------------------------------
s18 = f'''{top_band('Ch 02 · Acute GN (Nephritic Syndrome)', 'Investigations')}
{body(112, 58)}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card(ul(['Color → red or smoky (dark brown)', 'Oliguria: &lt; 300 ml/day in severe cases', 'Proteinuria &lt; 3.5 gm/day', 'Microscopic examination:', '<span style="padding-left:10px;">– Hematuria</span>', '<span style="padding-left:10px;">– <b style="color:#8E3B2B;">Dysmorphic red cells &amp; red cell casts</b> — both are pathognomonic for acute GN</span>', '<span style="padding-left:10px;">– Granular casts</span>'], fs=12), title='1. Urine Examination', title_fs=15)}
  {card('<b>2. Blood:</b> (Urea, Creatinine &amp; GFR) — variable impairment of renal function.<br><br><b>3. Renal imaging:</b> usually unnecessary.', title='Blood &amp; Imaging', title_fs=15, fs=12.5)}
  {card('Most of the renal pathology associated with acute GN is <b style="color:#8E3B2B;">proliferative</b>, either focal or diffuse.<br><br><b>Indications for renal biopsy:</b><br><span style="padding-left:8px;">A. Unusual clinical features</span><br><span style="padding-left:8px;">B. Uncertain diagnosis</span><br><span style="padding-left:8px;">C. Rapid deterioration of renal function → <b style="color:#8E3B2B;">crescentic GN</b></span>', title='4. Renal Biopsy', title_fs=15, fs=12.5)}
  {card('<b>Needed for etiological diagnosis, e.g.:</b><br><span style="padding-left:8px;">• <b>ANA, ds DNA</b> → SLE</span><br><span style="padding-left:8px;">• <b>Throat swab &amp; ASOT</b> and <b style="color:#8E3B2B;">transient decrease of C3 (&lt; 8 weeks)</b> → PSGN</span>', title='5. Specific Investigations', title_fs=15, fs=12.5, accent='olive')}
</div>
</div>'''
add(s18, 18, foot='PRINCIPLES OF NEPHROLOGY — Page 8–9')

# ------------------------------------------------------------
# 19 — CH2 · Treatment — General
# ------------------------------------------------------------
s19 = f'''{top_band('Ch 02 · Acute GN (Nephritic Syndrome)', 'Treatment — 1. General Measures')}
{body(112, 56)}
{card('<b>To control symptoms and prevent complications.</b>', title='General treatment', title_fs=15)}
<div style="margin-top:8px;">
{tbl(['Home treatment', 'Hospital admission'], [
    ['For uncomplicated cases', 'For complicated cases: severe hypertension, renal failure &amp; oliguria, pulmonary edema, encephalopathy'],
    ['Daily follow-up of blood pressure', 'Until hematuria, HTN &amp; edema disappear, and proteinuria decreases'],
    ['Urea and creatinine every few days', 'Strict bed rest in complicated cases (e.g. severe hypertension, pulmonary edema)'],
], fs=12)}
</div>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;margin-top:10px;">
  {card('<b>Salt restriction</b>', title_fs=14, fs=12.5)}
  {card('<b>Fluid restriction</b> in oliguric patients: <b style="color:#8E3B2B;">1/2 L + volume of previous day urine</b>', title_fs=14, fs=12.5)}
  {card('<b>Protein restriction</b> in renal failure: <b style="color:#8E3B2B;">0.6–0.8 gm/kg/day</b> (≈ 40 gm/day for an adult patient)', title_fs=14, fs=12.5)}
</div>
<div style="margin-top:10px;">{note('Fluid chart (fluid intake and output) and measurement of body weight and blood pressure are part of daily monitoring.', 'Monitoring')}</div>
</div>'''
add(s19, 19, foot='PRINCIPLES OF NEPHROLOGY — Page 9')

# ------------------------------------------------------------
# 20 — CH2 · Treatment — HTN/Edema, Encephalopathy, Pulmonary Edema, Specific
# ------------------------------------------------------------
s20 = f'''{top_band('Ch 02 · Acute GN (Nephritic Syndrome)', 'Treatment — Hypertension, Emergencies &amp; Specific Therapy')}
{body(112, 56)}
{card('• Salt restriction<br>• Diuretics: <b style="color:#8E3B2B;">loop diuretics</b><br>• Antihypertensive drugs — <b style="color:#B5522E;">β-blockers should be used with caution</b>, as they may precipitate pulmonary edema in patients with impending heart failure.', title='e.g. Hypertension &amp; Edema', title_fs=15, fs=12.5)}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:10px;">
  {card(ul(['Maintain airway', 'Control blood pressure by parenteral agent, such as <b style="color:#8E3B2B;">hydralazine 5–20 mg infusion</b>', 'Control of fits: <b style="color:#8E3B2B;">IV diazepam (10 mg)</b>'], fs=12), title='A. Hypertensive Encephalopathy', title_fs=15, accent='terra')}
  {card(ul(['Salt and water restriction', 'Ultrafiltration (dialysis) to remove excess fluid in oliguric patient', 'Acute renal failure: dialysis'], fs=12), title='B. Pulmonary Edema / Heart Failure', title_fs=15, accent='terra')}
</div>
<div style="margin-top:10px;">
{tbl(['Primary GN', 'Secondary GN'], [
    ['Corticosteroid ± immunosuppressives depending on the histopathological type (see the appropriate section)', 'Treat the cause, e.g.: PSGN, diabetic nephropathy, Lupus nephritis (see appropriate section)'],
], widths=[50, 50], fs=12.5)}
</div>
</div>'''
add(s20, 20, foot='PRINCIPLES OF NEPHROLOGY — Page 9–10')

# ------------------------------------------------------------
# 21 — DIVIDER 03
# ------------------------------------------------------------
divider('03', 'Nephrotic Syndrome', 'Definition · Causes · Clinical Features · Investigations · Treatment', 'Page 10–13')

# ------------------------------------------------------------
# 22 — CH3 · Definition + Causes
# ------------------------------------------------------------
s22 = f'''{top_band('Ch 03 · Nephrotic Syndrome', 'Definition &amp; Causes')}
{body(112, 58)}
{card('N.S. is a clinical syndrome characterized by:', title='Definition', title_fs=17)}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:10px;">
  <div style="background:rgba(142,59,43,0.09);border:1.5px solid #8E3B2B;border-radius:10px;padding:10px 14px;">
    <p style="font-size:13.5px;color:#3A2A18;margin:0;line-height:1.5;"><b style="color:#8E3B2B;">1. Heavy proteinuria</b> ≥ 3.5 gm/d/1.73 m² body surface area, or urinary protein/creatinine ratio &gt; 3.5 in adults.</p>
  </div>
  <div style="background:rgba(142,59,43,0.09);border:1.5px solid #8E3B2B;border-radius:10px;padding:10px 14px;">
    <p style="font-size:13.5px;color:#3A2A18;margin:0;line-height:1.5;"><b style="color:#8E3B2B;">2. Hypoalbuminemia</b> ≤ 2.5 gm/dl</p>
  </div>
  <div style="background:rgba(142,59,43,0.09);border:1.5px solid #8E3B2B;border-radius:10px;padding:10px 14px;">
    <p style="font-size:13.5px;color:#3A2A18;margin:0;line-height:1.5;"><b style="color:#8E3B2B;">3. Edema</b></p>
  </div>
  <div style="background:rgba(142,59,43,0.09);border:1.5px solid #8E3B2B;border-radius:10px;padding:10px 14px;">
    <p style="font-size:13.5px;color:#3A2A18;margin:0;line-height:1.5;"><b style="color:#8E3B2B;">4. Hyperlipidemia</b> (hypercholesterolemia)</p>
  </div>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:12px;">
  {card('All causes of acute GN.<br><br><b style="color:#B0722F;">Primary:</b> MCD, MGN, MPGN, MCGN, or FSGN.<br><br><b style="color:#B0722F;">Secondary</b> to: infection, multisystem disease, malignancy, drugs, metabolic or familial causes.', title='Causes', title_fs=16, fs=12.5)}
  {imp('Nephrotic syndrome = <b>heavy proteinuria</b> (≥ 3.5 gm/day) with hypoalbuminemia, edema and hyperlipidemia — in contrast to nephritic syndrome where proteinuria is &lt; 3.5 gm/day and hematuria dominates.', 'Contrast')}
</div>
</div>'''
add(s22, 22, foot='PRINCIPLES OF NEPHROLOGY — Page 10')

# ------------------------------------------------------------
# 23 — CH3 · Clinical Features
# ------------------------------------------------------------
s23 = f'''{top_band('Ch 03 · Nephrotic Syndrome', 'Clinical Features')}
{body(112, 58)}
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;">
  {card('<b style="color:#8E3B2B;">1. Proteinuria:</b> frothy urine — protein decreases the surface tension of urine, similar to bile salts and detergents.', title='Proteinuria', title_fs=15, fs=12.5)}
  {card('<b style="color:#8E3B2B;">2. Edema:</b> usually generalized — involves limbs, face, genitalia &amp; serous cavities (ascites, pleural &amp; pericardial effusion).<br><br><b>Severity</b> of edema correlates with serum albumin &amp; extent of urinary protein losses, and is conditioned by other factors such as heart failure.', title='Edema', title_fs=15, fs=12)}
  {card('<b style="color:#8E3B2B;">3. Hypertension:</b> variable, e.g.:<br><span style="padding-left:8px;">• In <b style="color:#8E3B2B;">MCD</b> → blood pressure is <b>always normal</b></span><br><span style="padding-left:8px;">• In <b style="color:#8E3B2B;">MCGN</b> → hypertension is <b>always present</b></span>', title='Hypertension', title_fs=15, fs=12.5)}
</div>
<div style="margin-top:10px;">{imp('Frothy urine + generalized edema + hyperlipidemia — think nephrotic syndrome. Remember the MCD vs MCGN blood-pressure contrast.', 'High-yield')}</div>
</div>'''
add(s23, 23, foot='PRINCIPLES OF NEPHROLOGY — Page 10–11')

# ------------------------------------------------------------
# 24 — CH3 · Investigations I (table)
# ------------------------------------------------------------
s24 = f'''{top_band('Ch 03 · Nephrotic Syndrome', 'Investigations — I')}
{body(112, 56)}
{tbl(['Investigation', 'Finding'], [
    ['<b>24-h urine protein</b>', '24-h urinary proteins (&gt; 3.5 gm/day in adults)'],
    ['<b>Plasma proteins</b>', 'Decreased serum albumin (≤ 2.5 gm/dl).<br><b>Serum protein electrophoresis:</b> decreased albumin; increased alpha2 &amp; beta globulin fractions; normal or slightly increased gamma globulin; increased fibrinogen.'],
    ['<b>Plasma lipids</b>', 'Increased cholesterol and LDL. Increased triglycerides in 50% of patients. Normal or decreased HDL (due to increased urinary loss).'],
    ['<b>Hypocalcemia</b>', 'Due to urinary loss of cholecalciferol-binding protein.'],
    ['<b>RFT</b>', 'Urea, creatinine &amp; eGFR are usually normal. Impaired in: severe hypovolemia → pre-renal AKI; MGN and MCGN.<br><b>NB:</b> in patients with impaired renal function, the biochemical features of NS are uncommon because of the concomitant decrease of GFR.'],
], widths=[20, 80], fs=12)}
</div>'''
add(s24, 24, foot='PRINCIPLES OF NEPHROLOGY — Page 11')

# ------------------------------------------------------------
# 25 — CH3 · Investigations II + Selective Proteinuria
# ------------------------------------------------------------
s25 = f'''{top_band('Ch 03 · Nephrotic Syndrome', 'Investigations — II &amp; Selective Proteinuria')}
{body(112, 56)}
{tbl(['Investigation', 'Finding'], [
    ['<b>Urine examination</b>', 'Red cells and red cell casts → GN (and exclude MCD).'],
    ['<b>PLA2R</b>', 'Phospholipase A2 Receptor (PLA2R) antibodies → primary membranous nephropathy (MN).'],
    ['<b>↓ Serum C3</b>', 'Decreased serum C3 → immune-complex-mediated GN.'],
    ['<b>ASOT &amp; swab</b>', 'ASOT &amp; throat swab → streptococcal infection.'],
    ['<b>ANA / ANCA</b>', 'ANA → SLE; ANCA → systemic vasculitis.'],
    ['<b>Hyperglycemia</b>', 'Hyperglycemia → diabetes mellitus.'],
], widths=[20, 80], fs=12)}
<div style="margin-top:8px;">{card('<b>Selective proteinuria</b> — tested in children. Blood + urine samples are examined simultaneously to determine the clearance of a large-molecular-weight protein (e.g. IgG) in comparison with a small-molecular-weight protein (e.g. albumin or transferrin).<br><br>• <b style="color:#5F6B2E;">Low ratio → selective</b> proteinuria in MCD, DM &amp; renal amyloidosis<br>• <b style="color:#8E3B2B;">High ratio → unselective</b> proteinuria in crescentic GN', title='Selective Proteinuria', title_fs=15, fs=12.5)}</div>
</div>'''
add(s25, 25, foot='PRINCIPLES OF NEPHROLOGY — Page 11')

# ------------------------------------------------------------
# 26 — CH3 · Renal Biopsy
# ------------------------------------------------------------
s26 = f'''{top_band('Ch 03 · Nephrotic Syndrome', 'Renal Biopsy — Indications &amp; Contraindications')}
{body(112, 58)}
{card('<b>Indications:</b> histological diagnosis and to plan therapy.', title='Renal biopsy', title_fs=16)}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:10px;">
  <div style="background:rgba(95,107,46,0.10);border:1px solid #5F6B2E;border-left:5px solid #5F6B2E;border-radius:10px;padding:10px 13px;">
    <p style="font-size:14px;font-weight:700;color:#4A2F16;margin:0 0 4px 0;">In children</p>
    <ul style="margin:0;padding-left:17px;font-size:12.5px;color:#3A2A18;line-height:1.5;">
      <li>Steroid-resistant, steroid-dependent and frequent relapses</li>
      <li>Children with renal impairment</li>
    </ul>
  </div>
  <div style="background:rgba(95,107,46,0.10);border:1px solid #5F6B2E;border-left:5px solid #5F6B2E;border-radius:10px;padding:10px 13px;">
    <p style="font-size:14px;font-weight:700;color:#4A2F16;margin:0 0 4px 0;">In adults</p>
    <p style="font-size:12.5px;color:#3A2A18;margin:0;line-height:1.5;">Most adults.</p>
  </div>
</div>
<div style="margin-top:10px;">{card('• <b style="color:#8E3B2B;">Young children</b> with selective proteinuria, normotensive &amp; benign urinary sediment → MCD<br>• <b style="color:#8E3B2B;">Long-standing DM</b> (&gt; 10 years in type 1, &gt; 5 years in type 2) with retinopathy or neuropathy<br>• <b style="color:#8E3B2B;">Patients under drug therapy</b> such as penicillamine', title='Biopsy NOT indicated in:', title_fs=15, fs=12.5, accent='terra')}</div>
</div>'''
add(s26, 26, foot='PRINCIPLES OF NEPHROLOGY — Page 11–12')

# ------------------------------------------------------------
# 27 — CH3 · Treatment General I
# ------------------------------------------------------------
s27 = f'''{top_band('Ch 03 · Nephrotic Syndrome', 'Treatment — 1. General Treatment')}
{body(112, 58)}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card('Daily physiological need (<b style="color:#8E3B2B;">1 gm/kg</b>) + the daily protein losses in urine.<br><br><b style="color:#8E3B2B;">N.B:</b> Protein restriction (0.6–0.8 gm/kg/day) in the presence of renal impairment.<br><br><b>High protein intake (1.5–2 gm/kg/day) is NOT advised because:</b><br><span style="padding-left:8px;">– Ineffective, due to increased protein loss</span><br><span style="padding-left:8px;">– Such a diet is difficult to manage with concomitant salt restriction</span><br><span style="padding-left:8px;">– Such a diet could aggravate glomerular damage</span>', title='Protein intake', title_fs=15, fs=12)}
  {card('• <b>ACE &amp; ARBs:</b> cause ↓ intraglomerular hydrostatic pressure → ↓ filtered urinary protein losses.<br>• <b style="color:#8E3B2B;">Medical nephrectomy</b> (mercurial drug or renal infarction) to abolish severe persistent proteinuria in ESRD.', title='Drug control of proteinuria', title_fs=15, fs=12.5)}
  {card(ul(['Bed rest → induces diuresis', 'Na<sup>+</sup> restriction', 'Diuretics in unresponsive patients', 'Human albumin infusion:', '<span style="padding-left:10px;">– <b>Indications:</b> severe hypoalbuminemia; diuretic-resistant patient undergoing surgery or an invasive procedure (biopsy)</span>', '<span style="padding-left:10px;">– <b>Disadvantages:</b> expensive &amp; transient effect (24–48 hours)</span>'], fs=12), title='Control of Edema', title_fs=15)}
  {card('<b style="color:#8E3B2B;">Contrast note:</b> unlike the general principles chapter, here the emphasis is on replacing losses (albumin) while restricting sodium — never use high-protein diets in nephrotic patients.', title='Rationale', title_fs=15, fs=12.5, accent='gold', bg='rgba(168,110,28,0.10)')}
</div>
</div>'''
add(s27, 27, foot='PRINCIPLES OF NEPHROLOGY — Page 12')

# ------------------------------------------------------------
# 28 — CH3 · Treatment General II + Specific
# ------------------------------------------------------------
s28 = f'''{top_band('Ch 03 · Nephrotic Syndrome', 'Treatment — Complications &amp; Specific Therapy')}
{body(112, 58)}
{card('', title='Control of complications', title_fs=15)}
<div style="margin-top:8px;">
{tbl(['Complication', 'Management'], [
    ['Subnutrition', 'Proper diet, minerals and vitamins.<br><b>N.B:</b> severe proteinuria may justify ablation of the kidneys by medical or surgical means.'],
    ['Sepsis', 'Early detection and aggressive treatment.'],
    ['Hyperlipidemia', 'Statins.'],
    ['Hypertension', 'Salt restriction + antihypertensives.'],
    ['Thrombotic complications', 'Long-term oral anticoagulant.<br><b>N.B:</b> Heparin is ineffective due to concomitant urinary loss of antithrombin III.<br><b>N.B:</b> prophylactic anticoagulant is used in NS due to membranous GN, as thromboembolic complications are common.'],
], widths=[28, 72], fs=12)}
</div>
<div style="margin-top:10px;">
{tbl(['In primary N.S.', 'In secondary N.S.'], [
    ['Depends on the histopathological types — such as MCD, MGN, MCGN, FSGN', 'Directed to the cause:<br>• SLE → Steroids + Cyclophosphamide<br>• DM → Control of hyperglycemia'],
], widths=[50, 50], fs=12.5)}
</div>
</div>'''
add(s28, 28, foot='PRINCIPLES OF NEPHROLOGY — Page 12–13')

# ------------------------------------------------------------
# 29 — DIVIDER 04
# ------------------------------------------------------------
divider('04', 'Anti-GBM Disease &amp; Goodpasture Syndrome', 'Definition · Pathology · Differential Diagnosis · Investigations · Treatment', 'Page 14–15')

# ------------------------------------------------------------
# 30 — CH4 · Definition + Pathology + D.D
# ------------------------------------------------------------
s30 = f'''{top_band('Ch 04 · Anti-GBM / Goodpasture', 'Definition, Pathology &amp; Differential Diagnosis')}
{body(112, 58)}
{tbl(['Goodpasture Disease (Anti-GBM GN)', "Goodpasture's Syndrome"], [
    ['A <b>kidney-limited</b> disease with:<br>a) GN resulting from glomerular deposition of anti-GBM antibodies<br>b) Circulating anti-GBM antibodies', 'A <b>systemic</b> disease with a triad of:<br>a) GN resulting from glomerular deposition of anti-GBM antibodies<br>b) Circulating anti-GBM antibodies<br>c) <b style="color:#8E3B2B;">Pulmonary hemorrhage</b>'],
], fs=12.5)}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:10px;">
  {card('<b style="color:#8E3B2B;">Diffuse proliferative GN</b> by LM, and <b style="color:#8E3B2B;">linear deposits</b> of anti-GBM IgG antibody by IF.<br><br>• G.P. <b>Disease</b> → GN<br>• G.P. <b>Syndrome</b> → GN + pulmonary hemorrhage', title='Pathology / Histopathology', title_fs=15, fs=12.5)}
  {card('<b>D.D. of hemoptysis with renal disease (Pulmonary-Renal Syndromes):</b><br><span style="padding-left:8px;">1. Goodpasture syndrome</span><br><span style="padding-left:8px;">2. Henoch-Schönlein purpura</span><br><span style="padding-left:8px;">3. Systemic lupus erythematosus (SLE)</span><br><span style="padding-left:8px;">4. Microscopic polyangiitis</span><br><span style="padding-left:8px;">5. Cryoglobulinemia</span><br><span style="padding-left:8px;">6. Advanced uremia with pulmonary edema and coagulopathies</span><br><span style="padding-left:8px;">7. Thrombotic thrombocytopenic purpura (TTP)</span><br><span style="padding-left:8px;">8. Pulmonary embolism with RV thrombosis</span>', title='Differential Diagnosis', title_fs=15, fs=11.5, accent='terra')}
</div>
</div>'''
add(s30, 30, foot='PRINCIPLES OF NEPHROLOGY — Page 14')

# ------------------------------------------------------------
# 31 — CH4 · Investigations + Treatment
# ------------------------------------------------------------
s31 = f'''{top_band('Ch 04 · Anti-GBM / Goodpasture', 'Investigations &amp; Treatment')}
{body(108, 46)}
{card(ul(['Evidence of GN: hematuria with dysmorphic red cells, red cell casts and variable degrees of proteinuria', 'Blood: positive circulating anti-GBM antibodies; other serological tests (complements, ASOT, ANA) are <b style="color:#8E3B2B;">normal</b>', 'Renal biopsy: diffuse proliferative GN'], fs=11.5), title='Investigations', title_fs=15, pad='9px 13px')}
<div style="margin-top:8px;">
{tbl(['Corticosteroids', 'Cyclophosphamide'], [
    ['IV methylprednisolone <b>7–15 mg/kg/day</b> (maximum 1 gm/day) for <b>3 days</b>, then oral prednisone <b>1 mg/kg/day</b>; reduce to 20 mg/day by 6 weeks and continue for 6 months.', 'Dose depends upon the patient&rsquo;s age:<br>• &lt; 55 years: 3 mg/kg (down to 50 mg) for 3 months<br>• &gt; 55 years: 2 mg/kg (down to 50 mg) for 3 months'],
], fs=11.5)}
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:8px;">
  {card('<b>Plasma exchange (plasmapheresis):</b> replacement with daily <b style="color:#8E3B2B;">40–50 ml/kg</b> plasma with albumin for <b>2 weeks</b> or until anti-GBM antibody disappears.', title='Plasma exchange', title_fs=14, fs=11.5, accent='gold', pad='8px 12px')}
  {card('<b>N.B.:</b> Plasmapheresis should <b style="color:#8E3B2B;">not</b> be given in patients with anuria and/or crescents &gt; 85% of glomeruli, <b>unless</b> there is pulmonary hemorrhage. Albumin is the recommended replacement fluid with plasmapheresis because of the lower incidence of complications.', title='Caution', title_fs=14, fs=11.5, accent='terra', pad='8px 12px')}
</div>
<div style="margin-top:8px;">{imp('<b>Summary:</b> 3 days pulse methylprednisolone → 2 weeks course of daily plasmapheresis → 6 months oral corticosteroids and 3 months cyclophosphamide.', 'Protocol')}</div>
</div>'''
add(s31, 31, foot='PRINCIPLES OF NEPHROLOGY — Page 14–15')

# ------------------------------------------------------------
# 32 — DIVIDER 05
# ------------------------------------------------------------
divider('05', 'Post-Streptococcal Glomerulonephritis (PSGN)', 'Organism · Clinical Features · Investigations · Treatment', 'Page 15–17')

# ------------------------------------------------------------
# 33 — CH5 · Organism + Clinical Features
# ------------------------------------------------------------
s33 = f'''{top_band('Ch 05 · Post-Streptococcal GN', 'Organism &amp; History of Infection')}
{body(112, 60)}
{card('Group A <b style="color:#8E3B2B;">β-hemolytic streptococci</b> (nephritogenic strains — types <b style="color:#8E3B2B;">1, 4, 12, 49</b>).<br><b style="color:#8E3B2B;">Type 49 is the most commonly isolated type.</b>', title='Organism', title_fs=16, fs=13)}
<div style="margin-top:12px;">{card('History of streptococcal infection (tonsillitis, pharyngitis, otitis media, or cellulitis) <b style="color:#8E3B2B;">1–2 weeks</b> before the onset of acute nephritis.<br><br>In <b>skin infection</b>, the latent period may be prolonged to <b style="color:#8E3B2B;">4 weeks</b>.<br><br>The latent period (time between exposure to infection and development of acute nephritis) reflects the time taken for immune-complex formation &amp; deposition and glomerular injury.', title='History of streptococcal infection', title_fs=16, fs=13)}</div>
<div style="margin-top:12px;">{imp('A <b>shorter latent period</b> signifies exacerbation of underlying CKD (e.g. IgA nephropathy) rather than de novo acute GN.', 'N.B.')}</div>
</div>'''
add(s33, 33, foot='PRINCIPLES OF NEPHROLOGY — Page 15–16')

s33b = f'''{top_band('Ch 05 · Post-Streptococcal GN', 'Clinical Presentation')}
{body(112, 58)}
{tbl(['Presentation', 'Notes'], [
    ['<b>1. Acute GN:</b> in children, picture of acute GN. In adults, the history of streptococcal infection is less commonly obtained, and the onset is subacute or insidious with progressive, slowly developing edema of the lower limbs.', '• About 10% of infected individuals develop GN<br>• Infection may be mild and pass unnoticed<br>• No relationship between severity of infection and probability of developing acute nephritis'],
    ['<b>2. Nephrotic syndrome:</b> uncommon (&lt; 20% of cases)', ''],
    ['<b>3. RPGN:</b> in 5% of cases', ''],
    ['<b>4. Asymptomatic:</b> discovered during routine urine examination', ''],
], widths=[52, 48], fs=12.5)}
<div style="margin-top:12px;">{imp('~10% of infected individuals develop GN; the infection may be mild and pass unnoticed, and there is <b>no relationship</b> between severity of infection and the probability of developing acute nephritis.', 'Key points')}</div>
</div>'''
add(s33b, 34, foot='PRINCIPLES OF NEPHROLOGY — Page 16')

# ------------------------------------------------------------
# 34 — CH5 · Investigations
# ------------------------------------------------------------
s34 = f'''{top_band('Ch 05 · Post-Streptococcal GN', 'Investigations')}
{body(112, 58)}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card('• Antibodies to streptococcal exo-enzymes: <b style="color:#8E3B2B;">ASO, DNAase, BNDase and hyaluronidase</b><br>• Decrease of <b style="color:#8E3B2B;">CH50 &amp; C3</b> during the acute phase, then returns to normal within <b style="color:#8E3B2B;">8 weeks</b> of nephritis (transient hypocomplementemia)', title='Evidence of streptococcal infection', title_fs=15, fs=12.5)}
  {card('', title='Evidence of acute GN', title_fs=15)}
</div>
<div style="margin-top:8px;">
{tbl(['Modality', 'Finding'], [
    ['Urine examination', 'Dysmorphic red cells, red cell casts &amp; proteinuria (&lt; 3 gm/day)'],
    ['Blood', 'Transient increase of serum cholesterol (in NS), decreased serum albumin, renal impairment'],
    ['Renal biopsy — LM', 'Diffuse endocapillary proliferative GN ± few crescents'],
    ['Renal biopsy — EM', 'Subepithelial electron-dense deposits (<b style="color:#8E3B2B;">humps</b>) and variable degrees of mesangial deposits'],
    ['Renal biopsy — IF', 'Granular deposits of C3 &amp; IgG'],
], widths=[26, 74], fs=12)}
</div>
<div style="margin-top:8px;">{imp('<b style="color:#8E3B2B;">Subepithelial humps</b> on EM + <b style="color:#8E3B2B;">granular C3 &amp; IgG</b> on IF + <b style="color:#8E3B2B;">transient low C3 (recovers &lt; 8 weeks)</b> → PSGN.', 'Biopsy triad')}</div>
</div>'''
add(s34, 34, foot='PRINCIPLES OF NEPHROLOGY — Page 16–17')

# ------------------------------------------------------------
# 35 — CH5 · Treatment
# ------------------------------------------------------------
s35 = f'''{top_band('Ch 05 · Post-Streptococcal GN', 'Treatment')}
{body(92, 56)}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card(ul(['Bed rest', 'Diet: salt, fluid and protein restriction', 'Drugs:', '<span style="padding-left:10px;">a. Diuretics</span>', '<span style="padding-left:10px;">b. Vasodilators for control of blood pressure</span>', '<span style="padding-left:10px;">c. Steroids, cytotoxic drugs and anticoagulants are <b style="color:#8E3B2B;">of no value</b> and may be harmful — <b style="color:#8E3B2B;">except in RPGN</b></span>', 'Dialysis for renal failure'], fs=11.5), title='General / Supportive / Symptomatic', title_fs=14.5, pad='9px 12px')}
  {card('<b>Antibiotic (penicillin) therapy.</b>', title='Specific treatment', title_fs=15)}
</div>
<div style="margin-top:8px;">
{tbl(['For patients', 'For close contacts'], [
    ['Aim:<br>• Decrease antigen load → decrease immune-complex formation → may stop progression of disease<br>• Halt spread of potentially nephritogenic streptococci from the patient to family members in close contact<br>• Such treatment, however, does <b style="color:#8E3B2B;">not</b> seem to be very effective in aborting or ameliorating the course of the disease', 'Use of short-term penicillin prophylaxis (<b style="color:#8E3B2B;">phenoxy penicillin 500 mg/day</b>) to all individuals at high risk in a closed community or family.'],
], fs=11.5)}
</div>
<div style="margin-top:8px;">{note('No effect of long-term penicillin in prophylaxis after the development of GN. Removal of infected tonsils or septic foci should be delayed until convalescence is advanced, as the operation may be followed by exacerbation of the disease. However, if needed, give benzyl penicillin on the day of operation and for three days after.', fs=11.5)}</div>
</div>'''
add(s35, 35)

# ------------------------------------------------------------
# 36 — DIVIDER 06
# ------------------------------------------------------------
divider('06', 'Lupus Nephritis', 'Definition · Prevalence · Pathology · Classes · Diagnosis · Management', 'Page 17–19')

# ------------------------------------------------------------
# 37 — CH6 · Definition + Prevalence + Pathology
# ------------------------------------------------------------
s37 = f'''{top_band('Ch 06 · Lupus Nephritis', 'Definition, Prevalence &amp; Pathology')}
{body(112, 56)}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card('LN is the <b style="color:#8E3B2B;">renal involvement in patients with SLE</b>. It exists with or without clinical manifestations of SLE. It is extremely diverse in its presentation and pathology.', title='Definition', title_fs=15, fs=12.5)}
  {card('The kidney is the <b style="color:#8E3B2B;">most common organ involvement</b> in SLE.<br><br>Clinically, about <b style="color:#8E3B2B;">50% of lupus patients</b> have LN at diagnosis.', title='Prevalence', title_fs=15, fs=12.5)}
</div>
<div style="margin-top:10px;">{card('The glomeruli are essentially involved, which may show:', title='Pathology', title_fs=16)}</div>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;margin-top:8px;">
  <div style="background:#FBF3E4;border:1px solid #E2CFAD;border-top:4px solid #8E3B2B;border-radius:10px;padding:9px 12px;">
    <p style="font-size:13.5px;font-weight:700;color:#4A2F16;margin:0 0 3px 0;">Haematoxylin bodies</p>
    <p style="font-size:11.5px;color:#3A2A18;margin:0;line-height:1.45;">Rounded bluish inclusions in H&amp;E-stained sections. They represent naked nuclei altered by binding to ANA, resulting in clumping of nuclear chromatin. Seen in only <b style="color:#8E3B2B;">2% of cases</b> — <b style="color:#8E3B2B;">pathognomonic of active LN</b>.</p>
  </div>
  <div style="background:#FBF3E4;border:1px solid #E2CFAD;border-top:4px solid #B0722F;border-radius:10px;padding:9px 12px;">
    <p style="font-size:13.5px;font-weight:700;color:#4A2F16;margin:0 0 3px 0;">Wire loop deposits</p>
    <p style="font-size:11.5px;color:#3A2A18;margin:0;line-height:1.45;">Subendothelial immune deposits that encircle the entire glomerular tuft circumference. Best seen in <b style="color:#8E3B2B;">trichrome &amp; silver</b> stained sections.</p>
  </div>
  <div style="background:#FBF3E4;border:1px solid #E2CFAD;border-top:4px solid #A86E1C;border-radius:10px;padding:9px 12px;">
    <p style="font-size:13.5px;font-weight:700;color:#4A2F16;margin:0 0 3px 0;">Hyaline thrombi</p>
    <p style="font-size:11.5px;color:#3A2A18;margin:0;line-height:1.45;">Massive subendothelial immune deposits that protrude into or occlude the glomerular tuft lumina (i.e. intraluminal immune deposits).</p>
  </div>
</div>
<div style="margin-top:8px;">{note('Tubulo-interstitial disease is seen in <b>50% of cases</b>, especially in proliferative LN.')}</div>
</div>'''
add(s37, 37, foot='PRINCIPLES OF NEPHROLOGY — Page 17–18')

# ------------------------------------------------------------
# 38 — CH6 · Pathological Classes
# ------------------------------------------------------------
s38 = f'''{top_band('Ch 06 · Lupus Nephritis', 'Pathological Classes — ISN/RPS Classification')}
{body(112, 58)}
{tbl(['Class', 'Name', 'Description'], [
    ['<b>I</b>', 'Minimal mesangial LN', 'Normal glomeruli by LM, and mesangial immune deposits by IF or EM.'],
    ['<b>II</b>', 'Mesangial proliferative LN', 'Mesangial hypercellularity and/or matrix expansion of any degree, in addition to mesangial immune deposits.'],
    ['<b>III</b>', 'Focal proliferative LN', '<b style="color:#8E3B2B;">&lt; 50%</b> of glomeruli are involved.'],
    ['<b>IV</b>', 'Diffuse proliferative LN', '<b style="color:#8E3B2B;">&gt; 50%</b> of glomeruli are involved.'],
    ['<b>V</b>', 'Membranous LN', 'Diffuse (global) glomerular capillary wall thickening plus continuous subepithelial immune deposits.'],
    ['<b>VI</b>', 'Advanced-stage LN', 'Global glomerulosclerosis of <b style="color:#8E3B2B;">≥ 90%</b> of the total glomeruli, without evidence of active lesion.'],
], widths=[8, 26, 66], fs=12.5)}
<div style="margin-top:10px;">{imp('6 major classes based upon LM, IF, and EM studies of renal biopsy, according to the <b>International Society of Nephrology / Renal Pathology Society (ISN/RPS)</b> classification.', 'Remember')}</div>
</div>'''
add(s38, 38, foot='PRINCIPLES OF NEPHROLOGY — Page 18')

# ------------------------------------------------------------
# 39 — CH6 · Clinical Features + Diagnosis
# ------------------------------------------------------------
s39 = f'''{top_band('Ch 06 · Lupus Nephritis', 'Clinical Features &amp; Diagnosis')}
{body(112, 58)}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card('• <b>Asymptomatic</b> in many patients.<br>• <b>Symptomatic</b> — manifested as:<br><span style="padding-left:8px;">– <b style="color:#8E3B2B;">Hypertension</b>: a clue of renal disease</span><br><span style="padding-left:8px;">– Symptoms and signs of acute nephritis, nephrotic syndrome, or rapidly progressive renal failure, and ESRD</span>', title='Clinical Features', title_fs=15, fs=12.5)}
  {card('• <b>Clinical:</b> hypertension and/or renal edema.<br><br>• <b>Laboratory findings:</b><br><span style="padding-left:8px;">– Urine examination (red cells, casts, proteinuria)</span><br><span style="padding-left:8px;">– Elevated serum creatinine level</span>', title='Diagnosis — Clinical &amp; Laboratory', title_fs=15, fs=12.5)}
</div>
<div style="margin-top:10px;">{card('<b>Renal biopsy</b> is useful in determining initial management — every patient suspected of having microangiopathy with LN requires a biopsy to:', title='Role of Renal Biopsy', title_fs=15)}</div>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;margin-top:8px;">
  {card('Determine the nature of the renal pathology and the <b style="color:#8E3B2B;">pathological class</b>.', title_fs=14, fs=12)}
  {card('Exclude other lesions that may complicate the course of SLE, such as <b>hypersensitivity interstitial nephritis</b> when the patient develops ATN, and <b>pure antiphospholipid syndrome</b>.', title_fs=14, fs=12)}
  {card('Assessment of the <b style="color:#8E3B2B;">activity index (0–24 score)</b> — acute and potentially treatable lesions — and the <b style="color:#8E3B2B;">chronicity index (0–12 score)</b> — irreversible lesions — which determine therapy &amp; prognosis.', title_fs=14, fs=12)}
</div>
</div>'''
add(s39, 39, foot='PRINCIPLES OF NEPHROLOGY — Page 18–19')

# ------------------------------------------------------------
# 40 — CH6 · Management + Prognosis
# ------------------------------------------------------------
s40 = f'''{top_band('Ch 06 · Lupus Nephritis', 'Management &amp; Prognosis')}
{body(112, 56)}
{card('<b style="color:#8E3B2B;">Principal goal:</b> normalize renal function &amp; prevent loss of renal function.', title='Goal of management', title_fs=15)}
<div style="margin-top:8px;">
{tbl(['Measure', 'Recommendation'], [
    ['Hydroxychloroquine', 'Or an equivalent antimalarial — to <b style="color:#8E3B2B;">all</b> patients with LN unless contraindicated.'],
    ['Control of hypertension', 'Target blood pressure ≤ <b style="color:#8E3B2B;">120/80 mmHg</b>.'],
    ['Control of proteinuria', 'Low doses of ACEIs or ARBs &amp; protein restriction.'],
    ['Control of hyperlipidemia', 'Statins and low-fat diet.'],
    ['Avoid nephrotoxic drugs', 'e.g. NSAIDs. <b style="color:#8E3B2B;">Non-acetylated salicylates are safe</b>.'],
    ['Avoid pregnancy in patients with active LN', 'It may worsen their renal disease; moreover, certain medications may be teratogenic.'],
], widths=[36, 64], fs=12, tpad=3)}
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:4px;">
  {card('<b>Specific treatment:</b> corticosteroids and immunosuppressive treatment of LN is divided into <b style="color:#8E3B2B;">induction</b> and <b style="color:#8E3B2B;">maintenance</b> phases.<br><br>• Corticosteroids should be instituted if the patient has clinically significant renal disease.<br>• Immunosuppressive agents: <b>cyclophosphamide, mycophenolate mofetil, azathioprine, or cyclosporine A</b>.', title='I. General + II. Specific', title_fs=15, fs=12)}
  {card('• Class <b style="color:#5F6B2E;">I, II and V</b> → generally <b style="color:#5F6B2E;">good prognosis</b>.<br>• Class <b style="color:#8E3B2B;">III and IV</b> → <b style="color:#8E3B2B;">poor prognosis</b> — tend to progress to ESRD, particularly class IV.<br>• Class <b style="color:#8E3B2B;">VI</b> → hemodialysis or transplantation.', title='Prognosis', title_fs=15, fs=12.5, accent='gold')}
</div>
</div>'''
add(s40, 40)

# ------------------------------------------------------------
# 41 — DIVIDER 07
# ------------------------------------------------------------
divider('07', 'Diabetic Nephropathy', 'Complications · Definition · Stages · Pathology · Pathogenesis · Diagnosis · Treatment', 'Page 19–22')

# ------------------------------------------------------------
# 42 — CH7 · Renal Complications + Definition + Prevalence
# ------------------------------------------------------------
s42 = f'''{top_band('Ch 07 · Diabetic Nephropathy', 'Renal Complications in Diabetes, Definition &amp; Prevalence')}
{body(112, 56)}
{card('Renal complications in diabetic patients:', title='Complications', title_fs=16)}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:8px;">
  <div style="background:#FBF3E4;border:1px solid #E2CFAD;border-radius:10px;padding:9px 13px;">
    <p style="font-size:12px;color:#3A2A18;margin:0;line-height:1.55;"><b style="color:#8E3B2B;">1. Diabetic Nephropathy (DN)</b> — diabetic glomerulosclerosis<br><b style="color:#8E3B2B;">2.</b> Papillary necrosis<br><b style="color:#8E3B2B;">3.</b> UTI (asymptomatic bacteriuria, acute pyelonephritis, perinephric abscess)</p>
  </div>
  <div style="background:#FBF3E4;border:1px solid #E2CFAD;border-radius:10px;padding:9px 13px;">
    <p style="font-size:12px;color:#3A2A18;margin:0;line-height:1.55;"><b style="color:#8E3B2B;">4.</b> Ischemic nephropathy due to renal artery atherosclerosis<br><b style="color:#8E3B2B;">5.</b> Hydronephrosis due to atonic bladder<br><b style="color:#8E3B2B;">6.</b> AKI secondary to: a) reaction to contrast (contrast nephropathy) b) urinary tract obstruction secondary to papillary necrosis</p>
  </div>
</div>
<div style="margin-top:8px;">{note('As type 2 DM is more common, most of the cases of DN seen are associated with type 2 DM.')}</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:10px;">
  {card('Presence of <b style="color:#8E3B2B;">proteinuria</b> with or without hypertension and renal impairment in patients with diabetes mellitus of <b style="color:#8E3B2B;">several years duration</b>.', title='Definition of DN', title_fs=15, fs=12.5)}
  {card('• In <b style="color:#8E3B2B;">type 1:</b> about <b style="color:#8E3B2B;">30–50%</b> of patients develop DN, since they survive longer.<br>• In <b style="color:#8E3B2B;">type 2:</b> about <b style="color:#8E3B2B;">20%</b> of patients develop DN, since they usually die earlier.', title='Prevalence', title_fs=15, fs=12.5)}
</div>
</div>'''
add(s42, 42, foot='PRINCIPLES OF NEPHROLOGY — Page 19–20')

# ------------------------------------------------------------
# 43 — CH7 · Clinical Features (Stages)
# ------------------------------------------------------------
s43 = f'''{top_band('Ch 07 · Diabetic Nephropathy', 'Clinical Features — Stages')}
{body(112, 58)}
{tbl(['Stage', 'Description'], [
    ['<b>Stage I</b> — Hyperfiltration / Hypertrophy stage', 'Increase in GFR by <b style="color:#8E3B2B;">20–40%</b> above age-matched control subjects. Hypertrophy of the kidneys by ultrasound. Clinically, there may be polyuria.'],
    ['<b>Stage II</b> — Silent stage', 'Normal GFR (in most patients). Normal urinary albumin excretion (&lt; 30 mg/day). Early structural renal damage.<br><b>N.B.:</b> About 30–50% of patients will proceed to stage III.'],
    ['<b>Stage III</b> — Incipient nephropathy', 'GFR starts to decline. <b style="color:#8E3B2B;">Microalbuminuria (30–300 mg/day)</b> — 5–10 years after the onset of DM. Early hypertension or rise of BP above the previous reading.'],
    ['<b>Stage IV</b> — Overt nephropathy', 'Progressive reduction of GFR. <b style="color:#8E3B2B;">Overt proteinuria &gt; 0.5 gm/day</b>. Hypertension.'],
    ['<b>Stage V</b> — ESRD', 'ESRD requiring renal replacement therapy. Presence of other complications of diabetes: retinopathy, neuropathy, CHF, cerebrovascular disease &amp; peripheral vascular disease.'],
], widths=[30, 70], fs=11.8)}
<div style="margin-top:8px;">{card('<b style="color:#8E3B2B;">In type 2 DM:</b><br><span style="padding-left:8px;">• Hyperfiltration stage is rarely detected</span><br><span style="padding-left:8px;">• Microalbuminuria is frequently present at the diagnosis of DM</span><br><span style="padding-left:8px;">• Hypertension is usually present at the time of diagnosis of nephropathy</span>', title='Type 2 DM — differences', title_fs=14, fs=12, accent='gold', bg='rgba(168,110,28,0.10)')}</div>
</div>'''
add(s43, 43, foot='PRINCIPLES OF NEPHROLOGY — Page 20')

# ------------------------------------------------------------
# 44 — CH7 · Pathology + Pathogenesis
# ------------------------------------------------------------
s44 = f'''{top_band('Ch 07 · Diabetic Nephropathy', 'Pathology &amp; Pathogenesis')}
{body(112, 58)}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card(ul(['<b>Glomerulosclerosis</b>: diffuse (more common but non-specific) and/or <b style="color:#8E3B2B;">nodular (less common but pathognomonic)</b>', '<b>Chronic tubulo-interstitial nephritis</b>', '<b>Vasculitic lesions</b>: arteriolosclerosis in afferent &amp; efferent arterioles (<b style="color:#8E3B2B;">pathognomonic for DM</b>)'], fs=12), title='Pathology — 3 major lesions', title_fs=15)}
  {card('', title='Pathogenesis (multifactorial)', title_fs=15)}
</div>
<div style="margin-top:8px;">
{tbl(['Factor', 'Mechanism'], [
    ['<b>1. Haemodynamic</b>', 'Hyperglycemia → ↑ GFR → ↑ intraglomerular pressure → endothelial injury → <b style="color:#8E3B2B;">glomerulosclerosis</b>.'],
    ['<b>2. Metabolic</b>', 'Hyperglycemia → glycosylation of mesangial &amp; GBM proteins → trapping of circulating macromolecules in the glomerular capillary wall and mesangium → mesangial hyperplasia → alteration of GBM permeability.'],
    ['<b>3. Genetic susceptibility</b>', 'As not all diabetic patients develop DN.'],
], widths=[24, 76], fs=12)}
</div>
</div>'''
add(s44, 44, foot='PRINCIPLES OF NEPHROLOGY — Page 20–21')

# ------------------------------------------------------------
# 45 — CH7 · Risk Factors + Diagnosis
# ------------------------------------------------------------
s45 = f'''{top_band('Ch 07 · Diabetic Nephropathy', 'Risk Factors &amp; Diagnosis')}
{body(112, 58)}
<div style="display:grid;grid-template-columns:1fr 2fr;gap:12px;">
  <div style="display:flex;flex-direction:column;gap:10px;">
    {card(ul(['Proteinuria', 'Hypertension', 'Hyperglycemia', 'Smoking', 'High-protein diet', 'Genetic factors'], fs=12.5), title='Risk factors for progression of DN', title_fs=15, accent='terra')}
  </div>
  {card('<b style="color:#8E3B2B;">Clinical diagnosis:</b><br><span style="padding-left:8px;">• DM of ≥ 10 years duration with proteinuria ± HTN &amp; renal insufficiency</span><br><span style="padding-left:8px;">• The presence of <b style="color:#8E3B2B;">diabetic retinopathy</b> strengthens the diagnosis</span><br><br><b style="color:#8E3B2B;">Urine examination:</b> presence of proteinuria (micro- or macro-albuminuria).', title='Diagnosis (clinical + urine examination ± renal biopsy)', title_fs=15, fs=12)}
</div>
<div style="margin-top:8px;">
{tbl(['Criteria of DN as a cause of CKD', 'Renal biopsy is needed if'], [
    ['1. Long-standing DM (≥ 10 years) before the onset of CKD<br>2. Normal-sized kidneys (by US)<br>3. Presence of diabetic retinopathy<br>4. Benign urinary sediment — no hematuria, no cellular casts<br>5. Proteinuria still present when the patient has already started dialysis', '1. Duration of DM &lt; 10 years in the absence of retinopathy or neuropathy<br>2. Suspicion of an alternative diagnosis, such as:<br>&nbsp;&nbsp;– Sudden onset of NS in early DM (&lt; 7 years in type 1, &lt; 5 years in type 2)<br>&nbsp;&nbsp;– Renal insufficiency + active urinary sediment (red cells, cellular casts)'],
], widths=[50, 50], fs=11.5)}
</div>
</div>'''
add(s45, 45, foot='PRINCIPLES OF NEPHROLOGY — Page 21')

# ------------------------------------------------------------
# 46 — CH7 · Treatment
# ------------------------------------------------------------
s46 = f'''{top_band('Ch 07 · Diabetic Nephropathy', 'Treatment')}
{body(112, 56)}
{card('<b style="color:#8E3B2B;">Aim:</b> slow the progression of the disease by tight control of hyperglycemia, hypertension, UTI, and protein restriction — and RRT for ESRD diabetic patients.', title='Aim', title_fs=15)}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:8px;">
  {card('• <b>Control of hyperglycemia:</b> insulin + proper diet.<br>• <b>Control of UTI:</b> proper antibiotic according to urine culture and sensitivity.<br>• <b>Dietary protein restriction:</b> <b style="color:#8E3B2B;">0.6–0.8 gm/kg/day</b> in patients with decreased GFR.<br>• <b>RRT for ESRD patients:</b> considered <b style="color:#8E3B2B;">early at GFR &lt; 20 ml/min</b>.', title='Hyperglycemia, UTI, Protein, RRT', title_fs=15, fs=12)}
  {card('<b>Control of hypertension</b> — one of the most important factors.<br><br><b>Goals:</b><br><span style="padding-left:8px;">• &lt; <b style="color:#8E3B2B;">130/80 mmHg</b> in patients without proteinuria</span><br><span style="padding-left:8px;">• &lt; <b style="color:#8E3B2B;">125/75 mmHg</b> in patients with proteinuria</span><br><br><b>Drugs:</b><br><span style="padding-left:8px;">– ACEI / ARBs</span><br><span style="padding-left:8px;">– Diuretics in addition to ACEIs</span><br><span style="padding-left:8px;">– CCB (non-dihydropyridine: verapamil &amp; diltiazem)</span><br><span style="padding-left:8px;">– β-blockers (BBs)</span><br><span style="padding-left:8px;">– Alpha-receptor antagonist, e.g. prazosin</span>', title='Hypertension', title_fs=15, fs=12)}
</div>
<div style="margin-top:8px;">{imp('Because the kidney metabolizes and excretes insulin, the half-life of insulin (endogenous and exogenous) is prolonged in the setting of decreased GFR — therefore <b>decrease the dose of insulin</b> in DN patients to avoid hypoglycemia.', 'N.B.')}</div>
</div>'''
add(s46, 46, foot='PRINCIPLES OF NEPHROLOGY — Page 21–22')

# ------------------------------------------------------------
# 47 — High-yield contrasts
# ------------------------------------------------------------
s47 = f'''{top_band('Glomerular Diseases · Final', 'High-Yield Contrasts &amp; Key Points')}
{body(112, 58)}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  <div style="background:#FBF3E4;border:1px solid #E2CFAD;border-left:5px solid #8E3B2B;border-radius:10px;padding:10px 13px;">
    <p style="font-size:14.5px;font-weight:700;color:#4A2F16;margin:0 0 4px 0;">Nephritic vs Nephrotic</p>
    <p style="font-size:11.5px;color:#3A2A18;margin:0;line-height:1.5;">
      <b style="color:#8E3B2B;">Nephritic (acute GN):</b> hematuria ± RBC casts, proteinuria &lt; 3.5 gm/day, oliguria, HTN, edema — sudden onset.<br>
      <b style="color:#8E3B2B;">Nephrotic:</b> proteinuria ≥ 3.5 gm/day, albumin ≤ 2.5 gm/dl, edema, hyperlipidemia — frothy urine.<br>
      <b style="color:#8E3B2B;">RPGN:</b> crescents — renal emergency.</p>
  </div>
  <div style="background:#FBF3E4;border:1px solid #E2CFAD;border-left:5px solid #B0722F;border-radius:10px;padding:10px 13px;">
    <p style="font-size:14.5px;font-weight:700;color:#4A2F16;margin:0 0 4px 0;">Immunofluorescence patterns</p>
    <p style="font-size:11.5px;color:#3A2A18;margin:0;line-height:1.5;">
      <b style="color:#8E3B2B;">Linear</b> (smooth) → anti-GBM disease.<br>
      <b style="color:#8E3B2B;">Granular</b> (diffuse) → immune-complex GN (e.g. PSGN: C3 + IgG; lupus: full house).<br>
      <b style="color:#8E3B2B;">No deposits</b> → MCD (foot-process fusion on EM).</p>
  </div>
  <div style="background:#FBF3E4;border:1px solid #E2CFAD;border-left:5px solid #5F6B2E;border-radius:10px;padding:10px 13px;">
    <p style="font-size:14.5px;font-weight:700;color:#4A2F16;margin:0 0 4px 0;">Low serum complement</p>
    <p style="font-size:11.5px;color:#3A2A18;margin:0;line-height:1.5;">
      PSGN (<b style="color:#8E3B2B;">transient, &lt; 8 weeks</b>), infective endocarditis, shunt nephropathy, <b style="color:#8E3B2B;">SLE</b>, cryoglobulinemia, serum sickness.</p>
  </div>
  <div style="background:#FBF3E4;border:1px solid #E2CFAD;border-left:5px solid #A86E1C;border-radius:10px;padding:10px 13px;">
    <p style="font-size:14.5px;font-weight:700;color:#4A2F16;margin:0 0 4px 0;">Blood pressure targets (proteinuria-adjusted)</p>
    <p style="font-size:11.5px;color:#3A2A18;margin:0;line-height:1.5;">
      Proteinuria &gt; 1 gm/day → <b style="color:#8E3B2B;">&lt; 125/75</b> (mean &lt; 92).<br>
      Proteinuria &lt; 1 gm/day → <b style="color:#8E3B2B;">&lt; 130/80</b> (mean &lt; 98).<br>
      Lupus nephritis → ≤ <b style="color:#8E3B2B;">120/80</b>. DN without proteinuria → &lt; 130/80; with proteinuria → &lt; 125/75.<br>
      First-line renoprotection in all: <b style="color:#8E3B2B;">ACEIs / ARBs</b>.</p>
  </div>
</div>
<div style="margin-top:10px;">{imp('Full details of every chapter — definitions, causes, pathology, investigations, treatment protocols and course — are preserved on the preceding slides without summarization.', 'Complete deck')}</div>
</div>'''
add(s47, 47)

# ============================================================
# WRITE FILES
# ============================================================
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'slides')
os.makedirs(OUT, exist_ok=True)

for i, (body_html, foot, show_badge, badge_right) in enumerate(slides, start=1):
    num = i if show_badge else None
    html = wrap(body_html, num, foot, badge_right)
    path = os.path.join(OUT, f'slide-{i:02d}.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

print(f"Wrote {len(slides)} slides to {OUT}")
