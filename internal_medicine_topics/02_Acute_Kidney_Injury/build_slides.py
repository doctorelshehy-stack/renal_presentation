# -*- coding: utf-8 -*-
"""Build a no-summarization HTML slide deck from the two AKI markdown files.
Theme: brown background, light mode, warm harmony colors, contrast for important info.
"""
import os

os.makedirs('slides', exist_ok=True)

# ---------------- Theme (brown / light mode / harmony) ----------------
TAN      = '#EDDCC2'   # slide background (warm light brown / tan)
CREAM    = '#FBF3E3'   # card background
CREAM2   = '#F4E6CC'   # alt card background
DEEP     = '#5B3A21'   # deep espresso brown (cover / headings / dividers)
BROWN    = '#7A5636'   # coffee brown (badges, table headers, borders)
CARAMEL  = '#B07C44'   # caramel (section numbers, accent bars)
AMBER    = '#D9A23B'   # amber (key highlights)
RUST     = '#B85C38'   # rust (emphasis / important)
DANGER   = '#9E3B2C'   # deep rust red (warnings / very important)
OLIVE    = '#6E7F4A'   # olive-sage (secondary contrast)
INK      = '#3A2A1B'   # body text (dark espresso)
SOFT     = '#5C4A38'   # secondary text
ON_DARK  = '#FBF3E3'   # cream text on brown

F = "'Times New Roman',serif"

# ---------------- Template ----------------
TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
html, body { margin:0; padding:0; width:100%%; height:100%%; overflow:hidden; display:flex; justify-content:center; align-items:center; background:#000; }
.slide-content { width:960px; height:540px; position:relative; transform-origin:center center; }
</style>
<script>
function scaleSlide(){const s=document.querySelector('.slide-content');if(!s)return;const sx=window.innerWidth/960;const sy=window.innerHeight/540;const sc=Math.min(sx,sy);s.style.width='960px';s.style.height='540px';s.style.transform='scale('+sc+')';s.style.transformOrigin='center center';s.style.flexShrink='0';}
window.addEventListener('load',scaleSlide);window.addEventListener('resize',scaleSlide);
</script>
</head>
<body>
<div class="slide-content" style="width:960px;height:540px;background:%(bg)s;font-family:%(font)s;overflow:hidden;">
%(body)s
%(badge)s
</div>
</body>
</html>
"""

def write_slide(num, body, bg=TAN, badge_num=None):
    b = ''
    if badge_num is not None:
        b = f'''<svg style="position:absolute;right:28px;bottom:20px;width:40px;height:30px;z-index:100;" aria-hidden="true">
  <rect x="0" y="0" width="40" height="30" rx="4" fill="{BROWN}"/>
  <text x="20" y="21" font-family="Times New Roman,serif" font-size="16" font-weight="700" fill="{ON_DARK}" text-anchor="middle">{badge_num}</text>
</svg>'''
    html = TEMPLATE % {'bg': bg, 'font': F, 'body': body, 'badge': b}
    with open(f'slides/slide-{num:02d}.html', 'w') as fh:
        fh.write(html)
    print(f'wrote slide-{num:02d}.html')

# ---------------- Helpers ----------------
def hdr(num, title, color=CARAMEL):
    return f'''<div style="position:absolute;top:20px;left:50px;right:50px;z-index:10;">
  <div style="display:flex;align-items:baseline;gap:12px;">
    <span style="font-size:24px;font-weight:700;color:{color};">{num}</span>
    <p style="font-size:30px;font-weight:700;color:{DEEP};margin:0;line-height:1.1;">{title}</p>
  </div>
  <div style="width:70px;height:4px;background:{CARAMEL};margin:7px 0 0 0;"></div>
</div>'''

def content(body):
    return f'<div style="position:absolute;top:88px;left:50px;right:50px;bottom:46px;z-index:10;">{body}</div>'

def card(title, html, accent=BROWN, bg=CREAM, pad='12px 16px', radius='10px'):
    t = f'<p style="font-size:17px;font-weight:700;color:{DEEP};margin:0 0 6px 0;">{title}</p>' if title else ''
    return f'<div style="background:{bg};border-radius:{radius};padding:{pad};border-left:5px solid {accent};box-shadow:0 1px 3px rgba(91,58,33,0.18);">{t}{html}</div>'

def warn(html):
    return f'''<div style="background:#F6DFD2;border-radius:8px;padding:11px 18px;border:1.5px solid {RUST};">
  <p style="font-size:13.5px;color:{INK};margin:0;line-height:1.5;"><b style="color:{DANGER};">&#9888; Important:</b> {html}</p>
</div>'''

def note(html):
    return f'''<div style="background:#EFE7D2;border-radius:8px;padding:8px 14px;border-left:5px solid {AMBER};">
  <p style="font-size:14px;color:{INK};margin:0;line-height:1.45;"><b style="color:{CARAMEL};">NB:</b> {html}</p>
</div>'''

def ul(items, size=14, color=INK, pad='0 0 0 18px', gap='5px'):
    lis = ''
    for it in items:
        lis += f'<li style="margin:0 0 {gap} 0;">{it}</li>'
    return f'<ul style="margin:0;padding:{pad};color:{color};font-size:{size}px;line-height:1.42;">{lis}</ul>'

# =====================================================================
# SLIDE 1 — Cover (09)
# =====================================================================
cover = f'''
<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:{DEEP};"></div>
<div style="position:absolute;top:0;left:0;width:26px;height:540px;background:{CARAMEL};"></div>
<div style="position:absolute;bottom:0;left:0;width:960px;height:90px;background:{BROWN};"></div>
<svg style="position:absolute;top:-70px;right:-90px;width:520px;height:420px;z-index:1;" aria-hidden="true">
  <ellipse cx="260" cy="210" rx="210" ry="300" fill="{CARAMEL}" opacity="0.25"/>
</svg>
<svg style="position:absolute;bottom:0;left:300px;width:520px;height:260px;z-index:1;" aria-hidden="true">
  <ellipse cx="260" cy="130" rx="240" ry="150" fill="{BROWN}" opacity="0.35"/>
</svg>
<div style="position:absolute;top:110px;left:80px;z-index:10;">
  <div style="width:90px;height:5px;background:{AMBER};margin-bottom:16px;"></div>
  <p style="font-size:22px;color:{AMBER};margin:0;font-weight:400;letter-spacing:3px;">INTERNAL MEDICINE &middot; NEPHROLOGY</p>
  <p style="font-size:56px;color:{ON_DARK};margin:10px 0 0 0;font-weight:700;line-height:1.08;">Acute Kidney Injury</p>
  <p style="font-size:40px;color:{AMBER};margin:6px 0 0 0;font-weight:700;">(AKI)</p>
  <div style="width:70px;height:4px;background:{AMBER};margin:22px 0 16px 0;"></div>
  <p style="font-size:22px;color:{ON_DARK};margin:0;font-weight:400;">Chapter 09 &mdash; Principles of Nephrology</p>
</div>
<div style="position:absolute;bottom:28px;left:80px;z-index:10;">
  <p style="font-size:17px;color:{ON_DARK};margin:0;opacity:0.95;">Dr. Hassan Abd-Elhady &mdash; Menoufia University</p>
  <p style="font-size:14px;color:{ON_DARK};margin:3px 0 0 0;opacity:0.7;">Definition &middot; RIFLE/AKIN Staging &middot; Causes &middot; Clinical Picture &middot; Investigations &middot; Treatment</p>
</div>
'''
write_slide(1, cover, bg=DEEP, badge_num=None)

# =====================================================================
# SLIDE 2 — TOC (09)
# =====================================================================
toc_items = [
    ('01', 'Definition'),
    ('02', 'Categorization of AKI (RIFLE &amp; AKIN staging)'),
    ('03', 'Causes &mdash; Pre-renal &middot; Renal &middot; Post-renal'),
    ('04', 'Clinical Manifestations'),
    ('05', 'Investigations'),
    ('06', 'Principles of Treatment'),
]
toc = f'''
<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:{TAN};"></div>
<div style="position:absolute;top:20px;left:60px;z-index:10;">
  <p style="font-size:34px;color:{DEEP};font-weight:700;margin:0;">Table of Contents</p>
  <div style="width:70px;height:4px;background:{CARAMEL};margin:9px 0 24px 0;"></div>
</div>
<div style="position:absolute;top:95px;left:60px;right:60px;z-index:10;">
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px 26px;">
'''
for n, t in toc_items:
    toc += f'''    <div style="display:flex;align-items:center;gap:14px;padding:12px 16px;background:{CREAM};border-radius:8px;border-left:4px solid {BROWN};box-shadow:0 1px 3px rgba(91,58,33,0.16);">
      <span style="font-size:22px;font-weight:700;color:{CARAMEL};min-width:34px;">{n}</span>
      <span style="font-size:18px;color:{INK};">{t}</span>
    </div>
'''
toc += '''  </div>
</div>
'''
write_slide(2, toc)

# =====================================================================
# SLIDE 3 — Section divider 01 Definition
# =====================================================================
def divider(big, title, subtitle, topics=None):
    html = f'''
<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:{DEEP};"></div>
<div style="position:absolute;top:0;right:0;width:360px;height:540px;background:{BROWN};opacity:0.5;"></div>
<svg style="position:absolute;top:0;right:-60px;width:420px;height:540px;z-index:1;" aria-hidden="true">
  <circle cx="180" cy="270" r="170" fill="{CARAMEL}" opacity="0.18"/>
</svg>
<div style="position:absolute;top:130px;left:80px;z-index:10;">
  <p style="font-size:96px;font-weight:700;color:{CARAMEL};margin:0;line-height:1;">{big}</p>
  <div style="width:84px;height:4px;background:{AMBER};margin:14px 0 16px 0;"></div>
  <p style="font-size:38px;font-weight:700;color:{ON_DARK};margin:0;">{title}</p>
  <p style="font-size:20px;color:{AMBER};margin:9px 0 0 0;max-width:600px;line-height:1.35;">{subtitle}</p>
'''
    if topics:
        html += f'  <div style="margin-top:26px;max-width:720px;">{topics}</div>'
    html += '</div>'
    return html

write_slide(3, divider('01', 'Definition', 'AKI &mdash; an abrupt (within 48 hours) and sustained decrease in kidney function'))

# =====================================================================
# SLIDE 4 — Definition content
# =====================================================================
s4 = content(
    card('', f'''
    <ul style="margin:0;padding:0 0 0 20px;color:{INK};font-size:15px;line-height:1.5;">
      <li style="margin-bottom:14px;">AKI is an <b style="color:{DANGER};">abrupt (within 48 hours)</b> and <b style="color:{DANGER};">sustained decrease in kidney function</b>, accompanied by changes in blood biochemistry (e.g. a <b style="color:{DANGER};">rise in serum creatinine</b>), urine output, or both.</li>
      <li>The term AKI has been proposed to <b style="color:{RUST};">encompass the entire spectrum</b> of the syndrome from a mild transient rise in s. creatinine to <b style="color:{RUST};">overt renal failure requiring RRT</b>; hence the term <b style="color:{DANGER};">AKI is more precise</b> than the term acute RF.</li>
    </ul>
    ''', accent=DANGER) +
    f'<div style="height:14px;"></div>' +
    card('<b>Key Points</b>', f'''
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;">
      <div style="background:{CREAM2};border-radius:8px;padding:10px 12px;border-top:3px solid {AMBER};"><p style="font-size:12px;color:{INK};margin:0;"><b style="color:{CARAMEL};">48 h</b><br>abrupt onset window</p></div>
      <div style="background:{CREAM2};border-radius:8px;padding:10px 12px;border-top:3px solid {AMBER};"><p style="font-size:12px;color:{INK};margin:0;"><b style="color:{CARAMEL};">Cr &uarr; / urine output</b><br>sustained change or both</p></div>
      <div style="background:{CREAM2};border-radius:8px;padding:10px 12px;border-top:3px solid {AMBER};"><p style="font-size:12px;color:{INK};margin:0;"><b style="color:{CARAMEL};">RRT possible</b><br>full spectrum &rarr; overt failure</p></div>
    </div>
    ''', accent=AMBER, bg=CREAM2)
)
write_slide(4, hdr('01', 'Definition') + s4)

# =====================================================================
# SLIDE 5 — RIFLE/AKIN table
# =====================================================================
rows = [
    ('Risk', '1', '&ge;1.5 &ndash; 2 folds &uarr; above baseline; or S. Cr. &uarr; by &ge;0.3', '&lt; 0.5 ml/kg/h for 6 hours', ''),
    ('Injury', '2', '&ge; 2 folds &uarr;', '&lt; 0.5 ml/kg/h for 12 hours', ''),
    ('Failure', '3', '&ge; 3 folds &uarr;; or S. Cr. &ge; 4.0 with rise of &ge; 0.5', '&lt; 0.3 ml/kg/h for 24 hours or anuria for 12 hs', ''),
    ('Loss', '&mdash;', 'Persistent loss of renal function for &gt; 4 weeks', '&mdash;', ''),
    ('ESRD', '&mdash;', 'Permanent loss of renal function for &gt; 3 months', '&mdash;', ''),
]
tr = ''
for i, (r, a, cr, uo, _) in enumerate(rows):
    bgc = CREAM if i % 2 == 0 else CREAM2
    hl = DANGER if r in ('Failure',) else INK
    tr += f'''<tr style="background:{bgc};">
      <td style="padding:7px 10px;border:1px solid #C9AC85;font-weight:700;color:{BROWN};">{r}</td>
      <td style="padding:7px 10px;border:1px solid #C9AC85;text-align:center;color:{CARAMEL};font-weight:700;">{a}</td>
      <td style="padding:7px 10px;border:1px solid #C9AC85;color:{hl};">{cr}</td>
      <td style="padding:7px 10px;border:1px solid #C9AC85;color:{hl};">{uo}</td>
    </tr>'''
s5 = content(f'''
<p style="font-size:14px;color:{SOFT};margin:0 0 10px 0;font-style:italic;">Categorization of AKI according to RIFLE and AKIN stage using serum creatinine and urine output criteria</p>
<table style="width:100%;border-collapse:collapse;font-size:13px;">
  <tr style="background:{BROWN};color:{ON_DARK};">
    <th style="padding:8px 10px;border:1px solid {BROWN};text-align:left;">RIFLE</th>
    <th style="padding:8px 10px;border:1px solid {BROWN};text-align:center;">AKIN</th>
    <th style="padding:8px 10px;border:1px solid {BROWN};text-align:left;">S. Cr. changes</th>
    <th style="padding:8px 10px;border:1px solid {BROWN};text-align:left;">Urine output criteria</th>
  </tr>
  {tr}
</table>
<div style="height:12px;"></div>
{note('Progression: <b>Risk &rarr; Injury &rarr; Failure</b> (reversible stages); <b>Loss</b> = persistent loss &gt; 4 weeks; <b>ESRD</b> = permanent loss &gt; 3 months.')}
''')
write_slide(5, hdr('02', 'Categorization of AKI &mdash; RIFLE &amp; AKIN Staging') + s5)

# =====================================================================
# SLIDE 6 — Section divider 02 Causes
# =====================================================================
topics6 = f'''
<div style="display:flex;gap:12px;">
  <div style="background:{BROWN};border-radius:8px;padding:10px 16px;"><p style="font-size:15px;color:{ON_DARK};margin:0;font-weight:700;">Pre-renal</p></div>
  <div style="background:{BROWN};border-radius:8px;padding:10px 16px;"><p style="font-size:15px;color:{ON_DARK};margin:0;font-weight:700;">Renal (intrinsic)</p></div>
  <div style="background:{BROWN};border-radius:8px;padding:10px 16px;"><p style="font-size:15px;color:{ON_DARK};margin:0;font-weight:700;">Post-renal</p></div>
</div>
'''
write_slide(6, divider('02', 'Causes', 'Pre-renal &middot; Intra-renal (intrinsic) &middot; Post-renal', topics6))

# =====================================================================
# SLIDE 7 — Pre-renal causes
# =====================================================================
pr = [
    ('<b>Decreased effective extracellular volume</b>', 'Fluid loss; hemorrhage, vomiting, diarrhea, burn &amp; diuretics. Redistribution; liver cell failure, NS, intestinal obstruction, pancreatitis, and malnutrition.'),
    ('<b>Decreased cardiac output</b>', 'Cardiogenic shock, valvulopathy, myocarditis, MI, arrhythmias, CHF, p. emboli, and cardiac tamponade.'),
    ('<b>Peripheral VD</b>', 'hypotension, sepsis, hypoxemia, anaphylactic shock.'),
    ('<b>Renal vasoconstriction</b>', 'PG inhibition, adrenergics, sepsis, hepato-renal syndrome and hypercalcemia.'),
    ('<b>Efferent arteriole vasodilatation</b>', 'ACEIs and ARBs &rarr; decreased intraglomerular pressure and renal blood flow &rarr; renal ischemia.'),
]
prtr = ''
for i, (c, e) in enumerate(pr):
    bgc = CREAM if i % 2 == 0 else CREAM2
    prtr += f'''<tr style="background:{bgc};">
      <td style="padding:8px 10px;border:1px solid #C9AC85;width:38%;color:{DEEP};">{c}</td>
      <td style="padding:8px 10px;border:1px solid #C9AC85;color:{INK};">{e}</td>
    </tr>'''
s7 = content(f'''
<table style="width:100%;border-collapse:collapse;font-size:13px;">
  <tr style="background:{BROWN};color:{ON_DARK};">
    <th style="padding:8px 10px;border:1px solid {BROWN};text-align:left;">Category</th>
    <th style="padding:8px 10px;border:1px solid {BROWN};text-align:left;">Causes</th>
  </tr>
  {prtr}
</table>
<div style="height:10px;"></div>
{note('<b>ACEIs / ARBs</b> (efferent arteriole vasodilatation) &rarr; decreased intraglomerular pressure &amp; renal blood flow &rarr; <b style="color:' + DANGER + ';">renal ischemia</b> &mdash; a classic pre-renal mechanism.')}
''')
write_slide(7, hdr('03', 'Causes &mdash; 1. Pre-renal Causes') + s7)

# =====================================================================
# SLIDE 8 — Intra-renal causes
# =====================================================================
s8 = content(f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  <div style="grid-column:1 / span 2;">
    {card('<b>1. ATN &mdash; Acute Tubular Necrosis</b>', ul([
      '<b style="color:' + DANGER + ';">a. Hemodynamic:</b> cardiovascular surgery, sepsis, prolonged pre-renal cause.',
      '<b style="color:' + DANGER + ';">b. Toxic:</b> antimicrobials, iodide contrast agents, immunosuppression or antineoplastic agents, organic solvents, heavy metals, and radiation.',
      '<b style="color:' + DANGER + ';">c. Intratubular deposits:</b> Acute UA nephropathy, myeloma, severe hypercalcemia, primary oxalosis, sulfadiazine.',
      '<b style="color:' + DANGER + ';">d. Organic pigments (endogenous nephrotoxins):</b> myoglobin (rhabdomyolysis), hemoglobinuria (intravascular hemolysis).',
    ], 12.5), accent=DANGER, pad='14px 20px')}
  </div>
  <div>{card('<b>2. Acute GN</b>', '<p style="font-size:14px;color:' + INK + ';margin:0;">e.g. RPGN.</p>', accent=BROWN)}</div>
  <div>{card('<b>3. Acute interstitial nephritis</b>', '<p style="font-size:14px;color:' + INK + ';margin:0;">Drug / infection mediated tubular-interstitial inflammation.</p>', accent=BROWN)}</div>
</div>
<div style="height:10px;"></div>
{card('<b>4. Renal vascular occlusion</b>', '<p style="font-size:14px;color:' + INK + ';margin:0;">Arterial / venous thrombosis, vasculitis, cortical necrosis.</p>', accent=OLIVE, bg=CREAM2)}
''')
write_slide(8, hdr('03', 'Causes &mdash; 2. Intra-renal (Intrinsic) Causes') + s8)

# =====================================================================
# SLIDE 9 — Post-renal causes
# =====================================================================
post = [
    ('1. Congenital anomalies', 'ureterocele, bladder diverticulosis, post-urethral valves, neurogenic bladder.'),
    ('2. Acquired uropathies', 'BPH, ureterolithiasis, papillary necrosis, ureteral ligation.'),
    ('3. Malignant disease', 'prostate, bladder, cervix, colon.'),
    ('4. Gynecologic non-neoplastic', 'uterine prolapse, endometriosis.'),
    ('5. Drugs', 'sulfonamides, aminocaproic acid.'),
    ('6. Infections', 'schistosomiasis, TB, candidiasis, aspergillosis, actinomycosis.'),
    ('7. Others', 'accidental urethral catheter occlusion.'),
]
posthtml = ''
for t, e in post:
    posthtml += f'''<div style="display:flex;gap:10px;align-items:flex-start;background:{CREAM};border-radius:8px;padding:8px 14px;border-left:4px solid {BROWN};margin-bottom:8px;">
      <p style="font-size:14px;color:{INK};margin:0;line-height:1.4;"><b style="color:{CARAMEL};">{t}:</b> {e}</p>
    </div>'''
s9 = content(posthtml + f'<div style="height:6px;"></div>' + warn('Nearly all cases of <b>ICU-associated AKI</b> result from <b>more than a single insult</b>.'))
write_slide(9, hdr('03', 'Causes &mdash; 3. Post-renal Causes') + s9)

# =====================================================================
# SLIDE 10 — Section divider 03 Clinical Manifestations
# =====================================================================
write_slide(10, divider('03', 'Clinical Manifestations', 'Oliguria / Anuria &middot; Manifestations of loss of kidney function'))

# =====================================================================
# SLIDE 11 — Oliguria / Anuria
# =====================================================================
s11 = content(f'''
{card('<b>1. Oliguria / Anuria</b>', f'''
<ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:14px;line-height:1.5;">
  <li><b style="color:{DANGER};">Oliguria</b> (&lt;300 ml/day, &lt; 5 ml/kg/day or 0.5 ml/kg/h) or anuria.</li>
  <li>Oliguria is significantly associated with the occurrence of AKI. <b style="color:{DANGER};">Oliguria alone is the best predictor of AKI.</b></li>
  <li>However, <b style="color:{RUST};">about 50% or more of all cases of AKI are non-oliguric</b>. Thus, the maintenance of normal urine output does <b style="color:{DANGER};">not</b> provide assurance to the clinician that GFR is normal.</li>
</ul>
''', accent=DANGER)}
<div style="height:12px;"></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card('<b>Oliguria</b>', '<p style="font-size:14px;color:' + INK + ';margin:0;">&lt; 300 ml/day &middot; &lt; 5 ml/kg/day &middot; 0.5 ml/kg/h<br><b style="color:' + DANGER + ';">Best predictor of AKI</b></p>', accent=AMBER, bg=CREAM2)}
  {card('<b>Non-oliguric AKI</b>', '<p style="font-size:14px;color:' + INK + ';margin:0;">&ge; 50% of cases &mdash; <b style="color:' + DANGER + ';">normal urine output does not exclude AKI</b></p>', accent=AMBER, bg=CREAM2)}
</div>
''')
write_slide(11, hdr('04', 'Clinical Manifestations &mdash; 1. Oliguria / Anuria') + s11)

# =====================================================================
# SLIDE 12 — Causes of anuric AKI
# =====================================================================
s12 = content(f'''
{card('<b>Causes of anuric AKI</b>', f'''
<ol style="margin:0;padding:0 0 0 20px;color:{INK};font-size:14px;line-height:1.5;">
  <li style="margin-bottom:8px;"><b style="color:{DANGER};">Complete UT obstruction</b> &mdash; <b style="color:{DANGER};">90% of cases</b>.</li>
  <li style="margin-bottom:4px;"><b style="color:{RUST};">Renal vascular occlusion;</b>
    <ul style="margin:2px 0 6px 0;padding:0 0 0 18px;font-size:13px;line-height:1.45;">
      <li>Renal artery thrombosis.</li>
      <li>Renal vein thrombosis.</li>
      <li>Cortical necrosis &mdash; sepsis, obstetric accidents, DIC.</li>
      <li>Renal vasculitis and RPGN.</li>
    </ul>
  </li>
  <li><b style="color:{RUST};">AKI complicating</b> &mdash; sepsis, heat stroke and rhabdomyolysis.</li>
</ol>
''', accent=DANGER)}
<div style="height:12px;"></div>
{card('<b>Remember</b>', '<p style="font-size:14px;color:' + INK + ';margin:0;">Anuric AKI is rare with intrinsic causes &mdash; always think of <b style="color:' + DANGER + ';">obstruction</b> (90%) and <b style="color:' + DANGER + ';">vascular occlusion</b> first.</p>', accent=AMBER, bg=CREAM2)}
''')
write_slide(12, hdr('04', 'Clinical Manifestations &mdash; Causes of Anuric AKI') + s12)

# =====================================================================
# SLIDE 13 — Manifestations of loss of kidney function
# =====================================================================
s13 = content(f'''
{card('<b>2. Manifestations of loss of kidney function</b>', f'''
<p style="font-size:14px;color:{INK};margin:0 0 8px 0;line-height:1.45;">On rare occasions, when frequent monitoring of urine output or serum creatinine concentration is <b style="color:{RUST};">not being done</b> (ambulatory or hospital ward populations), AKI will initially come by one or more of the clinical manifestations of loss of kidney function; e.g.</p>
<ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:14px;line-height:1.5;">
  <li style="margin-bottom:6px;"><b style="color:{DANGER};">Volume overload</b> &mdash; e.g. peripheral edema, weight gain, shortness of breath.</li>
  <li><b style="color:{DANGER};">Rarely;</b>
    <ul style="margin:3px 0 0 0;padding:0 0 0 18px;font-size:13px;line-height:1.5;">
      <li>GIT symptoms &mdash; e.g. anorexia, nausea, vomiting, diarrhea.</li>
      <li>Flank / back pain &mdash; due to edematous kidneys or UT obstruction.</li>
      <li>Altered mental status or seizures.</li>
      <li>Anemia and bleeding.</li>
      <li>Other symptoms.</li>
    </ul>
  </li>
</ul>
''', accent=DANGER)}
''')
write_slide(13, hdr('04', 'Clinical Manifestations &mdash; Loss of Kidney Function') + s13)

# =====================================================================
# SLIDE 14 — Section divider 04 Investigations
# =====================================================================
write_slide(14, divider('04', 'Investigations', 'Urine &middot; Blood &amp; Serology &middot; Bladder pressure &middot; US/Doppler &middot; Biopsy &middot; Biomarkers'))

# =====================================================================
# SLIDE 15 — Urine examination I
# =====================================================================
s15 = content(f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card('<b>Urine volume / color</b>', ul([
    '<b style="color:' + DANGER + ';">Urine volume / 24 h.</b>',
    '<b style="color:' + DANGER + ';">Urine color:</b> Reddish brown or cola-colored urine &rarr; myoglobin or Hb, especially in the setting of a <b>positive dipstick and no red blood cells</b> on microscopic examination.',
  ], 13), accent=DANGER)}
  {card('<b>Urinary red blood cells</b>', ul([
    '<b style="color:' + RUST + ';">Eumorphic</b> (normal shape) &rarr; bleeding along the collecting system.',
    '<b style="color:' + RUST + ';">Dysmorphic</b> or red cell casts &rarr; <b style="color:' + DANGER + ';">GN</b>.',
  ], 13), accent=BROWN)}
</div>
<div style="height:12px;"></div>
{card('<b>Urinary casts</b>', f'''
<ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:13px;line-height:1.5;">
  <li><b style="color:{DANGER};">Muddy brown casts &rarr; ATN</b> &mdash; the presence of tubular cell casts and oxalate crystals supports the diagnosis of ATN.</li>
  <li><b style="color:{RUST};">White blood cell casts or white blood cells</b> &rarr; pyelonephritis or acute interstitial nephritis (AIN) &mdash; the presence of <b>urine eosinophils</b> is helpful in establishing the diagnosis of AIN.</li>
</ul>
<p style="font-size:13px;color:{INK};margin:8px 0 0 0;"><b style="color:{CARAMEL};">Proteinuria.</b></p>
''', accent=RUST, bg=CREAM2)}
''')
write_slide(15, hdr('05', 'Investigations &mdash; 1. Urine Examination') + s15)

# =====================================================================
# SLIDE 16 — FENa
# =====================================================================
s16 = content(f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card('<b>Formula</b>', f'''
    <p style="font-size:18px;font-weight:700;color:{DEEP};margin:0 0 4px 0;text-align:center;">FENa = (UNa / PNa) / (Ucr / Pcr) &times; 100</p>
    <p style="font-size:12px;color:{SOFT};margin:0;text-align:center;">[U = urine, P = plasma, Na = sodium, cr = creatinine]</p>
  ''', accent=BROWN)}
  {card('<b>Values</b>', f'''
    <p style="font-size:14px;color:{INK};margin:0 0 5px 0;"><b style="color:{OLIVE};">&lt; 1%</b> &rarr; <b style="color:{OLIVE};">pre-renal AKI</b></p>
    <p style="font-size:14px;color:{INK};margin:0;"><b style="color:{DANGER};">&gt; 1%</b> &rarr; <b style="color:{DANGER};">ATN</b></p>
  ''', accent=DANGER)}
</div>
<div style="height:10px;"></div>
{warn('FENa &gt; 1% (<b>ATN</b>) exceptions &mdash; ATN caused by: <b>radio-contrast, severe burns, acute GN and rhabdomyolysis</b>.')}
<div style="height:10px;"></div>
{card('<b>N.B.</b>', f'''
<ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:13px;line-height:1.5;">
  <li>FENa is a valuable test for helping to detect <b style="color:{RUST};">extreme renal avidity for Na</b> in conditions such as hepato-renal syndrome (HRS).</li>
  <li>It is useful in AKI <b style="color:{DANGER};">only in the presence of oliguria</b>. It <b style="color:{DANGER};">cannot</b> be used as an indication of AKI in patients with: non-oliguric states, GN, those receiving diuretics, and liver cirrhosis.</li>
</ul>
''', accent=AMBER, bg=CREAM2)}
''')
write_slide(16, hdr('05', 'Investigations &mdash; Fractional Excretion of Sodium (FENa)') + s16)

# =====================================================================
# SLIDE 17 — FE urea
# =====================================================================
s17 = content(f'''
{card('<b>Formula</b>', f'''
  <p style="font-size:18px;font-weight:700;color:{DEEP};margin:0 0 4px 0;text-align:center;">FEur = (Uur / Pur) / (Ucr / Pcr) &times; 100</p>
  <p style="font-size:12px;color:{SOFT};margin:0;text-align:center;">[U = urine, P = plasma, ur = urea, cr = creatinine]</p>
''', accent=BROWN)}
<div style="height:12px;"></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card('<b>When to use</b>', f'''
    <p style="font-size:14px;color:{INK};margin:0;line-height:1.5;">FEurea is used in patients who are <b style="color:{DANGER};">receiving diuretics</b>, since <b style="color:{RUST};">urea transport is not affected by diuretics</b>.</p>
  ''', accent=BROWN)}
  {card('<b>Interpretation</b>', f'''
    <p style="font-size:16px;color:{INK};margin:0 0 4px 0;"><b style="color:{DANGER};">&lt; 35%</b> &rarr; suggestive of a <b style="color:{DANGER};">pre-renal</b> state.</p>
  ''', accent=DANGER)}
</div>
<div style="height:12px;"></div>
{note('FEurea is the preferred index in <b>diuretic-exposed</b> patients, where FENa loses its validity (see FENa N.B.).')}
''')
write_slide(17, hdr('05', 'Investigations &mdash; Fractional Excretion of Urea (FEurea)') + s17)

# =====================================================================
# SLIDE 18 — Blood examination & serology
# =====================================================================
s18 = content(f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  <div>
    {card('<b>Renal function</b>', f'''
      <ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:13px;line-height:1.5;">
        <li>S. creatinine and blood urea.</li>
        <li>Increased serum creatinine concentration is a <b style="color:{DANGER};">better surrogate marker for GFR</b> than BUN concentration.</li>
        <li><b style="color:{RUST};">BUN / creatinine ratio:</b>
          <ul style="margin:2px 0 0 0;padding:0 0 0 16px;">
            <li><b style="color:{OLIVE};">20/1</b> &rarr; <b style="color:{OLIVE};">pre-renal AKI</b></li>
            <li><b style="color:{DANGER};">&lt; 20/1</b> &rarr; <b style="color:{DANGER};">intrinsic or post-renal AKI</b></li>
          </ul>
        </li>
      </ul>
    ''', accent=BROWN)}
    <div style="height:10px;"></div>
    {card('<b>Biomarkers of specific causes</b>', f'''
      <ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:13px;line-height:1.5;">
        <li>Increased serum uric acid &rarr; <b style="color:{DANGER};">tumor lysis syndrome (TLS)</b>.</li>
        <li>Increased serum LDH &rarr; <b style="color:{RUST};">renal infarction</b>.</li>
        <li>Schistocytes in blood film &rarr; <b style="color:{DANGER};">HUS or TTP</b>.</li>
        <li>Increased rouleaux formation &rarr; suggests <b style="color:{RUST};">multiple myeloma</b>.</li>
        <li>Myoglobin or free Hb &rarr; <b style="color:{DANGER};">pigment nephropathy</b>.</li>
      </ul>
    ''', accent=OLIVE, bg=CREAM2)}
  </div>
  <div>
    {card('<b>Serology</b>', f'''
      <p style="font-size:14px;color:{INK};margin:0 0 5px 0;">Complement levels, ANA, ANCA, Anti-GBM Ab., HBV &amp; HCV, ASOT.</p>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:8px;">
        <div style="background:{CREAM2};border-radius:6px;padding:8px 10px;border-top:3px solid {BROWN};"><p style="font-size:12px;color:{INK};margin:0;"><b style="color:{CARAMEL};">ANA / ANCA</b><br>vasculitis / lupus</p></div>
        <div style="background:{CREAM2};border-radius:6px;padding:8px 10px;border-top:3px solid {BROWN};"><p style="font-size:12px;color:{INK};margin:0;"><b style="color:{CARAMEL};">Anti-GBM</b><br>Goodpasture / RPGN</p></div>
        <div style="background:{CREAM2};border-radius:6px;padding:8px 10px;border-top:3px solid {BROWN};"><p style="font-size:12px;color:{INK};margin:0;"><b style="color:{CARAMEL};">Complement</b><br>low in immune GN</p></div>
        <div style="background:{CREAM2};border-radius:6px;padding:8px 10px;border-top:3px solid {BROWN};"><p style="font-size:12px;color:{INK};margin:0;"><b style="color:{CARAMEL};">HBV &middot; HCV &middot; ASOT</b><br>infection-related GN</p></div>
      </div>
    ''', accent=BROWN)}
  </div>
</div>
''')
write_slide(18, hdr('05', 'Investigations &mdash; 2. Blood Examination &amp; Serology') + s18)

# =====================================================================
# SLIDE 19 — Bladder pressure + US/Doppler
# =====================================================================
s19 = content(f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card('<b>3. Bladder pressure</b>', f'''
    <p style="font-size:13px;color:{SOFT};margin:0 0 7px 0;">A measure of intra-abdominal pressure;</p>
    <ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:13px;line-height:1.6;">
      <li><b style="color:{OLIVE};">&lt; 10 mmHg</b> &rarr; <b style="color:{OLIVE};">normal</b>.</li>
      <li><b style="color:{RUST};">&gt; 10 mmHg</b> &rarr; <b style="color:{RUST};">abnormal</b>.</li>
      <li><b style="color:{DANGER};">15 &ndash; 25 mmHg</b> &rarr; <b style="color:{DANGER};">risk of abdominal compartment syndrome and AKI</b>.</li>
    </ul>
  ''', accent=BROWN)}
  {card('<b>4. Ultrasound and Doppler study</b>', f'''
    <ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:13px;line-height:1.5;">
      <li>US is useful for evaluating <b style="color:{RUST};">existing renal disease</b> and <b style="color:{RUST};">obstruction</b> of the urinary collecting system. <b style="color:{DANGER};">Small kidney &rarr; suggests CKD</b>.</li>
      <li style="margin-top:6px;"><b style="color:{CARAMEL};">Doppler:</b> detects the presence and nature of renal blood flow.
        <ul style="margin:2px 0 0 0;padding:0 0 0 16px;">
          <li>Reduced in pre-renal and renal AKI &rarr; <b style="color:{SOFT};">of little diagnostic value</b> in these conditions.</li>
          <li>Useful in <b style="color:{DANGER};">thrombo-embolic or renal vascular disease</b>.</li>
        </ul>
      </li>
    </ul>
  ''', accent=OLIVE, bg=CREAM2)}
</div>
''')
write_slide(19, hdr('05', 'Investigations &mdash; Bladder Pressure &amp; Ultrasound/Doppler') + s19)

# =====================================================================
# SLIDE 20 — Renal biopsy + Biomarkers
# =====================================================================
s20 = content(f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card('<b>5. Renal biopsy</b>', f'''
    <p style="font-size:14px;color:{INK};margin:0;line-height:1.5;">Indicated if the cause of <b style="color:{DANGER};">intrinsic</b> renal AKI is <b style="color:{RUST};">unclear</b> after <b style="color:{RUST};">exclusion of pre- and post-renal causes</b>.</p>
  ''', accent=DANGER)}
  {card('<b>6. Biomarkers for AKI</b>', f'''
    <p style="font-size:14px;color:{INK};margin:0 0 8px 0;">Current biomarker:</p>
    <div style="background:{CREAM2};border-radius:8px;padding:10px 14px;border-top:4px solid {AMBER};">
      <p style="font-size:15px;color:{DEEP};margin:0;font-weight:700;">1. Serum creatinine and eGFR</p>
    </div>
  ''', accent=AMBER, bg=CREAM2)}
</div>
<div style="height:12px;"></div>
{warn('Renal biopsy is reserved for <b>unexplained intrinsic AKI</b> &mdash; it distinguishes ATN from AIN, GN, and vascular causes.')}
''')
write_slide(20, hdr('05', 'Investigations &mdash; Renal Biopsy &amp; Biomarkers') + s20)

# =====================================================================
# SLIDE 21 — Section divider 05 Treatment
# =====================================================================
write_slide(21, divider('05', 'Principles of Treatment', 'Supportive care is the mainstay &mdash; no definitive therapy exists'))

# =====================================================================
# SLIDE 22 — Treatment A & B
# =====================================================================
s22 = content(f'''
{card('', f'''
<p style="font-size:14px;color:{INK};margin:0;line-height:1.45;"><b style="color:{DANGER};">Currently, there is no definitive therapy for AKI</b> and <b style="color:{RUST};">supportive care is the mainstay of management</b> regardless of the etiology. However, the following issues require attention.</p>
''', accent=DANGER)}
<div style="height:12px;"></div>
{card('<b>A. First</b>', f'''
<p style="font-size:14px;color:{INK};margin:0;line-height:1.45;"><b style="color:{RUST};">Recognition of the etiology of AKI</b> and underlying <b style="color:{RUST};">risk factors</b> that predispose patients to AKI &mdash; e.g. DM, CKD, hypertension, cardiac or liver dysfunction &mdash; should be <b style="color:{DANGER};">evaluated and managed</b>.</p>
''', accent=BROWN)}
<div style="height:12px;"></div>
{card('<b>B. Second</b>', f'''
<p style="font-size:14px;color:{INK};margin:0;line-height:1.45;"><b style="color:{RUST};">Monitoring the serum creatinine and urine output</b> to perform <b style="color:{DANGER};">staging</b>.</p>
''', accent=BROWN)}
''')
write_slide(22, hdr('06', 'Principles of Treatment &mdash; A &amp; B') + s22)

# =====================================================================
# SLIDE 23 — Treatment C
# =====================================================================
s23 = content(f'''
{card('<b>C. Third &mdash; Identification and careful management of comorbid conditions</b>', f'''
<p style="font-size:13px;color:{SOFT};margin:0 0 8px 0;">Comorbidities can influence the outcome of AKI, e.g.;</p>
<ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:14px;line-height:1.5;">
  <li style="margin-bottom:7px;"><b style="color:{DANGER};">Tight glucose control</b> by intensive insulin therapy.</li>
  <li style="margin-bottom:7px;"><b style="color:{DANGER};">Control of hyperkalemia.</b></li>
  <li style="margin-bottom:7px;">Use of <b style="color:{RUST};">nephrotoxic drugs</b> and planned procedures (e.g. imaging study and surgery) have to be <b style="color:{RUST};">balanced against their potential benefits</b>.</li>
  <li style="margin-bottom:7px;">Maintain renal perfusion by: <b style="color:{RUST};">volume resuscitation, inotropic or vasopressor support</b> to maintain hemodynamic stability &rarr; enhancing kidney recovery and preventing further kidney damage.</li>
  <li><b style="color:{CARAMEL};">Small dose of dopamine</b> (1&ndash;3 mcg/kg/min) causes: selective dilatation of the renal vasculatures, enhancing renal perfusion, and reducing sodium absorption &rarr; enhances urine flow that helps to prevent tubular cast obstruction. <b style="color:{DANGER};">However, there is controversy</b> in the use of small-dose dopamine in treating AKI.</li>
</ul>
''', accent=BROWN)}
''')
write_slide(23, hdr('06', 'Principles of Treatment &mdash; C. Comorbid Conditions') + s23)

# =====================================================================
# SLIDE 24 — Treatment D
# =====================================================================
s24 = content(f'''
{card('<b>D. Fourth &mdash; Renal replacement therapy (RRT)</b>', f'''
<ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:14px;line-height:1.5;">
  <li style="margin-bottom:8px;"><b style="color:{RUST};">There is no current consensus</b> on the indications of RRT for AKI. Moreover, <b style="color:{RUST};">RRT by itself may introduce multiple complications</b> in the patient&rsquo;s management.</li>
</ul>
''', accent=BROWN)}
<div style="height:12px;"></div>
{card('<b>Absolute indications for dialysis in AKI include;</b>', f'''
<ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:14px;line-height:1.55;">
  <li style="margin-bottom:7px;"><b style="color:{DANGER};">Clinically apparent signs and symptoms of uremia.</b></li>
  <li style="margin-bottom:7px;">Management of <b style="color:{DANGER};">refractory hyperkalemia, acidosis, and hypervolemia</b>.</li>
  <li>Many nephrologists initiate dialysis <b style="color:{RUST};">empirically for BUN &gt; 100 mg/dl</b>.</li>
</ul>
''', accent=DANGER)}
''')
write_slide(24, hdr('06', 'Principles of Treatment &mdash; D. Renal Replacement Therapy') + s24)

# =====================================================================
# SLIDE 25 — File 10 opener / section divider
# =====================================================================
topics25 = f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;max-width:720px;">
  <div style="background:{BROWN};border-radius:8px;padding:8px 14px;"><p style="font-size:14px;color:{ON_DARK};margin:0;font-weight:700;">1. Contrast-Induced Nephropathy (CIN)</p></div>
  <div style="background:{BROWN};border-radius:8px;padding:8px 14px;"><p style="font-size:14px;color:{ON_DARK};margin:0;font-weight:700;">2. Tumor Lysis Syndrome (TLS)</p></div>
  <div style="background:{BROWN};border-radius:8px;padding:8px 14px;"><p style="font-size:14px;color:{ON_DARK};margin:0;font-weight:700;">3. AKI in Pregnancy</p></div>
  <div style="background:{BROWN};border-radius:8px;padding:8px 14px;"><p style="font-size:14px;color:{ON_DARK};margin:0;font-weight:700;">4. AKI in Rhabdomyolysis</p></div>
</div>
'''
write_slide(25, divider('10', 'AKI in Special Situations', 'Chapter 10 &mdash; Principles of Nephrology', topics25))

# =====================================================================
# SLIDE 26 — Divider: CIN
# =====================================================================
write_slide(26, divider('1', 'Contrast-Induced Nephropathy (CIN)', 'Definition &middot; Risk factors &middot; Pathogenesis &middot; Diagnosis &middot; Prevention &amp; Treatment &middot; Prognosis'))

# =====================================================================
# SLIDE 27 — CIN Definition + Risk factors
# =====================================================================
s27 = content(f'''
{card('<b>Definition</b>', f'''
<p style="font-size:14px;color:{INK};margin:0;line-height:1.45;">CIN is acute kidney injury characterized by <b style="color:{DANGER};">rise of serum creatinine of &ge; 0.5 mg/dl or 25% above the baseline</b> within <b style="color:{DANGER};">48 hours after contrast administration</b>.</p>
''', accent=DANGER)}
<div style="height:12px;"></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card('<b>Patient-related factors</b>', f'''
    <ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:12.5px;line-height:1.5;">
      <li style="margin-bottom:4px;"><b style="color:{DANGER};">Pre-existing CKD</b> &mdash; the <b style="color:{DANGER};">most potent risk factor</b>. Nearly <b style="color:{DANGER};">60%</b> of patients developing CIN have CKD, and the incidence of CIN <b style="color:{RUST};">parallels the severity</b> of preexisting renal impairment.</li>
      <li>Diabetes mellitus</li>
      <li>Congestive heart failure</li>
      <li>Hypotension</li>
      <li>Volume depletion</li>
      <li>Old age</li>
    </ul>
  ''', accent=BROWN, pad='12px 16px 15px 16px')}
  {card('<b>Contrast-related factors</b>', f'''
    <ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:13px;line-height:1.5;">
      <li>Large volume (dose) of <b style="color:{RUST};">parenteral contrast material</b>.</li>
      <li>The <b style="color:{RUST};">type of contrast material</b>, especially its <b style="color:{DANGER};">osmolarity</b> &mdash; the incidence of CIN is <b style="color:{DANGER};">high with the high osmolar contrast materials</b>.</li>
    </ul>
  ''', accent=OLIVE, bg=CREAM2)}
</div>
''')
write_slide(27, hdr('1', 'CIN &mdash; Definition &amp; Risk Factors') + s27)

# =====================================================================
# SLIDE 28 — CIN Pathogenesis
# =====================================================================
s28 = content(f'''
<p style="font-size:13px;color:{SOFT};margin:0 0 8px 0;font-style:italic;">Several mechanisms have been proposed.</p>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card('<b>1. Renal ischemia</b>', f'''
    <p style="font-size:13px;color:{INK};margin:0 0 5px 0;">Contrast media induce renal ischemia by <b style="color:{DANGER};">two mechanisms</b>:</p>
    <ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:13px;line-height:1.45;">
      <li>a. Production of <b style="color:{RUST};">vasoconstrictive compounds</b> as endothelin and adenosine.</li>
      <li>b. <b style="color:{RUST};">Increased oxygen utilization</b> in the renal tubules.</li>
    </ul>
  ''', accent=DANGER)}
  {card('<b>2. Hyperosmolarity</b>', f'''
    <p style="font-size:13px;color:{INK};margin:0 0 5px 0;">Intra-tubular hyperosmolarity causes:</p>
    <ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:13px;line-height:1.45;">
      <li>a. <b style="color:{RUST};">Increased intra-tubular hydrostatic pressure</b> which decreases glomerular filtration.</li>
      <li>b. <b style="color:{RUST};">Increased tubular cell apoptosis</b>.</li>
    </ul>
  ''', accent=OLIVE, bg=CREAM2)}
  {card('<b>3. Generation of oxygen free radicals</b>', '<p style="font-size:13px;color:' + INK + ';margin:0;">Oxidative injury to tubular cells.</p>', accent=BROWN)}
  {card('<b>4. Direct cellular toxicity</b>', '<p style="font-size:13px;color:' + INK + ';margin:0;">Direct cytotoxic effect of contrast on tubular epithelium.</p>', accent=BROWN)}
</div>
''')
write_slide(28, hdr('1', 'CIN &mdash; Pathogenesis') + s28)

# =====================================================================
# SLIDE 29 — CIN Diagnosis
# =====================================================================
s29 = content(f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card('<b>Symptoms and signs</b>', f'''
    <ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:13px;line-height:1.5;">
      <li>In the <b style="color:{OLIVE};">vast majority</b> of patients, there are <b style="color:{OLIVE};">no symptoms or signs</b>.</li>
      <li>In a <b style="color:{RUST};">smaller subset</b>: oliguria with or without volume overload.</li>
      <li><b style="color:{DANGER};">Rarely</b>: a patient with CIN may present with symptoms and signs of <b style="color:{DANGER};">uremia</b>.</li>
    </ul>
  ''', accent=BROWN)}
  {card('<b>Laboratory &mdash; serum creatinine</b>', f'''
    <ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:13px;line-height:1.5;">
      <li><b style="color:{OLIVE};">Majority:</b> creatinine begins to rise <b style="color:{RUST};">24&ndash;48 h</b> after exposure, peaks within <b style="color:{RUST};">3&ndash;5 days</b>, returns to baseline within <b style="color:{RUST};">7&ndash;10 days</b>.</li>
      <li><b style="color:{DANGER};">More severe cases:</b> does not peak until <b style="color:{DANGER};">5&ndash;10 days</b> and may be accompanied by oliguria and <b style="color:{DANGER};">requirement for dialysis</b>.</li>
    </ul>
  ''', accent=OLIVE, bg=CREAM2)}
</div>
<div style="height:12px;"></div>
{card('<b>Imaging</b>', '<p style="font-size:14px;color:' + INK + ';margin:0;">To <b style="color:' + DANGER + ';">exclude other causes of AKI</b>.</p>', accent=AMBER, bg=CREAM2)}
''')
write_slide(29, hdr('1', 'CIN &mdash; Diagnosis') + s29)

# =====================================================================
# SLIDE 30 — CIN Management
# =====================================================================
s30 = content(f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card('<b>Prevention</b>', f'''
    <ol style="margin:0;padding:0 0 0 20px;color:{INK};font-size:13px;line-height:1.5;">
      <li>Use <b style="color:{RUST};">non-iodinated</b> contrast media.</li>
      <li>Use <b style="color:{RUST};">low osmolar</b> contrast media.</li>
      <li><b style="color:{DANGER};">Minimize contrast volume (dose)</b> &mdash; formula based on body weight and baseline S. creatinine:<br><span style="font-size:12px;font-weight:700;color:{DEEP};">Volume of contrast = 5 ml of contrast/kg of BW (max 300 ml) / S. creatinine mg/dl</span></li>
      <li><b style="color:{RUST};">Space between</b> contrast administrations.</li>
      <li><b style="color:{RUST};">Avoid nephrotoxic drugs</b> before and after the procedure.</li>
      <li><b style="color:{DANGER};">Adequate hydration</b> before, during, and after the procedure.</li>
      <li>Use of <b style="color:{CARAMEL};">N-acetyl cysteine</b> &mdash; it is <b style="color:{DANGER};">unclear whether it prevents CIN</b> as studies are conflicting.</li>
    </ol>
  ''', accent=OLIVE, bg=CREAM2)}
  {card('<b>Treatment</b>', f'''
    <p style="font-size:13px;color:{INK};margin:0 0 6px 0;"><b style="color:{DANGER};">No specific therapy for CIN once it occurs</b> &mdash; the best strategy is one of <b style="color:{RUST};">prevention</b>. However, once a patient develops CIN the following should be taken:</p>
    <ol style="margin:0;padding:0 0 0 20px;color:{INK};font-size:13px;line-height:1.5;">
      <li>Manage fluid and electrolytes.</li>
      <li>Adjust medications that are eliminated by the kidney.</li>
      <li>Regular monitoring of electrolytes, S. creatinine and BUN.</li>
      <li>Dialysis as needed.</li>
    </ol>
  ''', accent=DANGER)}
</div>
''')
write_slide(30, hdr('1', 'CIN &mdash; Prevention &amp; Treatment') + s30)

# =====================================================================
# SLIDE 31 — CIN Prognosis
# =====================================================================
s31 = content(f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card('<b>Most patients</b>', f'''
    <p style="font-size:15px;color:{INK};margin:0;line-height:1.5;"><b style="color:{OLIVE};">Complete recovery</b> of renal function <b style="color:{OLIVE};">usually occurs</b>.</p>
  ''', accent=OLIVE)}
  {card('<b>Small minority</b>', f'''
    <p style="font-size:15px;color:{INK};margin:0;line-height:1.5;">A small minority of patients may go on to <b style="color:{DANGER};">CKD</b>.</p>
  ''', accent=DANGER)}
</div>
<div style="height:14px;"></div>
{note('CIN is <b>largely reversible</b> &mdash; the creatinine curve typically returns to baseline within 7&ndash;10 days.')}
''')
write_slide(31, hdr('1', 'CIN &mdash; Prognosis') + s31)

# =====================================================================
# SLIDE 32 — Divider: TLS
# =====================================================================
write_slide(32, divider('2', 'Tumor Lysis Syndrome (TLS)', 'Definition &middot; Patients at risk &middot; Clinical features &middot; Diagnosis &amp; DD &middot; Management &middot; Prognosis'))

# =====================================================================
# SLIDE 33 — TLS Definition + Patients at risk
# =====================================================================
s33 = content(f'''
{card('<b>Definition</b>', f'''
<p style="font-size:14px;color:{INK};margin:0;line-height:1.45;">It is an <b style="color:{DANGER};">acute critical illness</b> characterized by <b style="color:{DANGER};">severe hyperuricemia, hyperphosphatemia, hyperkalemia, hypocalcemia, and AKI</b> seen in patients with <b style="color:{RUST};">rapidly growing cancers</b> (especially <b style="color:{RUST};">Burkitt&rsquo;s lymphomas</b>) after administration of chemotherapeutic agents.</p>
<p style="font-size:13px;color:{INK};margin:7px 0 0 0;line-height:1.4;">The acute electrolyte disorders are due to <b style="color:{RUST};">massive sudden death of tumor cells</b> &rarr; release of intra-cellular electrolytes (uric acid, phosphorus, and potassium). <b style="color:{DANGER};">Hypocalcemia is secondary to hyperphosphatemia</b> to maintain calcium-phosphorus balance.</p>
''', accent=DANGER)}
<div style="height:12px;"></div>
{card('<b>Patients at risk</b>', f'''
<ol style="margin:0;padding:0 0 0 20px;color:{INK};font-size:14px;line-height:1.55;">
  <li>Hematological and lymphoproliferative malignancy with <b style="color:{DANGER};">marked elevation of serum LDH</b>.</li>
  <li>Volume depletion.</li>
  <li><b style="color:{RUST};">Acidic urinary pH</b>.</li>
  <li>Patients with <b style="color:{DANGER};">CKD</b> &mdash; because <b style="color:{RUST};">renal clearance is the primary mechanism</b> of excretion of UA and phosphates.</li>
</ol>
''', accent=BROWN)}
''')
write_slide(33, hdr('2', 'TLS &mdash; Definition &amp; Patients at Risk') + s33)

# =====================================================================
# SLIDE 34 — TLS Clinical features + Diagnosis
# =====================================================================
s34 = content(f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card('<b>Clinical features</b>', f'''
    <p style="font-size:13px;color:{INK};margin:0;line-height:1.5;">Varying degrees of AKI due to <b style="color:{DANGER};">intra-tubular precipitation of UA</b> (acute UA nephropathy) and/or <b style="color:{DANGER};">acute nephrocalcinosis</b> secondary to marked hyper-phosphatemia.</p>
    <p style="font-size:13px;color:{INK};margin:7px 0 0 0;line-height:1.5;"><b style="color:{RUST};">AKI is most marked during the induction of chemotherapy.</b></p>
  ''', accent=DANGER)}
  {card('<b>Diagnosis</b>', f'''
    <ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:13px;line-height:1.5;">
      <li>Any patient with a <b style="color:{RUST};">known or suspected malignancy</b>, especially <b style="color:{RUST};">Burkitt&rsquo;s lymphoma</b>, who presents with: <b style="color:{DANGER};">AKI, hyperuricemia, and elevated serum LDH</b> should be examined for TLS.</li>
      <li>The presence of concomitant <b style="color:{RUST};">volume depletion, hyperkalemia, hyperphosphatemia and hypocalcemia</b> strongly support the clinical diagnosis.</li>
    </ul>
  ''', accent=OLIVE, bg=CREAM2)}
</div>
''')
write_slide(34, hdr('2', 'TLS &mdash; Clinical Features &amp; Diagnosis') + s34)

# =====================================================================
# SLIDE 35 — TLS Differential diagnosis
# =====================================================================
s35 = content(f'''
{card('<b>Differential diagnosis &mdash; other causes of AKI in cancer patients including:</b>', f'''
<ol style="margin:0;padding:0 0 0 20px;color:{INK};font-size:14px;line-height:1.5;">
  <li style="margin-bottom:6px;">UT obstruction.</li>
  <li style="margin-bottom:6px;">Severe volume depletion.</li>
  <li style="margin-bottom:4px;"><b style="color:{RUST};">Parenchymal renal diseases;</b> e.g.
    <ul style="margin:2px 0 6px 0;padding:0 0 0 18px;font-size:13px;line-height:1.5;">
      <li>GN secondary to <b style="color:{DANGER};">cryoglobulinemia</b> or tumor-related Ag&ndash;Ab complexes.</li>
      <li>Vasculitis.</li>
      <li>Hypercalcemic nephropathy.</li>
      <li>Tumor infiltrating the kidney parenchyma.</li>
      <li><b style="color:{DANGER};">Myeloma kidney (cast nephropathy)</b>.</li>
      <li><b style="color:{DANGER};">Nephrotoxic drugs:</b> Methotrexate, cisplatinum, mitomycin C, IFN-&alpha;, antibiotics.</li>
    </ul>
  </li>
</ol>
''', accent=BROWN)}
''')
write_slide(35, hdr('2', 'TLS &mdash; Differential Diagnosis') + s35)

# =====================================================================
# SLIDE 36 — TLS Prevention
# =====================================================================
s36 = content(f'''
{card('<b>Prevention (prophylactic)</b>', f'''
<ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:14px;line-height:1.5;">
  <li style="margin-bottom:7px;"><b style="color:{DANGER};">Early identification of patients at risk.</b></li>
  <li>Institution of the following measures <b style="color:{RUST};">prior to anti-neoplastic drug therapy</b>;</li>
</ul>
<ol style="margin:8px 0 0 0;padding:0 0 0 20px;color:{INK};font-size:13px;line-height:1.55;">
  <li>Correct initial <b style="color:{RUST};">electrolyte and fluid disorders</b>.</li>
  <li>Maintain adequate <b style="color:{RUST};">hydration and urine output</b>.</li>
  <li><b style="color:{DANGER};">Alkalinize urine to pH &gt; 7.0</b> to enhance UA solubility and prevent precipitation.</li>
  <li>Give <b style="color:{RUST};">oral phosphate-binding antacids</b>.</li>
  <li><b style="color:{DANGER};">Allopurinol (300 mg/m&sup2;)</b> 1&ndash;2 days before chemotherapy.</li>
  <li>Correct any <b style="color:{RUST};">renal or pre-renal dysfunction</b>, if present.</li>
</ol>
''', accent=OLIVE)}
<div style="height:10px;"></div>
{warn('Urine alkalinization + allopurinol are the cornerstones of TLS prophylaxis before starting chemotherapy.')}
''')
write_slide(36, hdr('2', 'TLS &mdash; Prevention (Prophylactic)') + s36)

# =====================================================================
# SLIDE 37 — TLS Treatment
# =====================================================================
s37 = content(f'''
{card('<b>Treatment of established AKI</b>', f'''
<ol style="margin:0;padding:0 0 0 20px;color:{INK};font-size:13px;line-height:1.5;">
  <li style="margin-bottom:6px;">Administer <b style="color:{DANGER};">allopurinol, 600 mg/day</b>.</li>
  <li style="margin-bottom:6px;">Intravenous <b style="color:{RUST};">isotonic NaHCO&sup3;</b> at rate of <b style="color:{RUST};">200&ndash;300 ml/h</b> to expand volume, wash out the renal medulla, and alkalinize the urine.</li>
  <li style="margin-bottom:4px;"><b style="color:{DANGER};">Dialysis:</b> HD is <b style="color:{DANGER};">life-saving</b> in the management of TLS and should be considered for <b style="color:{DANGER};">every patient</b>. It is generally required during induction. The main goals of HD are to;
    <ul style="margin:2px 0 6px 0;padding:0 0 0 18px;font-size:12px;line-height:1.5;">
      <li>Decrease plasma levels of UA, phosphorus, and potassium.</li>
      <li>Restore volume overload, and</li>
      <li>Control of uremia.</li>
    </ul>
  </li>
  <li><b style="color:{RUST};">Post-chemotherapy measures:</b>
    <ul style="margin:2px 0 0 0;padding:0 0 0 18px;font-size:12px;line-height:1.5;">
      <li>Discontinue urine alkalinization when <b style="color:{DANGER};">UA homeostasis is achieved</b> to avoid <b style="color:{DANGER};">Ca&sup3;(PO&sup4;)&sup2; precipitation</b>.</li>
      <li>Treat <b style="color:{RUST};">symptomatic hypocalcemia</b> after correction of hyperphosphatemia.</li>
    </ul>
  </li>
</ol>
''', accent=DANGER)}
''')
write_slide(37, hdr('2', 'TLS &mdash; Treatment of Established AKI') + s37)

# =====================================================================
# SLIDE 38 — Divider: Rhabdomyolysis
# =====================================================================
write_slide(38, divider('3', 'AKI in Rhabdomyolysis', 'Definition &middot; Causes &middot; Pathogenesis &middot; Diagnosis &middot; Treatment &middot; Prognosis'))

# =====================================================================
# SLIDE 39 — Rhabdo Definition + Causes 1-4
# =====================================================================
s39 = content(f'''
{card('<b>Definition</b>', f'''
<p style="font-size:13px;color:{INK};margin:0;line-height:1.45;">Rhabdomyolysis is a disorder resulting from an <b style="color:{DANGER};">injury or a metabolic defect in the skeletal muscle cell</b> resulting in <b style="color:{RUST};">lysis of the cell membrane</b> and leakage of its contents (<b style="color:{DANGER};">myoglobin, enzymes, phosphorus, potassium</b>) into the blood.</p>
''', accent=DANGER)}
<div style="height:10px;"></div>
{card('<b>Causes</b>', f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
  <div style="background:{CREAM2};border-radius:8px;padding:9px 12px;border-left:4px solid {RUST};">
    <p style="font-size:13px;font-weight:700;color:{DEEP};margin:0 0 3px 0;">1. Direct trauma</p>
    <ul style="margin:0;padding:0 0 0 16px;color:{INK};font-size:12px;line-height:1.45;">
      <li>Crush syndrome.</li><li>Electrical shock.</li><li>Prolonged pressure with coma.</li><li>Thermal burns &amp; freezing.</li>
    </ul>
  </div>
  <div style="background:{CREAM2};border-radius:8px;padding:9px 12px;border-left:4px solid {RUST};">
    <p style="font-size:13px;font-weight:700;color:{DEEP};margin:0 0 3px 0;">2. Excessive exercise</p>
    <p style="font-size:12px;color:{INK};margin:0;">e.g.; athletic injury and convulsive seizures.</p>
  </div>
  <div style="background:{CREAM2};border-radius:8px;padding:9px 12px;border-left:4px solid {RUST};">
    <p style="font-size:13px;font-weight:700;color:{DEEP};margin:0 0 3px 0;">3. Hereditary myopathies</p>
    <p style="font-size:12px;color:{INK};margin:0;">e.g. myophosphorylase deficiency (<b style="color:{DANGER};">McArdle&rsquo;s disease</b>).</p>
  </div>
  <div style="background:{CREAM2};border-radius:8px;padding:9px 12px;border-left:4px solid {RUST};">
    <p style="font-size:13px;font-weight:700;color:{DEEP};margin:0 0 3px 0;">4. Acquired metabolic disorders</p>
    <ul style="margin:0;padding:0 0 0 16px;color:{INK};font-size:12px;line-height:1.45;">
      <li>Hyperthyroidism.</li><li>Hypokalemia (acute).</li><li>Diabetic ketoacidosis.</li><li>Hypophosphatemia (acute).</li><li>Alcoholism.</li><li>Hyponatremia (acute).</li>
    </ul>
  </div>
</div>
''', accent=BROWN)}
''')
write_slide(39, hdr('3', 'Rhabdomyolysis &mdash; Definition &amp; Causes (1&ndash;4)') + s39)

# =====================================================================
# SLIDE 40 — Rhabdo Causes 5-9
# =====================================================================
s40 = content(f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card('<b>5. Hypoxia and ischemia</b>', f'''
    <ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:13px;line-height:1.5;">
      <li>Carbon monoxide poisoning.</li><li>Vascular occlusion.</li><li>Atheromatous embolism.</li><li>Compartment syndrome.</li>
    </ul>
  ''', accent=RUST)}
  {card('<b>6. Drugs</b>', f'''
    <ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:13px;line-height:1.5;">
      <li><b style="color:{DANGER};">Statins and lipid-lowering drugs.</b></li><li>Cocaine.</li><li>Amphetamine derivatives.</li>
    </ul>
  ''', accent=RUST)}
  {card('<b>7. Infectious diseases</b>', f'''
    <ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:13px;line-height:1.5;">
      <li><b style="color:{DANGER};">Viral:</b> Coxsackie, HIV, Influenza.</li>
      <li><b style="color:{DANGER};">Bacterial:</b> Clostridia infection, Legionella, Streptococcal infection, Staphylococcal infection, Pneumococcal pneumonia.</li>
    </ul>
  ''', accent=RUST)}
  {card('<b>8. Toxins</b>', f'''
    <p style="font-size:13px;color:{INK};margin:0;">Snake venom, poisonous mushrooms, fish poisoning (<b style="color:{DANGER};">Haff disease</b>).</p>
  ''', accent=RUST)}
</div>
<div style="height:12px;"></div>
{card('<b>9. Miscellaneous</b>', f'''
<p style="font-size:14px;color:{INK};margin:0;"><b style="color:{DANGER};">Malignant hyperthermia</b>, <b style="color:{DANGER};">neuroleptic malignant syndrome</b>.</p>
''', accent=OLIVE, bg=CREAM2)}
''')
write_slide(40, hdr('3', 'Rhabdomyolysis &mdash; Causes (5&ndash;9)') + s40)

# =====================================================================
# SLIDE 41 — Rhabdo Pathogenesis
# =====================================================================
s41 = content(f'''
{card('<b>Mild and moderate rhabdomyolysis</b>', f'''
<p style="font-size:13px;color:{INK};margin:0;line-height:1.45;">(e.g. after intense exertion, violent repetitive activities or a grand mal seizure) &rarr; <b style="color:{RUST};">direct injury of muscle cells and depletion of energy stores</b> &rarr; muscle pain and weakness.</p>
''', accent=OLIVE, bg=CREAM2)}
<div style="height:10px;"></div>
{card('<b>Severe acute rhabdomyolysis (crush injury / pigmented nephropathy)</b>', f'''
<p style="font-size:13px;color:{SOFT};margin:0 0 6px 0;">AKI is due to;</p>
<ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:13px;line-height:1.5;">
  <li style="margin-bottom:8px;"><b style="color:{DANGER};">1. Renal ischemia:</b> Myoglobin has <b style="color:{DANGER};">intense vasoconstrictive effect</b> &rarr; renal ischemia.</li>
  <li><b style="color:{DANGER};">2. Tubular obstruction and injury:</b> Once the myoglobin molecule is filtered by the glomerulus and enters the PCT fluid;
    <ul style="margin:2px 0 0 0;padding:0 0 0 18px;font-size:12px;line-height:1.5;">
      <li>a. A portion enters the <b style="color:{RUST};">PCT cells</b>; inside the cells the molecule releases <b style="color:{DANGER};">elemental iron and iron compounds</b> forming toxic products that injure the cells.</li>
      <li>b. The remaining unabsorbed pigment passes to the <b style="color:{RUST};">distal nephron</b> and interacts with <b style="color:{DANGER};">Tamm-Horsfall protein</b> (in <b style="color:{RUST};">acidic urine</b>) forming a <b style="color:{DANGER};">gel</b> and obstructing urine flow. Then the concentration of pigment in the tubule rises, augmenting proximal tubular absorption and toxicity.</li>
    </ul>
  </li>
</ul>
''', accent=DANGER)}
''')
write_slide(41, hdr('3', 'Rhabdomyolysis &mdash; Pathogenesis') + s41)

# =====================================================================
# SLIDE 42 — Rhabdo Diagnosis
# =====================================================================
s42 = content(f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card('<b>Clinical features</b>', f'''
    <p style="font-size:13px;color:{SOFT};margin:0 0 6px 0;">Depend on the severity of muscle injury.</p>
    <ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:13px;line-height:1.5;">
      <li><b style="color:{RUST};">Mild and moderate cases:</b> muscular pain, tenderness, edema, stiffness, weakness and impaired mobility.</li>
      <li><b style="color:{DANGER};">Severe acute cases (crush injury): AKI.</b></li>
    </ul>
  ''', accent=BROWN)}
  {card('<b>Laboratory</b>', f'''
    <p style="font-size:13px;color:{INK};margin:0 0 6px 0;">Estimation of serum <b style="color:{DANGER};">Creatine Kinase &ldquo;CK&rdquo;</b> enzyme level;</p>
    <ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:13px;line-height:1.5;">
      <li>Elevated total serum CK levels <b style="color:{DANGER}">&gt; 500 IU/L</b> &rarr; <b style="color:{DANGER};">high suspicion</b> of acute rhabdomyolysis.</li>
      <li>The <b style="color:{RUST};">CK-MM isoform</b> &rarr; the <b style="color:{DANGER};">most sensitive test</b> to confirm the diagnosis.</li>
    </ul>
  ''', accent=OLIVE, bg=CREAM2)}
</div>
''')
write_slide(42, hdr('3', 'Rhabdomyolysis &mdash; Diagnosis') + s42)

# =====================================================================
# SLIDE 43 — Rhabdo Treatment + Prognosis
# =====================================================================
s43 = content(f'''
{card('<b>Treatment</b>', f'''
<p style="font-size:13px;color:{INK};margin:0 0 6px 0;"><b style="color:{DANGER};">Severe cases should be managed in ICU.</b></p>
<ol style="margin:0;padding:0 0 0 20px;color:{INK};font-size:13px;line-height:1.5;">
  <li style="margin-bottom:5px;"><b style="color:{RUST};">Aggressive and urgent volume replacement</b> to maintain organ perfusion &mdash; <b style="color:{DANGER};">caution</b> must be taken to avoid volume overload and pulmonary edema.</li>
  <li style="margin-bottom:5px;"><b style="color:{RUST};">Alkalinization of urine</b> with bicarb infusion to prevent obstructive cast formation.</li>
  <li style="margin-bottom:5px;">Special care to <b style="color:{RUST};">respiratory failure</b> due to diaphragmatic weakness if severe.</li>
  <li style="margin-bottom:5px;">Monitor for <b style="color:{DANGER};">hyperkalemia</b> by ECG and serum potassium level.</li>
  <li><b style="color:{DANGER};">Dialysis for severe AKI.</b></li>
</ol>
''', accent=DANGER)}
<div style="height:10px;"></div>
{card('<b>Prognosis</b>', f'''
<p style="font-size:14px;color:{INK};margin:0;line-height:1.45;">Those who survive acute rhabdomyolysis are at risk of <b style="color:{DANGER};">permanent disability (muscle fibrosis)</b>.</p>
''', accent=AMBER, bg=CREAM2)}
''')
write_slide(43, hdr('3', 'Rhabdomyolysis &mdash; Treatment &amp; Prognosis') + s43)

# =====================================================================
# SLIDE 44 — End / References
# =====================================================================
end = f'''
<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:{DEEP};"></div>
<div style="position:absolute;top:0;left:0;width:26px;height:540px;background:{CARAMEL};"></div>
<div style="position:absolute;bottom:0;left:0;width:960px;height:90px;background:{BROWN};"></div>
<svg style="position:absolute;top:-70px;left:-90px;width:520px;height:420px;z-index:1;" aria-hidden="true">
  <ellipse cx="260" cy="210" rx="210" ry="300" fill="{CARAMEL}" opacity="0.22"/>
</svg>
<div style="position:absolute;top:120px;left:80px;z-index:10;">
  <div style="width:90px;height:5px;background:{AMBER};margin-bottom:16px;"></div>
  <p style="font-size:52px;color:{ON_DARK};margin:0;font-weight:700;">End of Topic</p>
  <p style="font-size:24px;color:{AMBER};margin:10px 0 0 0;">Acute Kidney Injury &middot; AKI in Special Situations</p>
  <div style="width:70px;height:4px;background:{AMBER};margin:24px 0 18px 0;"></div>
  <p style="font-size:18px;color:{ON_DARK};margin:0;font-weight:400;">References</p>
  <p style="font-size:16px;color:{ON_DARK};margin:8px 0 0 0;opacity:0.85;">&bull; Principles of Nephrology &mdash; <b>Pages 26&ndash;30</b> (Acute Kidney Injury)</p>
  <p style="font-size:16px;color:{ON_DARK};margin:4px 0 0 0;opacity:0.85;">&bull; Principles of Nephrology &mdash; <b>Pages 30&ndash;35</b> (AKI in Special Situations)</p>
</div>
<div style="position:absolute;bottom:28px;left:80px;z-index:10;">
  <p style="font-size:17px;color:{ON_DARK};margin:0;opacity:0.95;">Dr. Hassan Abd-Elhady &mdash; Menoufia University</p>
</div>
'''
write_slide(44, end, bg=DEEP, badge_num=None)

# ---------------- Index ----------------
index_items = [
    (1, 'Cover &mdash; Acute Kidney Injury (AKI)'),
    (2, 'Table of Contents'),
    (3, 'Section 01 &mdash; Definition (divider)'),
    (4, 'Definition'),
    (5, 'Categorization &mdash; RIFLE &amp; AKIN Staging'),
    (6, 'Section 02 &mdash; Causes (divider)'),
    (7, 'Causes &mdash; Pre-renal'),
    (8, 'Causes &mdash; Intra-renal (Intrinsic)'),
    (9, 'Causes &mdash; Post-renal'),
    (10, 'Section 03 &mdash; Clinical Manifestations (divider)'),
    (11, 'Oliguria / Anuria'),
    (12, 'Causes of Anuric AKI'),
    (13, 'Manifestations of Loss of Kidney Function'),
    (14, 'Section 04 &mdash; Investigations (divider)'),
    (15, 'Investigations &mdash; Urine Examination'),
    (16, 'Investigations &mdash; FENa'),
    (17, 'Investigations &mdash; FEurea'),
    (18, 'Investigations &mdash; Blood &amp; Serology'),
    (19, 'Investigations &mdash; Bladder Pressure &amp; US/Doppler'),
    (20, 'Investigations &mdash; Renal Biopsy &amp; Biomarkers'),
    (21, 'Section 05 &mdash; Treatment (divider)'),
    (22, 'Treatment &mdash; A &amp; B'),
    (23, 'Treatment &mdash; C. Comorbid Conditions'),
    (24, 'Treatment &mdash; D. Renal Replacement Therapy'),
    (25, 'AKI in Special Situations (divider)'),
    (26, 'Section 1 &mdash; CIN (divider)'),
    (27, 'CIN &mdash; Definition &amp; Risk Factors'),
    (28, 'CIN &mdash; Pathogenesis'),
    (29, 'CIN &mdash; Diagnosis'),
    (30, 'CIN &mdash; Prevention &amp; Treatment'),
    (31, 'CIN &mdash; Prognosis'),
    (32, 'Section 2 &mdash; TLS (divider)'),
    (33, 'TLS &mdash; Definition &amp; Patients at Risk'),
    (34, 'TLS &mdash; Clinical Features &amp; Diagnosis'),
    (35, 'TLS &mdash; Differential Diagnosis'),
    (36, 'TLS &mdash; Prevention'),
    (37, 'TLS &mdash; Treatment of Established AKI'),
    (38, 'Section 3 &mdash; Rhabdomyolysis (divider)'),
    (39, 'Rhabdomyolysis &mdash; Definition &amp; Causes (1&ndash;4)'),
    (40, 'Rhabdomyolysis &mdash; Causes (5&ndash;9)'),
    (41, 'Rhabdomyolysis &mdash; Pathogenesis'),
    (42, 'Rhabdomyolysis &mdash; Diagnosis'),
    (43, 'Rhabdomyolysis &mdash; Treatment &amp; Prognosis'),
    (44, 'End &mdash; References'),
]
rows_html = ''
for n, t in index_items:
    rows_html += f'''<tr style="background:{CREAM if n % 2 else CREAM2};">
  <td style="padding:7px 12px;border:1px solid #C9AC85;color:{CARAMEL};font-weight:700;text-align:center;">{n:02d}</td>
  <td style="padding:7px 12px;border:1px solid #C9AC85;color:{INK};">
    <a href="slide-{n:02d}.html" target="_blank" style="color:{BROWN};font-weight:700;text-decoration:none;">{t} &rarr;</a>
  </td>
</tr>'''
index_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AKI Slide Deck &mdash; Index</title>
<style>
body {{ margin:0; padding:30px; background:{TAN}; font-family:'Times New Roman',serif; color:{INK}; }}
h1 {{ color:{DEEP}; font-size:34px; margin:0 0 4px 0; }}
.sub {{ color:{SOFT}; font-size:16px; margin:0 0 22px 0; }}
table {{ border-collapse:collapse; width:100%; max-width:760px; font-size:15px; }}
th {{ background:{BROWN}; color:{ON_DARK}; padding:9px 12px; text-align:left; }}
a:hover {{ text-decoration:underline !important; color:{DANGER} !important; }}
</style>
</head>
<body>
<h1>Acute Kidney Injury &mdash; Slide Deck Index</h1>
<p class="sub">44 slides &middot; Full content &mdash; no summarization &middot; Brown light-mode theme &middot; Dr. Hassan Abd-Elhady, Menoufia University</p>
<table>
  <tr><th style="width:60px;">Slide</th><th>Topic</th></tr>
  {rows_html}
</table>
</body>
</html>'''
with open('slides/index.html', 'w') as fh:
    fh.write(index_html)
print('wrote slides/index.html')
print('DONE — 44 slides generated')
