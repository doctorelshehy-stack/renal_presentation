# -*- coding: utf-8 -*-
"""Build a no-summarization HTML slide deck from the five Electrolytes & Acid-Base markdown files.
Theme: brown background, light mode, warm harmony colors, contrast for important info.
Chapters: Acid-Base Balance (14) · Hyponatremia (15) · Hypernatremia (16) · Hyperkalemia (17) · Hypokalemia (18)
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
    return f'''<div style="background:#F6DFD2;border-radius:8px;padding:9px 14px;border:1.5px solid {RUST};">
  <p style="font-size:14px;color:{INK};margin:0;line-height:1.45;"><b style="color:{DANGER};">&#9888; Important:</b> {html}</p>
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
  <p style="font-size:20px;color:{AMBER};margin:9px 0 0 0;">{subtitle}</p>
'''
    if topics:
        html += f'  <div style="margin-top:26px;max-width:720px;">{topics}</div>'
    html += '</div>'
    return html

# =====================================================================
# SLIDE 1 — Cover (Chapters 14–18)
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
<div style="position:absolute;top:100px;left:80px;z-index:10;">
  <div style="width:90px;height:5px;background:{AMBER};margin-bottom:16px;"></div>
  <p style="font-size:22px;color:{AMBER};margin:0;font-weight:400;letter-spacing:3px;">INTERNAL MEDICINE &middot; NEPHROLOGY</p>
  <p style="font-size:52px;color:{ON_DARK};margin:10px 0 0 0;font-weight:700;line-height:1.08;">Electrolytes &amp; Acid-Base<br>Disturbances</p>
  <div style="width:70px;height:4px;background:{AMBER};margin:20px 0 16px 0;"></div>
  <p style="font-size:22px;color:{ON_DARK};margin:0;font-weight:400;">Chapters 14 &ndash; 18 &mdash; Principles of Nephrology</p>
</div>
<div style="position:absolute;bottom:28px;left:80px;z-index:10;">
  <p style="font-size:17px;color:{ON_DARK};margin:0;opacity:0.95;">Dr. Hassan Abd-Elhady &mdash; Menoufia University</p>
  <p style="font-size:14px;color:{ON_DARK};margin:3px 0 0 0;opacity:0.7;">Acid-Base Balance &middot; Hyponatremia &middot; Hypernatremia &middot; Hyperkalemia &middot; Hypokalemia</p>
</div>
'''
write_slide(1, cover, bg=DEEP, badge_num=None)

# =====================================================================
# SLIDE 2 — TOC (Chapters 14–18)
# =====================================================================
toc_items = [
    ('01', 'Acid-Base Balance &mdash; Overview &middot; Metabolic Acidosis &middot; Metabolic Alkalosis'),
    ('02', 'Hyponatremia'),
    ('03', 'Hypernatremia'),
    ('04', 'Hyperkalemia'),
    ('05', 'Hypokalemia'),
]
toc = f'''
<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:{TAN};"></div>
<div style="position:absolute;top:20px;left:60px;z-index:10;">
  <p style="font-size:34px;color:{DEEP};font-weight:700;margin:0;">Table of Contents</p>
  <div style="width:70px;height:4px;background:{CARAMEL};margin:9px 0 24px 0;"></div>
</div>
<div style="position:absolute;top:95px;left:60px;right:60px;z-index:10;">
  <div style="display:grid;grid-template-columns:1fr;gap:14px 26px;">
'''
for n, t in toc_items:
    toc += f'''    <div style="display:flex;align-items:center;gap:14px;padding:13px 16px;background:{CREAM};border-radius:8px;border-left:4px solid {BROWN};box-shadow:0 1px 3px rgba(91,58,33,0.16);">
      <span style="font-size:22px;font-weight:700;color:{CARAMEL};min-width:34px;">{n}</span>
      <span style="font-size:18px;color:{INK};">{t}</span>
    </div>
'''
toc += '''  </div>
</div>
'''
write_slide(2, toc)

# =====================================================================
# SLIDE 3 — Section divider 01 Acid-Base Balance
# =====================================================================
topics3 = f'''
<div style="display:flex;gap:12px;">
  <div style="background:{BROWN};border-radius:8px;padding:10px 16px;"><p style="font-size:15px;color:{ON_DARK};margin:0;font-weight:700;">Overview</p></div>
  <div style="background:{BROWN};border-radius:8px;padding:10px 16px;"><p style="font-size:15px;color:{ON_DARK};margin:0;font-weight:700;">Metabolic Acidosis</p></div>
  <div style="background:{BROWN};border-radius:8px;padding:10px 16px;"><p style="font-size:15px;color:{ON_DARK};margin:0;font-weight:700;">Metabolic Alkalosis</p></div>
</div>
'''
write_slide(3, divider('01', 'Acid-Base Balance', 'Overview &middot; Metabolic Acidosis &middot; Metabolic Alkalosis', topics3))

# =====================================================================
# SLIDE 4 — Overview: Primary Events (Table 1)
# =====================================================================
overview_rows = [
    ('Metabolic acidosis',
     'Primary reduction of plasma HCO<sub>3</sub><sup>&minus;</sup>, leading to decrease in pH stimulating ventilation to decrease CO<sub>2</sub> <b style="color:{DANGER};">(low pH, CO<sub>2</sub> and HCO<sub>3</sub><sup>&minus;</sup>)</b>'),
    ('Metabolic alkalosis',
     'Primary increase of plasma HCO<sub>3</sub><sup>&minus;</sup>, leading to increase in pH inhibiting ventilation to increase CO<sub>2</sub> <b style="color:{DANGER};">(high pH, CO<sub>2</sub> and HCO<sub>3</sub><sup>&minus;</sup>)</b>'),
    ('Respiratory acidosis',
     'Primary retention of CO<sub>2</sub>, leading to decrease in pH enhancing renal retention of HCO<sub>3</sub><sup>&minus;</sup> <b style="color:{DANGER};">(low pH, high CO<sub>2</sub> and HCO<sub>3</sub><sup>&minus;</sup>)</b>'),
    ('Respiratory alkalosis',
     'Primary loss of CO<sub>2</sub>, leading to increase in pH enhancing renal excretion of HCO<sub>3</sub><sup>&minus;</sup> <b style="color:{DANGER};">(high pH, low CO<sub>2</sub> and HCO<sub>3</sub><sup>&minus;</sup>)</b>'),
]
ov_tr = ''
for i, (name, ev) in enumerate(overview_rows):
    bgc = CREAM if i % 2 == 0 else CREAM2
    ov_tr += f'''<tr style="background:{bgc};">
      <td style="padding:9px 10px;border:1px solid #C9AC85;width:20%;font-weight:700;color:{BROWN};">{name}</td>
      <td style="padding:9px 10px;border:1px solid #C9AC85;color:{INK};">{ev}</td>
    </tr>'''
s4 = content(f'''
<p style="font-size:14px;color:{SOFT};margin:0 0 10px 0;font-style:italic;">Overview of Acid-Base Disturbances &mdash; the primary event in each of the four disturbances</p>
<table style="width:100%;border-collapse:collapse;font-size:13px;">
  <tr style="background:{BROWN};color:{ON_DARK};">
    <th style="padding:8px 10px;border:1px solid {BROWN};text-align:left;">Disturbance</th>
    <th style="padding:8px 10px;border:1px solid {BROWN};text-align:left;">Primary event</th>
  </tr>
  {ov_tr}
</table>
<div style="height:10px;"></div>
{note('The <b>primary event</b> (H<sup>+</sup> gain/loss or CO<sub>2</sub> retention/loss) triggers a <b>physiologic compensatory response</b> by the other organ system (lungs or kidneys) to defend the pH.')}
''')
write_slide(4, hdr('01', 'Overview of Acid-Base Disturbances &mdash; Primary Events') + s4)

# =====================================================================
# SLIDE 5 — Body Compensation Table (Table 2)
# =====================================================================
comp_rows = [
    ('PH', '&darr;', '&uarr;', '&darr;', '&uarr;'),
    ('CO<sub>2</sub>', '&darr;', '&uarr;', '&uarr;', '&darr;'),
    ('HCO<sub>3</sub><sup>&minus;</sup>', '&darr;', '&uarr;', '&uarr;', '&darr;'),
]
comp_tr = ''
for i, (param, ma, malk, ra, ralk) in enumerate(comp_rows):
    bgc = CREAM if i % 2 == 0 else CREAM2
    col = DANGER if i == 0 else INK
    comp_tr += f'''<tr style="background:{bgc};">
      <td style="padding:9px 10px;border:1px solid #C9AC85;font-weight:700;color:{BROWN};text-align:center;">{param}</td>
      <td style="padding:9px 10px;border:1px solid #C9AC85;text-align:center;color:{col};font-size:16px;font-weight:700;">{ma}</td>
      <td style="padding:9px 10px;border:1px solid #C9AC85;text-align:center;color:{col};font-size:16px;font-weight:700;">{malk}</td>
      <td style="padding:9px 10px;border:1px solid #C9AC85;text-align:center;color:{col};font-size:16px;font-weight:700;">{ra}</td>
      <td style="padding:9px 10px;border:1px solid #C9AC85;text-align:center;color:{col};font-size:16px;font-weight:700;">{ralk}</td>
    </tr>'''
s5 = content(f'''
<p style="font-size:14px;color:{SOFT};margin:0 0 10px 0;font-style:italic;">Table: Body compensation to Acid-Base imbalance</p>
<table style="width:100%;border-collapse:collapse;font-size:14px;">
  <tr style="background:{BROWN};color:{ON_DARK};">
    <th style="padding:8px 10px;border:1px solid {BROWN};text-align:center;">Parameter</th>
    <th style="padding:8px 10px;border:1px solid {BROWN};text-align:center;">Metabolic &mdash; Acidosis</th>
    <th style="padding:8px 10px;border:1px solid {BROWN};text-align:center;">Metabolic &mdash; Alkalosis</th>
    <th style="padding:8px 10px;border:1px solid {BROWN};text-align:center;">Respiratory &mdash; Acidosis</th>
    <th style="padding:8px 10px;border:1px solid {BROWN};text-align:center;">Respiratory &mdash; Alkalosis</th>
  </tr>
  {comp_tr}
</table>
<div style="height:12px;"></div>
{warn('Reading the table: e.g. in <b>metabolic acidosis</b> the pH is low, CO<sub>2</sub> falls (respiratory compensation &mdash; hyperventilation) and HCO<sub>3</sub><sup>&minus;</sup> is low (the primary deficit).')}
<div style="height:12px;"></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card('<b>Direction of change</b>', '<p style="font-size:13px;color:' + INK + ';margin:0;">The <b style="color:' + DANGER + ';">pH</b> always follows the primary disturbance; the <b style="color:' + RUST + ';">compensatory</b> change opposes it (e.g. metabolic acidosis &rarr; CO<sub>2</sub> &darr;).</p>', accent=AMBER, bg=CREAM2)}
  {card('<b>Compensatory direction</b>', '<p style="font-size:13px;color:' + INK + ';margin:0;">Lungs compensate <b style="color:' + RUST + ';">metabolic</b> disorders by changing CO<sub>2</sub>; kidneys compensate <b style="color:' + RUST + ';">respiratory</b> disorders by changing HCO<sub>3</sub><sup>&minus;</sup>.</p>', accent=OLIVE, bg=CREAM2)}
</div>
''')
write_slide(5, hdr('01', 'Body Compensation to Acid-Base Imbalance') + s5)

# =====================================================================
# SLIDE 6 — Section divider 1A Metabolic Acidosis
# =====================================================================
topics6 = f'''
<div style="display:flex;gap:12px;">
  <div style="background:{BROWN};border-radius:8px;padding:10px 14px;"><p style="font-size:14px;color:{ON_DARK};margin:0;font-weight:700;">Definition</p></div>
  <div style="background:{BROWN};border-radius:8px;padding:10px 14px;"><p style="font-size:14px;color:{ON_DARK};margin:0;font-weight:700;">Anion Gap</p></div>
  <div style="background:{BROWN};border-radius:8px;padding:10px 14px;"><p style="font-size:14px;color:{ON_DARK};margin:0;font-weight:700;">Causes</p></div>
  <div style="background:{BROWN};border-radius:8px;padding:10px 14px;"><p style="font-size:14px;color:{ON_DARK};margin:0;font-weight:700;">Clinical Features</p></div>
  <div style="background:{BROWN};border-radius:8px;padding:10px 14px;"><p style="font-size:14px;color:{ON_DARK};margin:0;font-weight:700;">Treatment</p></div>
</div>
'''
write_slide(6, divider('1A', 'Metabolic Acidosis', 'Definition &middot; The Anion Gap &middot; Causes &middot; Clinical Features &middot; Investigations &middot; Treatment', topics6))

# =====================================================================
# SLIDE 7 — MA: Definition & The Anion Gap (concept)
# =====================================================================
s7 = content(
    card('<b>Definition</b>',
         '<p style="font-size:14px;color:' + INK + ';margin:0;line-height:1.45;">Decrease in <b style="color:' + DANGER + ';">blood pH</b> due to a decrease in <b style="color:' + DANGER + ';">serum HCO<sub>3</sub><sup>&minus;</sup></b> concentrations.</p>',
         accent=DANGER) +
    f'<div style="height:12px;"></div>' +
    card('<b>The Anion Gap (AG)</b>', f'''
    <p style="font-size:14px;color:{INK};margin:0 0 7px 0;line-height:1.45;">Plasma is <b style="color:{RUST};">electro-neutral</b>, i.e. total anions match total cations.</p>
    <ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:13.5px;line-height:1.5;">
      <li style="margin-bottom:5px;">The major <b style="color:{OLIVE};">measured</b> plasma cation is <b>Na<sup>+</sup></b>; the major <b style="color:{OLIVE};">measured</b> anions are <b>HCO<sub>3</sub><sup>&minus;</sup></b> and <b>Cl<sup>&minus;</sup></b>.</li>
      <li style="margin-bottom:5px;">There are <b style="color:{OLIVE};">unmeasured</b> plasma cations (e.g. K<sup>+</sup>, Mg<sup>2+</sup> and Ca<sup>2+</sup>) as well as <b style="color:{OLIVE};">unmeasured</b> anions (e.g. sulfate, phosphate and some organic anions).</li>
      <li style="margin-bottom:5px;">The unmeasured anions are <b style="color:{DANGER};">slightly more</b> than the unmeasured cations; this difference is termed <b style="color:{DANGER};">&quot;the Anion Gap (AG)&quot;</b>.</li>
      <li>Based on the fact that the total cations equal the total anions; AG can be calculated as the difference between the major cation (Na<sup>+</sup>) and the sum of the major anions (HCO<sub>3</sub><sup>&minus;</sup> and Cl<sup>&minus;</sup>), i.e. <b style="color:{DANGER};">AG = Na<sup>+</sup> &minus; (HCO<sub>3</sub><sup>&minus;</sup> + Cl<sup>&minus;</sup>)</b>.</li>
    </ul>
    ''', accent=BROWN) +
    f'<div style="height:10px;"></div>' +
    note('An <b>increase of AG</b> can result from either: a <b>decrease in the unmeasured cations</b> (e.g. hypokalemia) or an <b>increase in the unmeasured anions</b> (e.g. hyperphosphatemia).')
)
write_slide(7, hdr('1A', 'Metabolic Acidosis &mdash; Definition &amp; The Anion Gap') + s7)

# =====================================================================
# SLIDE 8 — MA: AG — Formula & Types (high vs normal AG)
# =====================================================================
s8 = content(f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card('<b>AG formula</b>', f'''
    <p style="font-size:19px;font-weight:700;color:{DEEP};margin:0 0 4px 0;text-align:center;">AG = Na<sup>+</sup> &minus; (HCO<sub>3</sub><sup>&minus;</sup> + Cl<sup>&minus;</sup>)</p>
    <p style="font-size:12px;color:{SOFT};margin:0;text-align:center;">In certain forms of metabolic acidosis, acidic substances (anions) accumulate and increase the AG</p>
  ''', accent=DANGER)}
  {card('<b>Why the AG matters</b>', f'''
    <p style="font-size:13.5px;color:{INK};margin:0;line-height:1.45;">By recognizing the <b style="color:{DANGER};">increase in the AG</b>, this can help to <b style="color:{RUST};">differentiate the cause</b> of acidosis. Thus, metabolic acidosis can be either:</p>
  ''', accent=BROWN)}
</div>
<div style="height:12px;"></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card('<b>1. High AG metabolic acidosis</b>',
    '<p style="font-size:13.5px;color:' + INK + ';margin:0;line-height:1.45;">The reduction in plasma HCO<sub>3</sub><sup>&minus;</sup> <b style="color:' + DANGER + ';">equals</b> the increase in AG.</p>',
    accent=DANGER)}
  {card('<b>2. Normal (Non) AG metabolic acidosis</b>',
    '<p style="font-size:13.5px;color:' + INK + ';margin:0;line-height:1.45;">The reduction in plasma HCO<sub>3</sub><sup>&minus;</sup> is compensated by an <b style="color:' + DANGER + ';">increase in plasma Cl<sup>&minus;</sup></b> to maintain electro-neutrality (<b style="color:' + RUST + ';">hyperchloremic</b> metabolic acidosis).</p>',
    accent=OLIVE)}
</div>
<div style="height:12px;"></div>
{warn('High AG: the &ldquo;extra&rdquo; unmeasured anions are the retained acids. Normal AG: chloride rises to balance the lost bicarbonate (hyperchloremic).')}
''')
write_slide(8, hdr('1A', 'Metabolic Acidosis &mdash; Anion Gap: Formula &amp; Types') + s8)

# =====================================================================
# SLIDE 9 — MA: Causes (normal AG & high AG)
# =====================================================================
s9 = content(f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card('<b>Normal AG (hyperchloremic) metabolic acidosis</b>', f'''
  <ol style="margin:0;padding:0 0 0 20px;color:{INK};font-size:13px;line-height:1.45;">
    <li style="margin-bottom:7px;">GI loss of HCO<sub>3</sub><sup>&minus;</sup> (e.g. <b style="color:{DANGER};">diarrhea</b>, enteric fistula).</li>
    <li style="margin-bottom:7px;">Renal loss of HCO<sub>3</sub><sup>&minus;</sup> (<b style="color:{DANGER};">Proximal Type II RTA</b>).</li>
    <li style="margin-bottom:7px;">Failure of renal H<sup>+</sup> secretion (<b style="color:{DANGER};">Distal Type I RTA</b>).</li>
    <li>Acid infusion (e.g. <b style="color:{DANGER};">ammonium chloride</b>, hyperalimentation).</li>
  </ol>
  ''', accent=OLIVE)}
  {card('<b>High AG metabolic acidosis</b>', f'''
  <ol style="margin:0;padding:0 0 0 20px;color:{INK};font-size:13px;line-height:1.45;">
    <li style="margin-bottom:7px;"><b style="color:{DANGER};">Ketoacidosis</b> (beta-hydroxybutyrate and acetoacetate).</li>
    <li style="margin-bottom:7px;"><b style="color:{DANGER};">Renal failure</b> (phosphate, sulfate, urate).</li>
    <li style="margin-bottom:7px;"><b style="color:{DANGER};">Lactic acidosis</b> (L-lactate, D-lactate).</li>
    <li style="margin-bottom:7px;"><b style="color:{DANGER};">Massive rhabdomyolysis</b> (H<sup>+</sup> and organic anions from the damaged muscles).</li>
    <li><b style="color:{DANGER};">Exogenous</b> (salicylate, methanol, ethylene glycol, metformin).</li>
  </ol>
  ''', accent=DANGER)}
</div>
<div style="height:10px;"></div>
{note('Mnemonics of high AG acidosis: <b>K.U.S.M.A.U.L.</b>-like list &mdash; <b>K</b>etoacidosis, <b>U</b>remia (renal failure), <b>S</b>alicylates, <b>M</b>ethanol, <b>A</b>lcohol (ketoacidosis), <b>U</b>ric acid (rhabdomyolysis), <b>L</b>actic acidosis.')}
''')
write_slide(9, hdr('1A', 'Metabolic Acidosis &mdash; Causes &amp; Classification') + s9)

# =====================================================================
# SLIDE 10 — MA: Clinical Features (symptoms & signs)
# =====================================================================
s10 = content(f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card('<b>Symptoms</b>', f'''
  <ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:13px;line-height:1.42;">
    <li style="margin-bottom:6px;">Variable degrees of <b style="color:{DANGER};">dyspnea</b> (due to hyperventilation).</li>
    <li style="margin-bottom:6px;">Other symptoms are <b style="color:{SOFT};">non-specific</b> and symptoms of the cause if present, e.g.;</li>
    <li style="margin-bottom:6px;">1- Symptoms of <b style="color:{RUST};">diabetic ketoacidosis (DKA)</b> or of <b style="color:{RUST};">CKD</b>.</li>
    <li>2- History of <b style="color:{RUST};">alcoholism</b>, drug intake (e.g. salicylates, acetazolamide, metformin), or of <b style="color:{RUST};">renal stone</b> (e.g. in RTA).</li>
  </ul>
  ''', accent=BROWN)}
  {card('<b>Signs</b>', f'''
  <ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:13px;line-height:1.42;">
    <li style="margin-bottom:6px;">The most prominent sign is <b style="color:{DANGER};">Kussmaul Respiration</b> (rapid deep breathing).</li>
    <li style="margin-bottom:6px;">Other signs are non-specific if present, e.g.;</li>
    <li style="margin-bottom:6px;">1- <b style="color:{RUST};">Hypotension</b>, cardiac arrhythmia.</li>
    <li style="margin-bottom:6px;">2- <b style="color:{RUST};">Disturbed consciousness</b> and coma.</li>
    <li>3- Signs of the cause, e.g. DKA, CKD, or alcoholism.</li>
  </ul>
  ''', accent=DANGER)}
</div>
<div style="height:12px;"></div>
{card('<b>Key examination point</b>',
  '<p style="font-size:13.5px;color:' + INK + ';margin:0;line-height:1.45;"><b style="color:' + DANGER + ';">Kussmaul respiration</b> (rapid, deep sighing breathing) is the hallmark respiratory sign &mdash; the body attempts to blow off CO<sub>2</sub> to compensate the metabolic acidosis.</p>',
  accent=AMBER, bg=CREAM2)}
''')
write_slide(10, hdr('1A', 'Metabolic Acidosis &mdash; Clinical Features') + s10)

# =====================================================================
# SLIDE 11 — MA: Investigations
# =====================================================================
s11 = content(f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card('<b>General investigations</b>', f'''
  <p style="font-size:13.5px;color:{INK};margin:0 0 6px 0;">&rarr; to diagnose metabolic acidosis and calculate AG, e.g.;</p>
  <ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:13px;line-height:1.45;">
    <li style="margin-bottom:6px;"><b style="color:{DANGER};">ABG</b> (arterial blood gases): pH, HCO<sub>3</sub><sup>&minus;</sup>, CO<sub>2</sub></li>
    <li><b style="color:{DANGER};">Serum electrolytes</b>: Na<sup>+</sup>, K<sup>+</sup> and Cl<sup>&minus;</sup></li>
  </ul>
  ''', accent=BROWN)}
  {card('<b>Specific investigations</b>', f'''
  <p style="font-size:13.5px;color:{INK};margin:0 0 6px 0;">&rarr; to diagnose the etiology, e.g.;</p>
  <ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:13px;line-height:1.45;">
    <li style="margin-bottom:6px;"><b style="color:{DANGER};">Kidney functions</b></li>
    <li style="margin-bottom:6px;"><b style="color:{DANGER};">Blood glucose level</b></li>
    <li style="margin-bottom:6px;"><b style="color:{DANGER};">Urinary ketones</b></li>
    <li style="margin-bottom:6px;"><b style="color:{DANGER};">Serum lactate</b></li>
    <li><b style="color:{DANGER};">Toxicological screening</b></li>
  </ul>
  ''', accent=OLIVE)}
</div>
<div style="height:12px;"></div>
{note('<b>Stepwise approach:</b> confirm acidosis on ABG (low pH + low HCO<sub>3</sub><sup>&minus;</sup>) &rarr; compute the AG from electrolytes &rarr; then target specific tests according to the suspected etiology.')}
''')
write_slide(11, hdr('1A', 'Metabolic Acidosis &mdash; Investigations') + s11)

# =====================================================================
# SLIDE 12 — MA: Treatment
# =====================================================================
s12 = content(f'''
{card('<b>General principles</b>', f'''
<ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:13.5px;line-height:1.45;">
  <li style="margin-bottom:6px;">Treatment is generally directed to the <b style="color:{DANGER};">underlying condition or disease</b>.</li>
  <li>Treatment of acidosis using <b style="color:{DANGER};">alkali therapy (HCO<sub>3</sub><sup>&minus;</sup>)</b> is usually indicated to raise plasma pH above <b style="color:{DANGER};">7.20</b> in the following circumstances:</li>
</ul>
''', accent=DANGER)}
<div style="height:10px;"></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card('<b>1. Low HCO<sub>3</sub><sup>&minus;</sup> + PCO<sub>2</sub> near compensation limit</b>',
    '<p style="font-size:12.5px;color:' + INK + ';margin:0;line-height:1.42;">Low serum HCO<sub>3</sub><sup>&minus;</sup> and PCO<sub>2</sub> close to the lower limit of compensation (approximately <b style="color:' + DANGER + ';">15 mmHg</b>). Any further drop in HCO<sub>3</sub><sup>&minus;</sup> will not be matched by a corresponding fall in PCO<sub>2</sub> &rarr; <b style="color:' + DANGER + ';">marked drop in pH</b>.</p>',
    accent=RUST, bg=CREAM2)}
  {card('<b>2. Well-compensated acidosis + impending respiratory failure</b>',
    '<p style="font-size:12.5px;color:' + INK + ';margin:0;line-height:1.42;">Well-compensated metabolic acidosis with <b style="color:' + DANGER + ';">impending respiratory failure</b> due to respiratory muscle fatigue. PCO<sub>2</sub> starts to rise &rarr; <b style="color:' + DANGER + ';">dramatic drop in pH</b>.</p>',
    accent=RUST, bg=CREAM2)}
</div>
<div style="height:10px;"></div>
{card('<b>Route of administration of bicarbonate</b>', f'''
<ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:13px;line-height:1.45;">
  <li style="margin-bottom:6px;"><b style="color:{DANGER};">I.V. sodium bicarbonate (NaHCO<sub>3</sub>)</b>: corrects <b style="color:{RUST};">acute</b> metabolic acidosis. Deficit can be calculated as: <b style="color:{DANGER};">(Desired HCO<sub>3</sub><sup>&minus;</sup> &minus; Measured HCO<sub>3</sub><sup>&minus;</sup>) &times; 0.5 &times; body weight</b>.</li>
  <li style="margin-bottom:6px;"><b style="color:{DANGER};">Oral sodium bicarbonate (NaHCO<sub>3</sub>)</b>: used to correct <b style="color:{RUST};">chronic</b> metabolic acidosis (e.g. RTA) and uncommonly used in acute situations when the I.V. route is not suitable.</li>
  <li><b style="color:{CARAMEL};">Monitoring:</b> serum HCO<sub>3</sub><sup>&minus;</sup> and pH should be assessed frequently; monitor serum Na<sup>+</sup>, volume status and PCO<sub>2</sub> during treatment.</li>
</ul>
''', accent=OLIVE)}
''')
write_slide(12, hdr('1A', 'Metabolic Acidosis &mdash; Treatment') + s12)

# =====================================================================
# SLIDE 13 — Section divider 1B Metabolic Alkalosis
# =====================================================================
topics13 = f'''
<div style="display:flex;gap:12px;">
  <div style="background:{BROWN};border-radius:8px;padding:10px 14px;"><p style="font-size:14px;color:{ON_DARK};margin:0;font-weight:700;">Definition</p></div>
  <div style="background:{BROWN};border-radius:8px;padding:10px 14px;"><p style="font-size:14px;color:{ON_DARK};margin:0;font-weight:700;">Classification</p></div>
  <div style="background:{BROWN};border-radius:8px;padding:10px 14px;"><p style="font-size:14px;color:{ON_DARK};margin:0;font-weight:700;">Causes</p></div>
  <div style="background:{BROWN};border-radius:8px;padding:10px 14px;"><p style="font-size:14px;color:{ON_DARK};margin:0;font-weight:700;">Clinical Features</p></div>
  <div style="background:{BROWN};border-radius:8px;padding:10px 14px;"><p style="font-size:14px;color:{ON_DARK};margin:0;font-weight:700;">Treatment</p></div>
</div>
'''
write_slide(13, divider('1B', 'Metabolic Alkalosis', 'Definition &middot; Causes &amp; Classification &middot; Clinical Features &middot; Investigations &middot; Treatment', topics13))

# =====================================================================
# SLIDE 14 — MAlk: Definition & Classification
# =====================================================================
s14 = content(f'''
{card('<b>Definition</b>',
  '<p style="font-size:14px;color:' + INK + ';margin:0;line-height:1.45;">An increase in <b style="color:' + DANGER + ';">blood pH</b> due to increase in <b style="color:' + DANGER + ';">serum HCO<sub>3</sub><sup>&minus;</sup></b> concentrations.</p>',
  accent=DANGER)}
<div style="height:12px;"></div>
{card('<b>Causes and classification</b>', f'''
<p style="font-size:13.5px;color:{INK};margin:0 0 8px 0;">Causes of metabolic alkalosis can be classified into;</p>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;">
  <div style="background:{CREAM2};border-radius:8px;padding:10px 12px;border-top:3px solid {AMBER};"><p style="font-size:13px;color:{INK};margin:0;"><b style="color:{CARAMEL};">1. Chloride-responsive</b><br>urine chloride <b style="color:{DANGER};">&lt; 20 mEq/L</b></p></div>
  <div style="background:{CREAM2};border-radius:8px;padding:10px 12px;border-top:3px solid {AMBER};"><p style="font-size:13px;color:{INK};margin:0;"><b style="color:{CARAMEL};">2. Chloride-resistant</b><br>urine chloride <b style="color:{DANGER};">&gt; 20 mEq/L</b></p></div>
  <div style="background:{CREAM2};border-radius:8px;padding:10px 12px;border-top:3px solid {AMBER};"><p style="font-size:13px;color:{INK};margin:0;"><b style="color:{CARAMEL};">3. Other causes</b><br>including <b style="color:{DANGER};">alkali-loading</b> alkalosis</p></div>
</div>
''', accent=BROWN)}
<div style="height:12px;"></div>
{note('The <b style="color:' + DANGER + ';">urine chloride</b> measurement is the key first step &mdash; it separates saline-responsive from saline-resistant alkalosis.')}
''')
write_slide(14, hdr('1B', 'Metabolic Alkalosis &mdash; Definition &amp; Classification') + s14)

# =====================================================================
# SLIDE 15 — MAlk: Causes (A. chloride-responsive + C. other)
# =====================================================================
s15 = content(f'''
{card('<b>A. Causes of chloride-responsive alkalosis (urine chloride &lt; 20 mEq/L)</b>', f'''
<ol style="margin:0;padding:0 0 0 20px;color:{INK};font-size:13px;line-height:1.45;">
  <li style="margin-bottom:6px;"><b style="color:{DANGER};">Loss of gastric secretions</b>; vomiting, nasogastric suction.</li>
  <li style="margin-bottom:6px;"><b style="color:{DANGER};">Loss of colonic secretions</b>; congenital chloridorrhea, villous adenoma.</li>
  <li style="margin-bottom:6px;"><b style="color:{DANGER};">Volume depletion.</b></li>
  <li style="margin-bottom:6px;"><b style="color:{DANGER};">Thiazides and loop diuretics</b> (after discontinuation).</li>
  <li><b style="color:{DANGER};">Cystic fibrosis.</b></li>
</ol>
''', accent=RUST)}
<div style="height:10px;"></div>
{card('<b>C. Other causes of metabolic alkalosis</b>', f'''
<ol style="margin:0;padding:0 0 0 20px;color:{INK};font-size:12.5px;line-height:1.42;">
  <li style="margin-bottom:5px;">Exogenous alkali administration: <b style="color:{RUST};">sodium bicarbonate</b> or <b style="color:{RUST};">massive blood transfusion</b> (high citrate content) in the presence of renal insufficiency.</li>
  <li style="margin-bottom:5px;"><b style="color:{RUST};">Recovery of metabolic acidosis</b> (due to the metabolism of lactic acid or ketoacids).</li>
  <li style="margin-bottom:5px;"><b style="color:{RUST};">Milk-alkali syndrome</b> (comprises hypercalcemia, renal insufficiency, and metabolic alkalosis).</li>
  <li style="margin-bottom:5px;"><b style="color:{RUST};">Hypercalcemia</b> causes volume depletion and enhanced bicarbonate reabsorption.</li>
  <li><b style="color:{RUST};">Hypoalbuminemia</b>: may be related to loss of negative charges of albumin.</li>
</ol>
''', accent=OLIVE, bg=CREAM2)}
''')
write_slide(15, hdr('1B', 'Metabolic Alkalosis &mdash; Causes (Chloride-responsive &amp; Other)') + s15)

# =====================================================================
# SLIDE 16 — MAlk: Causes (B. chloride-resistant)
# =====================================================================
s16 = content(f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card('<b>B1. Chloride-resistant with hypertension</b>', f'''
  <ol style="margin:0;padding:0 0 0 20px;color:{INK};font-size:12.5px;line-height:1.42;">
    <li style="margin-bottom:6px;"><b style="color:{DANGER};">Hyperaldosteronism</b> (primary, adrenal adenoma, hyperplasia, carcinoma, glucocorticoid-remediable hyperaldosteronism).</li>
    <li style="margin-bottom:6px;"><b style="color:{DANGER};">Cushing syndrome.</b></li>
    <li style="margin-bottom:6px;"><b style="color:{DANGER};">Exogenous steroids.</b></li>
    <li style="margin-bottom:6px;"><b style="color:{DANGER};">Liddle&rsquo;s syndrome.</b></li>
    <li><b style="color:{DANGER};">Reno-vascular hypertension.</b></li>
  </ol>
  ''', accent=DANGER)}
  {card('<b>B2. Chloride-resistant without hypertension</b>', f'''
  <ol style="margin:0;padding:0 0 0 20px;color:{INK};font-size:12.5px;line-height:1.42;">
    <li style="margin-bottom:6px;"><b style="color:{DANGER};">Bartter&rsquo;s syndrome.</b></li>
    <li style="margin-bottom:6px;"><b style="color:{DANGER};">Gitelman syndrome.</b></li>
    <li style="margin-bottom:6px;"><b style="color:{DANGER};">Severe potassium depletion.</b></li>
    <li style="margin-bottom:6px;"><b style="color:{DANGER};">Current use of thiazides and loop diuretics.</b></li>
    <li><b style="color:{DANGER};">Hypomagnesaemia</b>: the mechanism probably involves hypokalemia, which is usually caused by or associated with magnesium depletion.</li>
  </ol>
  ''', accent=OLIVE)}
</div>
<div style="height:12px;"></div>
{warn('Key discriminator: <b>hypertension + chloride-resistant alkalosis</b> &rarr; think hyperaldosteronism / Cushing / Liddle; <b>normotension</b> &rarr; think Bartter / Gitelman / K<sup>+</sup> or Mg<sup>2+</sup> depletion.')}
''')
write_slide(16, hdr('1B', 'Metabolic Alkalosis &mdash; Causes (Chloride-resistant)') + s16)

# =====================================================================
# SLIDE 17 — MAlk: Clinical Features
# =====================================================================
s17 = content(f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card('<b>History</b>', f'''
  <ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:12.5px;line-height:1.42;">
    <li style="margin-bottom:5px;">Helpful in establishing the <b style="color:{RUST};">etiology</b>, e.g. GI fluid loss, surgery, drug history, or renal insufficiency.</li>
    <li style="margin-bottom:5px;">Symptoms: <b style="color:{SOFT};">not specific</b>.</li>
    <li style="margin-bottom:5px;"><b style="color:{DANGER};">Hypoventilation</b> because of inhibition of the respiratory centers.</li>
    <li style="margin-bottom:5px;">Symptoms of <b style="color:{DANGER};">hypokalemia</b>, e.g. weakness, myalgia, polyuria, and cardiac arrhythmias.</li>
    <li>Symptoms of <b style="color:{DANGER};">hypocalcemia</b> (e.g. perioral tingling, muscle cramps and carpopedal spasms) due to decreased ionized calcium.</li>
  </ul>
  ''', accent=BROWN)}
  {card('<b>Signs</b>', f'''
  <ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:12.5px;line-height:1.42;">
    <li style="margin-bottom:5px;">Also not specific but may help to establish the cause.</li>
    <li style="margin-bottom:5px;"><b style="color:{RUST};">Volume depletion</b> usually accompanies chloride-responsive alkalosis, while <b style="color:{RUST};">volume expansion</b> accompanies chloride-resistant alkalosis.</li>
    <li style="margin-bottom:5px;">There may be signs of <b style="color:{DANGER};">hypocalcaemia</b>, e.g. <b style="color:{DANGER};">tetany, Chvostek sign, and Trousseau sign</b>.</li>
    <li>Change in <b style="color:{DANGER};">mental status</b>, or <b style="color:{DANGER};">seizures</b>.</li>
  </ul>
  ''', accent=DANGER)}
</div>
<div style="height:12px;"></div>
{card('<b>Key clinical clue</b>',
  '<p style="font-size:13px;color:' + INK + ';margin:0;line-height:1.45;">Volume status on examination points to the subtype: <b style="color:' + DANGER + ';">volume depleted</b> &rarr; chloride-responsive; <b style="color:' + DANGER + ';">volume expanded</b> &rarr; chloride-resistant.</p>',
  accent=AMBER, bg=CREAM2)}
''')
write_slide(17, hdr('1B', 'Metabolic Alkalosis &mdash; Clinical Features') + s17)

# =====================================================================
# SLIDE 18 — MAlk: Investigations
# =====================================================================
s18 = content(f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card('<b>General investigations</b>', f'''
  <p style="font-size:13.5px;color:{INK};margin:0 0 6px 0;">&rarr; for the diagnosis of metabolic alkalosis.</p>
  <ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:13px;line-height:1.45;">
    <li style="margin-bottom:6px;"><b style="color:{DANGER};">ABG</b> (arterial blood gases): pH, HCO<sub>3</sub><sup>&minus;</sup>, CO<sub>2</sub></li>
    <li style="margin-bottom:6px;"><b style="color:{DANGER};">Serum electrolytes</b>: Na<sup>+</sup>, K<sup>+</sup>, Cl<sup>&minus;</sup>, Ca<sup>2+</sup> and Mg<sup>2+</sup></li>
    <li><b style="color:{DANGER};">Urinary Cl<sup>&minus;</sup></b></li>
  </ul>
  ''', accent=BROWN)}
  {card('<b>Specific investigations</b>', f'''
  <p style="font-size:13.5px;color:{INK};margin:0 0 6px 0;">&rarr; for determination of the etiology, e.g.</p>
  <ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:13px;line-height:1.45;">
    <li style="margin-bottom:6px;"><b style="color:{DANGER};">Plasma aldosterone and cortisol levels</b></li>
    <li style="margin-bottom:6px;"><b style="color:{DANGER};">Plasma renin activity</b></li>
    <li><b style="color:{DANGER};">Reno-vascular imaging</b></li>
  </ul>
  ''', accent=OLIVE)}
</div>
<div style="height:12px;"></div>
{note('Urine chloride (&lt; 20 vs &gt; 20 mEq/L) separates <b>chloride-responsive</b> from <b>chloride-resistant</b> alkalosis; hormone assays then target the specific etiology.')}
''')
write_slide(18, hdr('1B', 'Metabolic Alkalosis &mdash; Investigations') + s18)

# =====================================================================
# SLIDE 19 — MAlk: Treatment
# =====================================================================
s19 = content(f'''
<p style="font-size:14px;color:{SOFT};margin:0 0 10px 0;font-style:italic;">Treatment depends on the underlying etiology and on the patient&rsquo;s volume status.</p>
{card('<b>Treatment of chloride-responsive metabolic alkalosis</b>', f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  <div style="background:{CREAM2};border-radius:8px;padding:10px 12px;border-top:3px solid {AMBER};">
    <p style="font-size:14px;font-weight:700;color:{DEEP};margin:0 0 5px 0;">Patients with volume depletion</p>
    <ul style="margin:0;padding:0 0 0 16px;color:{INK};font-size:12.5px;line-height:1.42;">
      <li style="margin-bottom:4px;">Infusion of <b style="color:{DANGER};">isotonic (0.9% NaCl) sodium chloride</b> to correct alkalosis and restore volume.</li>
      <li><b style="color:{DANGER};">Potassium chloride</b> (I.V. or oral) to correct the hypokalemia, if present.</li>
    </ul>
  </div>
  <div style="background:{CREAM2};border-radius:8px;padding:10px 12px;border-top:3px solid {AMBER};">
    <p style="font-size:14px;font-weight:700;color:{DEEP};margin:0 0 5px 0;">Patients with volume overload (edematous states)</p>
    <ul style="margin:0;padding:0 0 0 16px;color:{INK};font-size:12.5px;line-height:1.42;">
      <li style="margin-bottom:4px;"><b style="color:{DANGER};">Potassium chloride</b> (I.V. or oral) to correct the alkalosis and avoid volume overload.</li>
      <li><b style="color:{DANGER};">Carbonic anhydrase inhibitors</b> or <b style="color:{DANGER};">potassium-sparing diuretics</b> can be used to decrease volume and correct the alkalosis.</li>
    </ul>
  </div>
</div>
''', accent=RUST)}
<div style="height:10px;"></div>
{card('<b>Treatment of chloride-resistant metabolic alkalosis</b>',
  '<p style="font-size:13.5px;color:' + INK + ';margin:0;line-height:1.45;">Management is based on the <b style="color:' + DANGER + ';">specific cause</b> (e.g. treat hyperaldosteronism, stop diuretics, replace Mg<sup>2+</sup>/K<sup>+</sup>).</p>',
  accent=OLIVE)}
''')
write_slide(19, hdr('1B', 'Metabolic Alkalosis &mdash; Treatment') + s19)

# =====================================================================
# SLIDE 20 — Section divider 02 Hyponatremia
# =====================================================================
topics20 = f'''
<div style="display:flex;gap:12px;">
  <div style="background:{BROWN};border-radius:8px;padding:10px 14px;"><p style="font-size:14px;color:{ON_DARK};margin:0;font-weight:700;">Definition</p></div>
  <div style="background:{BROWN};border-radius:8px;padding:10px 14px;"><p style="font-size:14px;color:{ON_DARK};margin:0;font-weight:700;">Types</p></div>
  <div style="background:{BROWN};border-radius:8px;padding:10px 14px;"><p style="font-size:14px;color:{ON_DARK};margin:0;font-weight:700;">Causes</p></div>
  <div style="background:{BROWN};border-radius:8px;padding:10px 14px;"><p style="font-size:14px;color:{ON_DARK};margin:0;font-weight:700;">Algorithm</p></div>
  <div style="background:{BROWN};border-radius:8px;padding:10px 14px;"><p style="font-size:14px;color:{ON_DARK};margin:0;font-weight:700;">Treatment</p></div>
</div>
'''
write_slide(20, divider('02', 'Hyponatremia', 'Definition &middot; Pathological Effects &middot; Clinical Manifestations &middot; Classification &middot; Causes &middot; Diagnostic Algorithm &middot; Treatment', topics20))

# =====================================================================
# SLIDE 21 — HNa: Definition
# =====================================================================
s21 = content(f'''
{card('<b>Definition</b>',
  '<p style="font-size:14px;color:' + INK + ';margin:0;line-height:1.45;">A decrease in serum sodium concentration to a level <b style="color:' + DANGER + ';">below 135 mmol/L</b>.</p>',
  accent=DANGER)}
<div style="height:12px;"></div>
{card('<b>Dilutional hyponatremia</b>',
  '<p style="font-size:13.5px;color:' + INK + ';margin:0;line-height:1.45;">It is the <b style="color:' + DANGER + ';">most common form</b> of the disorder and is caused by <b style="color:' + DANGER + ';">water retention</b> rather than sodium depletion.</p>',
  accent=BROWN)}
<div style="height:12px;"></div>
{card('<b>Pseudohyponatremia</b>', f'''
<p style="font-size:13.5px;color:{INK};margin:0;line-height:1.45;">A <b style="color:{DANGER};">spuriously low</b> plasma sodium concentration; the measured sodium concentration is low, but the <b style="color:{DANGER};">true physiological plasma sodium concentration is normal</b>.</p>
<p style="font-size:13.5px;color:{INK};margin:6px 0 0 0;line-height:1.45;">Pseudohyponatremia can occur in any clinical situation in which the <b style="color:{RUST};">serum lipids or protein concentration is markedly increased</b> to maintain plasma osmolality.</p>
''', accent=OLIVE, bg=CREAM2)}
<div style="height:12px;"></div>
{note('Always check the <b>plasma osmolality</b>: in true hypotonic hyponatremia it is low; in pseudohyponatremia it remains normal (iso-osmolar) &mdash; the sodium is diluted by excess lipid/protein in the measuring cup.')}
''')
write_slide(21, hdr('02', 'Hyponatremia &mdash; Definition') + s21)

# =====================================================================
# SLIDE 22 — HNa: Pathological Effects & Clinical Manifestations
# =====================================================================
s22 = content(f'''
{card('<b>Pathological effects</b>', f'''
<ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:13.5px;line-height:1.45;">
  <li style="margin-bottom:6px;">Hyponatremia leads to <b style="color:{DANGER};">shift of water from the ECF to the ICF</b> compartments.</li>
  <li style="margin-bottom:6px;">Increased ICF volume leads to <b style="color:{DANGER};">cell swelling</b>.</li>
  <li>In the brain this leads to <b style="color:{DANGER};">brain oedema</b> and neurologic manifestations.</li>
</ul>
''', accent=DANGER)}
<div style="height:10px;"></div>
{card('<b>Clinical manifestations</b>', f'''
<ol style="margin:0;padding:0 0 0 20px;color:{INK};font-size:13.5px;line-height:1.45;">
  <li style="margin-bottom:6px;">Manifestations of the <b style="color:{RUST};">cause</b>.</li>
  <li style="margin-bottom:6px;">Manifestations of hyponatremia (<b style="color:{RUST};">neurologic symptoms</b>): changes in mental status including altered personality, lethargy, and confusion.</li>
  <li style="margin-bottom:6px;">As the serum sodium falls: <b style="color:{DANGER};">stupor, neuromuscular hyperexcitability, hyperreflexia, seizures, coma, and death</b> can result.</li>
</ol>
''', accent=BROWN)}
<div style="height:10px;"></div>
{warn('The severity of neurologic symptoms correlates well with the <b>severity</b> and the <b>rate of development</b> of hyponatremia.')}
''')
write_slide(22, hdr('02', 'Hyponatremia &mdash; Pathological Effects &amp; Clinical Manifestations') + s22)

# =====================================================================
# SLIDE 23 — HNa: Classification & Clinical Types (tree)
# =====================================================================
s23 = content(f'''
{card('<b>Classification and clinical types</b>', f'''
<ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:13.5px;line-height:1.45;">
  <li style="margin-bottom:6px;">Hyponatremia states can be classified into <b style="color:{DANGER};">three types</b> according to plasma osmolality (tonicity): <b style="color:{RUST};">Hypertonic, Isotonic and Hypotonic</b>.</li>
  <li style="margin-bottom:6px;">The first two types, <b style="color:{DANGER};">Hypertonic and Isotonic</b>, can be considered as <b style="color:{DANGER};">pseudohyponatremia</b> while the last type, <b style="color:{DANGER};">Hypotonic</b>, is considered <b style="color:{DANGER};">true hyponatremia</b>.</li>
  <li>Hypotonic Hyponatremia is classified into <b style="color:{RUST};">three subtypes</b> according to the <b style="color:{RUST};">volume status</b> of the patient.</li>
</ul>
''', accent=BROWN)}
<div style="height:10px;"></div>
<div style="display:flex;flex-direction:column;align-items:center;gap:8px;">
  <div style="background:{DEEP};border-radius:8px;padding:8px 26px;"><p style="font-size:15px;font-weight:700;color:{ON_DARK};margin:0;">Hyponatremia</p></div>
  <svg width="340" height="22" aria-hidden="true"><line x1="170" y1="0" x2="170" y2="22" stroke="{BROWN}" stroke-width="2"/></svg>
  <div style="display:flex;gap:30px;">
    <div style="display:flex;flex-direction:column;align-items:center;gap:6px;">
      <div style="background:{DANGER};border-radius:8px;padding:7px 18px;"><p style="font-size:13px;font-weight:700;color:{ON_DARK};margin:0;">Hypotonic</p></div>
      <svg width="30" height="16" aria-hidden="true"><line x1="15" y1="0" x2="15" y2="16" stroke="{BROWN}" stroke-width="2"/></svg>
      <div style="display:flex;gap:10px;">
        <div style="background:{CREAM2};border:2px solid {CARAMEL};border-radius:8px;padding:6px 12px;"><p style="font-size:12.5px;font-weight:700;color:{DEEP};margin:0;">Hypervolemic</p></div>
        <div style="background:{CREAM2};border:2px solid {CARAMEL};border-radius:8px;padding:6px 12px;"><p style="font-size:12.5px;font-weight:700;color:{DEEP};margin:0;">Euvolemic</p></div>
        <div style="background:{CREAM2};border:2px solid {CARAMEL};border-radius:8px;padding:6px 12px;"><p style="font-size:12.5px;font-weight:700;color:{DEEP};margin:0;">Hypovolemic</p></div>
      </div>
    </div>
    <div style="display:flex;flex-direction:column;justify-content:flex-start;">
      <div style="background:{OLIVE};border-radius:8px;padding:7px 18px;"><p style="font-size:13px;font-weight:700;color:{ON_DARK};margin:0;">Isotonic</p></div>
    </div>
    <div style="display:flex;flex-direction:column;justify-content:flex-start;">
      <div style="background:{OLIVE};border-radius:8px;padding:7px 18px;"><p style="font-size:13px;font-weight:700;color:{ON_DARK};margin:0;">Hypertonic</p></div>
    </div>
  </div>
</div>
<div style="height:8px;"></div>
{note('Isotonic &amp; hypertonic = pseudohyponatremia; hypotonic (true) hyponatremia &rarr; classify by volume status.')}
''')
write_slide(23, hdr('02', 'Hyponatremia &mdash; Classification &amp; Clinical Types') + s23)

# =====================================================================
# SLIDE 24 — HNa: Causes (3-column table)
# =====================================================================
s24 = content(f'''
<table style="width:100%;border-collapse:collapse;font-size:12.5px;">
  <tr style="background:{BROWN};color:{ON_DARK};">
    <th style="padding:9px 10px;border:1px solid {BROWN};text-align:left;">Hypervolemic Hyponatremia</th>
    <th style="padding:9px 10px;border:1px solid {BROWN};text-align:left;">Euvolemic Hyponatremia</th>
    <th style="padding:9px 10px;border:1px solid {BROWN};text-align:left;">Hypovolemic Hyponatremia</th>
  </tr>
  <tr style="background:{CREAM};">
    <td style="padding:9px 10px;border:1px solid #C9AC85;vertical-align:top;">
      <ul style="margin:0;padding:0 0 0 16px;line-height:1.45;">
        <li style="margin-bottom:5px;"><b style="color:{DANGER};">Heart failure</b></li>
        <li style="margin-bottom:5px;"><b style="color:{DANGER};">Liver failure</b></li>
        <li style="margin-bottom:5px;"><b style="color:{DANGER};">Oliguric AKI</b></li>
        <li style="margin-bottom:5px;"><b style="color:{DANGER};">CKD</b></li>
        <li style="margin-bottom:5px;"><b style="color:{DANGER};">Nephrotic syndrome</b></li>
        <li><b style="color:{DANGER};">Hypoalbuminemia</b></li>
      </ul>
    </td>
    <td style="padding:9px 10px;border:1px solid #C9AC85;vertical-align:top;">
      <ul style="margin:0;padding:0 0 0 16px;line-height:1.45;">
        <li style="margin-bottom:5px;"><b style="color:{RUST};">SIADH</b> (Syndrome of Inappropriate Anti Diuretic Hormone secretion).</li>
        <li style="margin-bottom:5px;"><b style="color:{RUST};">Nephrogenic syndrome of inappropriate antidiuresis.</b></li>
        <li style="margin-bottom:5px;"><b style="color:{RUST};">Primary polydipsia</b></li>
        <li style="margin-bottom:5px;"><b style="color:{RUST};">Thiazide Diuretics.</b></li>
        <li><b style="color:{RUST};">Hypothyroidism.</b></li>
      </ul>
    </td>
    <td style="padding:9px 10px;border:1px solid #C9AC85;vertical-align:top;">
      <ul style="margin:0;padding:0 0 0 16px;line-height:1.45;">
        <li style="margin-bottom:5px;"><b style="color:{OLIVE};">Extra-renal loss</b> (vomiting, diarrhea, hemorrhage, pancreatitis)</li>
        <li><b style="color:{OLIVE};">Renal loss</b> (diuretics, adrenal insufficiency, TIN, recovery phase of AKI)</li>
      </ul>
    </td>
  </tr>
</table>
<div style="height:12px;"></div>
{card('<b>How to read the table</b>',
  '<p style="font-size:13px;color:' + INK + ';margin:0;line-height:1.45;"><b style="color:' + DANGER + ';">Hypervolemic</b>: water excess with edema (edematous states). <b style="color:' + RUST + ';">Euvolemic</b>: no edema, SIADH is the prototype. <b style="color:' + OLIVE + ';">Hypovolemic</b>: sodium + water loss (extra-renal or renal).</p>',
  accent=AMBER, bg=CREAM2)}
''')
write_slide(24, hdr('02', 'Hyponatremia &mdash; Causes') + s24)

# =====================================================================
# SLIDE 25 — HNa: Diagnostic Algorithm
# =====================================================================
s25 = content(f'''
{card('<b>Diagnostic algorithm &mdash; types and causes of hyponatremia (flowchart)</b>', f'''
<div style="display:flex;flex-direction:column;gap:8px;">
  <div style="display:flex;align-items:center;gap:10px;">
    <div style="background:{DEEP};border-radius:8px;padding:7px 16px;"><p style="font-size:13px;font-weight:700;color:{ON_DARK};margin:0;">Hyponatremia</p></div>
    <span style="font-size:14px;color:{BROWN};font-weight:700;">&rarr;</span>
    <div style="background:{BROWN};border-radius:8px;padding:7px 16px;"><p style="font-size:13px;font-weight:700;color:{ON_DARK};margin:0;">Plasma osmolality</p></div>
  </div>
  <div style="display:flex;gap:14px;padding-left:30px;">
    <div style="flex:1;background:{CREAM};border-left:4px solid {DANGER};border-radius:8px;padding:9px 12px;">
      <p style="font-size:13px;font-weight:700;color:{DANGER};margin:0 0 5px 0;">Low osmolality &rarr; EVS (extracellular volume status)</p>
      <ul style="margin:0;padding:0 0 0 16px;font-size:12px;line-height:1.45;">
        <li style="margin-bottom:4px;"><b style="color:{DANGER};">Increased</b> &rarr; consider <b>heart failure, cirrhosis or nephrosis</b></li>
        <li style="margin-bottom:4px;"><b style="color:{DANGER};">Normal</b> &rarr; urine osmolality:
          <ul style="margin:2px 0 0 0;padding:0 0 0 14px;">
            <li>&lt; 100 mOsm/kg H<sub>2</sub>O &rarr; consider <b>polydipsia</b></li>
            <li>&gt; 100 mOsm/kg H<sub>2</sub>O &rarr; consider <b>SIADH, hypothyroidism, or hypocortisolism</b></li>
          </ul>
        </li>
        <li><b style="color:{DANGER};">Decreased</b> &rarr; consider <b>gastrointestinal fluid loss, Addison disease, salt-losing nephritis or cerebral salt wasting</b></li>
      </ul>
    </div>
    <div style="flex:1;background:{CREAM2};border-left:4px solid {OLIVE};border-radius:8px;padding:9px 12px;">
      <p style="font-size:13px;font-weight:700;color:{OLIVE};margin:0 0 5px 0;">Normal or high osmolality</p>
      <p style="font-size:12px;color:{INK};margin:0;line-height:1.45;">Consider <b style="color:{OLIVE};">hyperglycemia</b> or <b style="color:{OLIVE};">pseudohyponatremia</b></p>
    </div>
  </div>
</div>
''', accent=BROWN)}
<div style="height:10px;"></div>
{note('EVS = extracellular volume status. The algorithm begins with <b>plasma osmolality</b> to separate true (hypotonic) from pseudo hyponatremia, then uses <b>volume status</b> and <b>urine osmolality</b> to reach the cause.')}
''')
write_slide(25, hdr('02', 'Hyponatremia &mdash; Diagnostic Algorithm') + s25)

# =====================================================================
# SLIDE 26 — HNa: Treatment
# =====================================================================
s26 = content(f'''
{card('<b>General principles</b>', f'''
<ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:13.5px;line-height:1.45;">
  <li style="margin-bottom:6px;">Primary goal is to <b style="color:{DANGER};">control symptoms</b>, then to <b style="color:{DANGER};">correct Na<sup>+</sup> level</b>.</li>
  <li style="margin-bottom:6px;">Determine whether hyponatremia is <b style="color:{RUST};">acute or chronic</b>.</li>
  <li style="margin-bottom:6px;">Be careful of the <b style="color:{DANGER};">rate of correction</b> according to the rate of development (acute or chronic) to avoid <b style="color:{DANGER};">osmotic demyelination</b>, i.e. <b style="color:{DANGER};">central pontine myelinolysis</b>.</li>
  <li>The fluid of choice for correction depends on the <b style="color:{RUST};">volume status</b> of the patient.</li>
</ul>
''', accent=DANGER)}
<div style="height:10px;"></div>
{card('<b>Medications</b>', f'''
<table style="width:100%;border-collapse:collapse;font-size:13px;">
  <tr style="background:{BROWN};color:{ON_DARK};">
    <th style="padding:7px 10px;border:1px solid {BROWN};text-align:left;">Fluid / drug</th>
    <th style="padding:7px 10px;border:1px solid {BROWN};text-align:left;">Indicated states</th>
  </tr>
  <tr style="background:{CREAM};">
    <td style="padding:7px 10px;border:1px solid #C9AC85;"><b style="color:{DANGER};">Isotonic 0.9% NaCl</b></td>
    <td style="padding:7px 10px;border:1px solid #C9AC85;">Hypo- and euvolemic states</td>
  </tr>
  <tr style="background:{CREAM2};">
    <td style="padding:7px 10px;border:1px solid #C9AC85;"><b style="color:{DANGER};">Hypertonic 3% NaCl + Loop diuretics</b></td>
    <td style="padding:7px 10px;border:1px solid #C9AC85;">Hyper- and euvolemic states</td>
  </tr>
  <tr style="background:{CREAM};">
    <td style="padding:7px 10px;border:1px solid #C9AC85;"><b style="color:{DANGER};">Vasopressin receptor antagonists</b>: Conivaptan, Tolvaptan</td>
    <td style="padding:7px 10px;border:1px solid #C9AC85;">&mdash;</td>
  </tr>
</table>
''', accent=OLIVE)}
<div style="height:10px;"></div>
{warn('Too rapid correction of chronic hyponatremia may cause <b>osmotic demyelination syndrome (central pontine myelinolysis)</b> &mdash; correct slowly in chronic cases.')}
''')
write_slide(26, hdr('02', 'Hyponatremia &mdash; Treatment') + s26)

# =====================================================================
# SLIDE 27 — Section divider 03 Hypernatremia
# =====================================================================
topics27 = f'''
<div style="display:flex;gap:12px;">
  <div style="background:{BROWN};border-radius:8px;padding:10px 14px;"><p style="font-size:14px;color:{ON_DARK};margin:0;font-weight:700;">Definition</p></div>
  <div style="background:{BROWN};border-radius:8px;padding:10px 14px;"><p style="font-size:14px;color:{ON_DARK};margin:0;font-weight:700;">Pathogenesis</p></div>
  <div style="background:{BROWN};border-radius:8px;padding:10px 14px;"><p style="font-size:14px;color:{ON_DARK};margin:0;font-weight:700;">Types</p></div>
  <div style="background:{BROWN};border-radius:8px;padding:10px 14px;"><p style="font-size:14px;color:{ON_DARK};margin:0;font-weight:700;">Treatment</p></div>
</div>
'''
write_slide(27, divider('03', 'Hypernatremia', 'Definition &middot; Pathogenesis &middot; Pathological Effects &middot; Clinical Manifestations &middot; Classification &middot; Treatment', topics27))

# =====================================================================
# SLIDE 28 — HNa+: Definition & Pathogenesis
# =====================================================================
s28 = content(f'''
{card('<b>Definition</b>',
  '<p style="font-size:14px;color:' + INK + ';margin:0;line-height:1.45;">An increase in the serum sodium concentration to a level <b style="color:' + DANGER + ';">above 145 mmol/L</b>. Hypernatremia is a <b style="color:' + DANGER + ';">rare condition</b> and nearly always indicates a <b style="color:' + DANGER + ';">water deficit</b> that always reflects a state of <b style="color:' + DANGER + ';">hypertonicity</b> because sodium is an osmotically effective ECF solute.</p>',
  accent=DANGER)}
<div style="height:12px;"></div>
{card('<b>Pathogenesis</b>', f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
  <div style="background:{CREAM2};border-radius:8px;padding:9px 12px;border-top:3px solid {AMBER};">
    <p style="font-size:13px;color:{INK};margin:0;line-height:1.42;"><b style="color:{CARAMEL};">Water deficiency</b><br>Free water deficient states: <b style="color:{DANGER};">total body water deficit &gt; total body sodium deficit</b></p>
  </div>
  <div style="background:{CREAM2};border-radius:8px;padding:9px 12px;border-top:3px solid {AMBER};">
    <p style="font-size:13px;color:{INK};margin:0;line-height:1.42;"><b style="color:{CARAMEL};">Excess solute</b><br>Excess water loss or <b style="color:{DANGER};">excess sodium retention</b></p>
  </div>
</div>
<p style="font-size:13px;color:{INK};margin:8px 0 0 0;line-height:1.45;"><b style="color:{RUST};">Lacks normal physiologic response</b> to free water loss: <b style="color:{DANGER};">ADH secretion</b> and <b style="color:{DANGER};">thirst</b>.</p>
''', accent=BROWN)}
<div style="height:12px;"></div>
{note('Normally, <b>ADH</b> (conserving water) and <b>thirst</b> (drinking water) defend against hypernatremia &mdash; hypernatremia therefore occurs when these defenses fail (e.g. unconscious, hypodipsia, diabetes insipidus).')}
''')
write_slide(28, hdr('03', 'Hypernatremia &mdash; Definition &amp; Pathogenesis') + s28)

# =====================================================================
# SLIDE 29 — HNa+: Pathological Effects & Clinical Manifestations
# =====================================================================
s29 = content(f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card('<b>Pathological effects</b>', f'''
  <ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:13px;line-height:1.45;">
    <li style="margin-bottom:6px;">Hypernatremia leads to <b style="color:{DANGER};">shift of water from the ICF to the ECF</b> compartments.</li>
    <li style="margin-bottom:6px;">Reduction in the ICF volume and <b style="color:{DANGER};">cell shrinkage</b>.</li>
    <li>In the brain this leads to <b style="color:{DANGER};">neurological sequelae</b> and <b style="color:{DANGER};">intracerebral hemorrhage</b>, often punctate, but sometimes major blood vessels disruption may occur.</li>
  </ul>
  ''', accent=DANGER)}
  {card('<b>Clinical manifestations</b>', f'''
  <ol style="margin:0;padding:0 0 0 20px;color:{INK};font-size:13px;line-height:1.45;">
    <li style="margin-bottom:6px;">Manifestations of the <b style="color:{RUST};">underlying condition</b>.</li>
    <li style="margin-bottom:6px;">Manifestations of <b style="color:{RUST};">ECF volume disturbances</b>.</li>
    <li>Manifestations of <b style="color:{DANGER};">hypertonicity</b>: confusion, restlessness, hyperreflexia, spasticity, seizures and coma.</li>
  </ol>
  ''', accent=BROWN)}
</div>
<div style="height:12px;"></div>
{warn('Unlike hyponatremia (swelling), hypernatremia causes <b>cell shrinkage</b> &mdash; in the brain it can cause <b>intracerebral hemorrhage</b>.')}
''')
write_slide(29, hdr('03', 'Hypernatremia &mdash; Pathological Effects &amp; Clinical Manifestations') + s29)

# =====================================================================
# SLIDE 30 — HNa+: Classification (table)
# =====================================================================
s30 = content(f'''
<table style="width:100%;border-collapse:collapse;font-size:13px;">
  <tr style="background:{BROWN};color:{ON_DARK};">
    <th style="padding:9px 10px;border:1px solid {BROWN};text-align:left;width:22%;">Type</th>
    <th style="padding:9px 10px;border:1px solid {BROWN};text-align:left;width:40%;">Mechanism</th>
    <th style="padding:9px 10px;border:1px solid {BROWN};text-align:left;">Examples</th>
  </tr>
  <tr style="background:{CREAM};">
    <td style="padding:9px 10px;border:1px solid #C9AC85;font-weight:700;color:{DANGER};">Hypervolemic Hypernatremia</td>
    <td style="padding:9px 10px;border:1px solid #C9AC85;">Excessive IV sodium administration</td>
    <td style="padding:9px 10px;border:1px solid #C9AC85;"><b style="color:{RUST};">Hypertonic (3%) saline</b>, <b style="color:{RUST};">Sodium Bicarbonate</b></td>
  </tr>
  <tr style="background:{CREAM2};">
    <td style="padding:9px 10px;border:1px solid #C9AC85;font-weight:700;color:{DANGER};">Euvolemic Hypernatremia</td>
    <td style="padding:9px 10px;border:1px solid #C9AC85;">Renal water loss (low urine osmolality): <b style="color:{RUST};">Diabetes Insipidus</b><br>Extra-renal water loss (high urine osmolality): <b style="color:{RUST};">Rhabdomyolysis</b></td>
    <td style="padding:9px 10px;border:1px solid #C9AC85;">&mdash;</td>
  </tr>
  <tr style="background:{CREAM};">
    <td style="padding:9px 10px;border:1px solid #C9AC85;font-weight:700;color:{DANGER};">Hypovolemic Hypernatremia</td>
    <td style="padding:9px 10px;border:1px solid #C9AC85;">Renal sodium loss (high urine Na): <b style="color:{RUST};">Diuretics, Polyuric ATN</b><br>Extra-renal sodium loss (low urine Na): <b style="color:{RUST};">GIT, respiratory and skin loss</b></td>
    <td style="padding:9px 10px;border:1px solid #C9AC85;">&mdash;</td>
  </tr>
</table>
<div style="height:12px;"></div>
{card('<b>How to read the table</b>',
  '<p style="font-size:13px;color:' + INK + ';margin:0;line-height:1.45;"><b style="color:' + DANGER + ';">Hypervolemic</b>: sodium gain. <b style="color:' + RUST + ';">Euvolemic</b>: pure water loss (urine osmolality tells renal vs extra-renal). <b style="color:' + OLIVE + ';">Hypovolemic</b>: hypotonic fluid loss (urine Na tells renal vs extra-renal).</p>',
  accent=AMBER, bg=CREAM2)}
''')
write_slide(30, hdr('03', 'Hypernatremia &mdash; Classification &amp; Clinical Types') + s30)

# =====================================================================
# SLIDE 31 — HNa+: Treatment
# =====================================================================
s31 = content(f'''
{card('<b>General principles</b>', f'''
<ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:13.5px;line-height:1.45;">
  <li style="margin-bottom:6px;">Primary goal is to <b style="color:{DANGER};">control volume loss (resuscitation)</b>, then <b style="color:{DANGER};">correct Na<sup>+</sup> level (maintenance)</b>.</li>
  <li style="margin-bottom:6px;">During resuscitation, use fluid with volume of distribution confined to the <b style="color:{RUST};">intravascular compartment</b> (i.e. isotonic), while use <b style="color:{RUST};">hypotonic solutions</b> during maintenance.</li>
</ul>
''', accent=DANGER)}
<div style="height:10px;"></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card('<b>1. Rapid correction of severe ECF volume depletion (resuscitation)</b>',
    '<p style="font-size:12.5px;color:' + INK + ';margin:0;line-height:1.42;">Intravenous <b style="color:' + DANGER + ';">Isotonic 0.9% NaCl</b>: volume and rate of infusion is guided by <b style="color:' + RUST + ';">clinical parameters</b>.</p>',
    accent=RUST)}
  {card('<b>2. Gradual replacement of fluid deficit (maintenance)</b>', f'''
  <p style="font-size:12.5px;color:{INK};margin:0 0 5px 0;line-height:1.42;"><b style="color:{DANGER};">TBW deficit = 0.6 &times; premorbid weight (1 &minus; [140/Na]) + daily requirements</b></p>
  <p style="font-size:12.5px;color:{INK};margin:0;line-height:1.42;">Oral tap water in conscious patients or through an NG tube. If not feasible, use <b style="color:{RUST};">Intravenous 5% Glucose</b> or <b style="color:{RUST};">Half normal saline (0.45% NaCl)</b>.</p>
  ''', accent=OLIVE)}
</div>
<div style="height:10px;"></div>
{warn('Correct <b>gradually</b> over hours to days <b>(0.5 to 1 mmol/L/hour)</b> to avoid <b>brain oedema</b>.')}
''')
write_slide(31, hdr('03', 'Hypernatremia &mdash; Treatment') + s31)

# =====================================================================
# SLIDE 32 — Section divider 04 Hyperkalemia
# =====================================================================
topics32 = f'''
<div style="display:flex;gap:12px;">
  <div style="background:{BROWN};border-radius:8px;padding:10px 14px;"><p style="font-size:14px;color:{ON_DARK};margin:0;font-weight:700;">Definition</p></div>
  <div style="background:{BROWN};border-radius:8px;padding:10px 14px;"><p style="font-size:14px;color:{ON_DARK};margin:0;font-weight:700;">Causes</p></div>
  <div style="background:{BROWN};border-radius:8px;padding:10px 14px;"><p style="font-size:14px;color:{ON_DARK};margin:0;font-weight:700;">Manifestations</p></div>
  <div style="background:{BROWN};border-radius:8px;padding:10px 14px;"><p style="font-size:14px;color:{ON_DARK};margin:0;font-weight:700;">Treatment</p></div>
  <div style="background:{BROWN};border-radius:8px;padding:10px 14px;"><p style="font-size:14px;color:{ON_DARK};margin:0;font-weight:700;">ECG</p></div>
</div>
'''
write_slide(32, divider('04', 'Hyperkalemia', 'Definition &middot; Causes &middot; Manifestations &middot; Treatment &middot; ECG Changes', topics32))

# =====================================================================
# SLIDE 33 — HK+: Definition & Causes I (increased release)
# =====================================================================
s33 = content(f'''
{card('<b>Definition</b>',
  '<p style="font-size:14px;color:' + INK + ';margin:0;line-height:1.45;">An increase in S. potassium concentration to a level <b style="color:' + DANGER + ';">above 5.5 mmol/L</b>.</p>',
  accent=DANGER)}
<div style="height:12px;"></div>
{card('<b>I) Increased potassium release from the cells</b>', f'''
<ol style="margin:0;padding:0 0 0 20px;color:{INK};font-size:13px;line-height:1.45;">
  <li style="margin-bottom:6px;"><b style="color:{DANGER};">Pseudo-hyperkalemia</b>: increased blood cell destruction <i>in vitro</i> (e.g. hemolysis) leading to K<sup>+</sup> release from the damaged cells &mdash; when blood samples are left for a long time at low temperature, especially in patients with <b style="color:{RUST};">polycythemia or leukocytosis</b>.</li>
  <li style="margin-bottom:6px;"><b style="color:{DANGER};">Metabolic acidosis</b></li>
  <li style="margin-bottom:6px;"><b style="color:{DANGER};">Insulin deficiency</b>, hyperglycemia, and hyperosmolality</li>
  <li style="margin-bottom:6px;"><b style="color:{DANGER};">Increased tissue catabolism</b>: e.g. trauma, cytotoxic and radiation therapy for malignancy (<b style="color:{RUST};">tumor lysis syndrome</b>).</li>
  <li style="margin-bottom:6px;"><b style="color:{DANGER};">&beta;-adrenergic blockade</b></li>
  <li style="margin-bottom:6px;"><b style="color:{DANGER};">Exercise</b></li>
  <li><b style="color:{DANGER};">Digitalis overdose.</b></li>
</ol>
''', accent=BROWN)}
''')
write_slide(33, hdr('04', 'Hyperkalemia &mdash; Definition &amp; Causes (I. Increased Release)') + s33)

# =====================================================================
# SLIDE 34 — HK+: Causes II (reduced urinary excretion)
# =====================================================================
s34 = content(f'''
{card('<b>II) Reduced urinary potassium excretion</b>', f'''
<ol style="margin:0;padding:0 0 0 20px;color:{INK};font-size:13.5px;line-height:1.45;">
  <li style="margin-bottom:7px;"><b style="color:{DANGER};">Renal failure</b>; due to decreased K<sup>+</sup> excretion.</li>
  <li style="margin-bottom:7px;"><b style="color:{DANGER};">Hypoaldosteronism</b> (primary and secondary).</li>
  <li style="margin-bottom:7px;"><b style="color:{DANGER};">Circulatory volume depletion</b>.</li>
  <li style="margin-bottom:7px;"><b style="color:{DANGER};">Type (IV) RTA</b>.</li>
  <li style="margin-bottom:7px;"><b style="color:{DANGER};">Drugs:</b>
    <ul style="margin:3px 0 0 0;padding:0 0 0 18px;font-size:12.5px;line-height:1.45;">
      <li style="margin-bottom:5px;"><b style="color:{RUST};">ACEIs, ARBs, NSAIDs, Cyclosporin</b>; cause impaired angiotensin II induced aldosterone secretion &rarr; hypoaldosteronism &rarr; K<sup>+</sup> retention.</li>
      <li><b style="color:{RUST};">Potassium sparing diuretics (spironolactone)</b>, <b style="color:{RUST};">trimethoprim antibiotic</b>, and <b style="color:{RUST};">heparin</b> &rarr; aldosterone resistance &rarr; K<sup>+</sup> retention.</li>
    </ul>
  </li>
</ol>
''', accent=DANGER)}
<div style="height:10px;"></div>
{warn('Two drug mechanisms of K<sup>+</sup> retention: <b>impaired aldosterone secretion</b> (ACEIs / ARBs / NSAIDs / cyclosporin) vs <b>aldosterone resistance</b> (spironolactone / trimethoprim / heparin).')}
''')
write_slide(34, hdr('04', 'Hyperkalemia &mdash; Causes (II. Reduced Urinary Excretion)') + s34)

# =====================================================================
# SLIDE 35 — HK+: Manifestations
# =====================================================================
s35 = content(f'''
{card('<b>Manifestations</b>', f'''
<p style="font-size:13.5px;color:{INK};margin:0 0 8px 0;line-height:1.45;">Elevation of the extracellular potassium concentrations results in a <b style="color:{DANGER};">decrease in cell membrane excitability</b> (especially nerve, muscle and cardiac cells) which is manifested by;</p>
<ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:13.5px;line-height:1.5;">
  <li style="margin-bottom:8px;"><b style="color:{DANGER};">Muscle weakness or paralysis</b>, irritability, anxiety, paraesthesia, and/or</li>
  <li><b style="color:{DANGER};">Impaired cardiac conduction</b>, irregular pulse and <b style="color:{DANGER};">cardiac standstill</b> (if hyperkalemia is sudden or severe).</li>
</ul>
''', accent=DANGER)}
<div style="height:12px;"></div>
{card('<b>Key concept &mdash; the membrane effect</b>',
  '<p style="font-size:13px;color:' + INK + ';margin:0;line-height:1.45;">High extracellular K<sup>+</sup> <b style="color:' + DANGER + ';">depolarizes</b> the resting membrane potential, making nerve/muscle/cardiac cells <b style="color:' + DANGER + ';">less excitable</b> &mdash; hence weakness and cardiac conduction blocks.</p>',
  accent=AMBER, bg=CREAM2)}
''')
write_slide(35, hdr('04', 'Hyperkalemia &mdash; Manifestations') + s35)

# =====================================================================
# SLIDE 36 — HK+: Treatment 1 & 2
# =====================================================================
s36 = content(f'''
{warn('Urgent therapy is indicated when serious manifestations are present such as: <b>muscle weakness or paralysis, cardiac conduction abnormalities, cardiac arrhythmias, and/or serum K<sup>+</sup> concentration &ge; 7 mmol/L</b>.')}
<div style="height:10px;"></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card('<b>1. Stabilize the myocardial cell membrane</b>', f'''
  <p style="font-size:13px;color:{INK};margin:0;line-height:1.45;">I.V. <b style="color:{DANGER};">calcium gluconate</b>, <b style="color:{DANGER};">10 mg in 10 ml over 10 minutes</b>, as calcium antagonizes the cellular effects of hyperkalemia (a <b style="color:{RUST};">physiologic antidote</b>).</p>
  ''', accent=DANGER)}
  {card('<b>2. Drive extracellular K<sup>+</sup> into the cells</b> (increase Na<sup>+</sup>/K<sup>+</sup>-ATPase pump activity)', f'''
  <table style="width:100%;border-collapse:collapse;font-size:11.5px;">
    <tr style="background:{BROWN};color:{ON_DARK};">
      <th style="padding:5px 7px;border:1px solid {BROWN};text-align:left;">Agent</th>
      <th style="padding:5px 7px;border:1px solid {BROWN};text-align:left;">Dose</th>
      <th style="padding:5px 7px;border:1px solid {BROWN};text-align:left;">Notes</th>
    </tr>
    <tr style="background:{CREAM};">
      <td style="padding:5px 7px;border:1px solid #C9AC85;"><b style="color:{DANGER};">&beta;2 agonists</b> (albuterol, salbutamol)</td>
      <td style="padding:5px 7px;border:1px solid #C9AC85;">10 to 20 mg inhaled over 10 minutes</td>
      <td style="padding:5px 7px;border:1px solid #C9AC85;">Peak effect in 90 minutes. Contraindicated in patients with ischemic heart diseases</td>
    </tr>
    <tr style="background:{CREAM2};">
      <td style="padding:5px 7px;border:1px solid #C9AC85;"><b style="color:{DANGER};">Insulin and glucose</b></td>
      <td style="padding:5px 7px;border:1px solid #C9AC85;">One ampule dextrose 50% concentration with 5&ndash;10 units of regular insulin I.V.</td>
      <td style="padding:5px 7px;border:1px solid #C9AC85;">Peak effect within 60 min, lasts several hours. Side effect: <b style="color:{RUST};">hypoglycemia</b></td>
    </tr>
    <tr style="background:{CREAM};">
      <td style="padding:5px 7px;border:1px solid #C9AC85;"><b style="color:{DANGER};">Sodium bicarbonate (NaHCO<sub>3</sub>)</b></td>
      <td style="padding:5px 7px;border:1px solid #C9AC85;">&mdash;</td>
      <td style="padding:5px 7px;border:1px solid #C9AC85;">Rapid effect within few minutes but <b style="color:{RUST};">not long lasting</b></td>
    </tr>
  </table>
  ''', accent=OLIVE, bg=CREAM2)}
</div>
''')
write_slide(36, hdr('04', 'Hyperkalemia &mdash; Treatment (1. Membrane &amp; 2. Cellular Shift)') + s36)

# =====================================================================
# SLIDE 37 — HK+: Treatment 3 & 4 (removal + monitoring)
# =====================================================================
s37 = content(f'''
{card('<b>3. Removal of potassium from the body</b>', f'''
<table style="width:100%;border-collapse:collapse;font-size:12.5px;">
  <tr style="background:{BROWN};color:{ON_DARK};">
    <th style="padding:7px 10px;border:1px solid {BROWN};text-align:left;width:26%;">Method</th>
    <th style="padding:7px 10px;border:1px solid {BROWN};text-align:left;">Mechanism / Notes</th>
  </tr>
  <tr style="background:{CREAM};">
    <td style="padding:7px 10px;border:1px solid #C9AC85;"><b style="color:{DANGER};">1- Loop diuretics</b></td>
    <td style="padding:7px 10px;border:1px solid #C9AC85;">Lead to K<sup>+</sup> loss in the urine by inhibiting Na/K/Cl transporter in loop of Henle.</td>
  </tr>
  <tr style="background:{CREAM2};">
    <td style="padding:7px 10px;border:1px solid #C9AC85;"><b style="color:{DANGER};">2- Potassium exchange resins</b> (sodium polystyrene sulfate)</td>
    <td style="padding:7px 10px;border:1px solid #C9AC85;">Given orally or per rectum. Exchanges Na<sup>+</sup> for K<sup>+</sup> and binds it in the gut (primarily in large intestine) &rarr; decreasing total body K<sup>+</sup>. K<sup>+</sup> is removed in the stool, 8&ndash;12 hours after administration. <b style="color:{RUST};">Side effects: intestinal necrosis / gangrene</b>.</td>
  </tr>
  <tr style="background:{CREAM};">
    <td style="padding:7px 10px;border:1px solid #C9AC85;"><b style="color:{DANGER};">3- Hemodialysis</b></td>
    <td style="padding:7px 10px;border:1px solid #C9AC85;">In <b style="color:{RUST};">refractory and emergency cases</b> (i.e. high K<sup>+</sup> level &gt; 7 mmol/L or ECG changes).</td>
  </tr>
</table>
''', accent=DANGER)}
<div style="height:10px;"></div>
{card('<b>4- Monitoring</b>', f'''
<ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:13px;line-height:1.45;">
  <li style="margin-bottom:5px;">Continuous <b style="color:{DANGER};">cardiac monitoring</b> and serial ECGs.</li>
  <li>Measurement of <b style="color:{DANGER};">serum potassium at 1&ndash;2 hours</b> after the initiation of therapy.</li>
</ul>
''', accent=OLIVE, bg=CREAM2)}
''')
write_slide(37, hdr('04', 'Hyperkalemia &mdash; Treatment (3. Removal &amp; 4. Monitoring)') + s37)

# =====================================================================
# SLIDE 38 — HK+: ECG changes
# =====================================================================
s38 = content(f'''
{card('<b>ECG changes of hyperkalemia</b>', f'''
<p style="font-size:14px;color:{INK};margin:0 0 8px 0;line-height:1.5;">With rising serum K<sup>+</sup>, the ECG shows a <b style="color:{DANGER};">progressive sequence</b>:</p>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;">
  <div style="background:{CREAM2};border-radius:8px;padding:9px 12px;border-top:3px solid {DANGER};"><p style="font-size:12.5px;color:{INK};margin:0;line-height:1.4;"><b style="color:{DANGER};">Early</b><br>Tall peaked T waves</p></div>
  <div style="background:{CREAM2};border-radius:8px;padding:9px 12px;border-top:3px solid {DANGER};"><p style="font-size:12.5px;color:{INK};margin:0;line-height:1.4;"><b style="color:{DANGER};">Intermediate</b><br>Prolonged PR intervals &middot; ST segment depression &middot; loss of P waves</p></div>
  <div style="background:{CREAM2};border-radius:8px;padding:9px 12px;border-top:3px solid {DANGER};"><p style="font-size:12.5px;color:{INK};margin:0;line-height:1.4;"><b style="color:{DANGER};">Late / severe</b><br>Widened QRS &middot; VT &middot; cardiac standstill</p></div>
</div>
''', accent=DANGER)}
<div style="height:12px;"></div>
<div style="display:flex;gap:12px;align-items:center;justify-content:center;">
  <div style="flex:1;background:{CREAM};border-radius:8px;padding:10px 14px;border-left:4px solid {BROWN};">
    <p style="font-size:12.5px;color:{SOFT};margin:0;font-style:italic;">Figure: ECG changes of severe hyperkalemia.</p>
    <p style="font-size:12px;color:{INK};margin:6px 0 0 0;line-height:1.4;">Tall peaked T waves &rarr; PR prolongation &rarr; P wave flattening/loss &rarr; QRS widening &rarr; sine wave &rarr; VT/VF &rarr; standstill.</p>
  </div>
</div>
<div style="height:10px;"></div>
{warn('ECG changes are an <b>emergency trigger</b> &mdash; treat immediately even while awaiting the lab K<sup>+</sup> result.')}
''')
write_slide(38, hdr('04', 'Hyperkalemia &mdash; ECG Changes') + s38)

# =====================================================================
# SLIDE 39 — Section divider 05 Hypokalemia
# =====================================================================
topics39 = f'''
<div style="display:flex;gap:12px;">
  <div style="background:{BROWN};border-radius:8px;padding:10px 14px;"><p style="font-size:14px;color:{ON_DARK};margin:0;font-weight:700;">Definition</p></div>
  <div style="background:{BROWN};border-radius:8px;padding:10px 14px;"><p style="font-size:14px;color:{ON_DARK};margin:0;font-weight:700;">Causes</p></div>
  <div style="background:{BROWN};border-radius:8px;padding:10px 14px;"><p style="font-size:14px;color:{ON_DARK};margin:0;font-weight:700;">Syndromes</p></div>
  <div style="background:{BROWN};border-radius:8px;padding:10px 14px;"><p style="font-size:14px;color:{ON_DARK};margin:0;font-weight:700;">Manifestations</p></div>
  <div style="background:{BROWN};border-radius:8px;padding:10px 14px;"><p style="font-size:14px;color:{ON_DARK};margin:0;font-weight:700;">Treatment</p></div>
</div>
'''
write_slide(39, divider('05', 'Hypokalemia', 'Definition &middot; Causes &middot; Associated Syndromes &middot; Manifestations &middot; ECG &middot; Treatment', topics39))

# =====================================================================
# SLIDE 40 — Hk+: Definition & Causes
# =====================================================================
s40 = content(f'''
{card('<b>Definition</b>',
  '<p style="font-size:14px;color:' + INK + ';margin:0;line-height:1.45;">A decrease in the S. potassium concentration to a level <b style="color:' + DANGER + ';">below 3.5 mmol/L</b>.</p>',
  accent=DANGER)}
<div style="height:10px;"></div>
{card('<b>Causes</b>', f'''
<ol style="margin:0;padding:0 0 0 20px;color:{INK};font-size:12.5px;line-height:1.42;">
  <li style="margin-bottom:5px;"><b style="color:{DANGER};">Spurious hypokalemia;</b> occurs when a blood sample is kept in the blood tube for a long period at room temperature. This allows K<sup>+</sup> to enter the cells &rarr; falsely lower serum K<sup>+</sup> level. Particularly seen with <b style="color:{RUST};">marked leukocytosis</b> and when <b style="color:{RUST};">insulin is given just prior to blood drawing</b>.</li>
  <li style="margin-bottom:5px;"><b style="color:{DANGER};">Decreased K<sup>+</sup> intake</b> (normal daily K<sup>+</sup> intake = 40 &ndash; 120 mmol).</li>
  <li style="margin-bottom:5px;"><b style="color:{DANGER};">Shift of K<sup>+</sup> into the cells;</b> e.g. alkalosis, insulin therapy, &beta; agonists and stress.</li>
  <li style="margin-bottom:5px;"><b style="color:{DANGER};">Renal K<sup>+</sup> loss;</b> e.g.
    <ul style="margin:2px 0 0 0;padding:0 0 0 18px;font-size:12px;line-height:1.4;">
      <li style="margin-bottom:3px;"><b style="color:{RUST};">Diuretics</b> &rarr; activates renin angiotensin aldosterone system (RAAS) hyperaldosteronism &rarr; salt retention and potassium loss.</li>
      <li style="margin-bottom:3px;"><b style="color:{RUST};">Hyperaldosteronism</b> / steroids therapy.</li>
      <li style="margin-bottom:3px;"><b style="color:{RUST};">Proximal RTA</b></li>
      <li style="margin-bottom:3px;"><b style="color:{RUST};">Hypomagnesaemia.</b></li>
      <li><b style="color:{RUST};">Polyuria.</b></li>
    </ul>
  </li>
  <li><b style="color:{DANGER};">Extra-renal K<sup>+</sup> loss;</b> e.g. loss of gastric fluid (persistent vomiting and gastric aspiration) leads to:
    <ul style="margin:2px 0 0 0;padding:0 0 0 18px;font-size:12px;line-height:1.4;">
      <li style="margin-bottom:3px;">Loss of H<sup>+</sup> &rarr; increases plasma bicarbonate &rarr; <b style="color:{RUST};">alkalosis</b> &rarr; &uarr; cellular K<sup>+</sup> uptake.</li>
      <li>Coexisting <b style="color:{RUST};">volume depletion</b> &rarr; increases aldosterone secretion.</li>
    </ul>
  </li>
</ol>
''', accent=BROWN)}
''')
write_slide(40, hdr('05', 'Hypokalemia &mdash; Definition &amp; Causes') + s40)

# =====================================================================
# SLIDE 41 — Hk+: NB — Associated Syndromes
# =====================================================================
s41 = content(f'''
{card('<b>NB: Syndromes associated with hypokalemia</b>', f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
  <div style="background:{CREAM2};border-radius:8px;padding:9px 12px;border-top:3px solid {DANGER};grid-column:1 / span 2;">
    <p style="font-size:13.5px;font-weight:700;color:{DEEP};margin:0 0 4px 0;">Hypokalemic periodic paralysis</p>
    <ul style="margin:0;padding:0 0 0 16px;color:{INK};font-size:12px;line-height:1.4;">
      <li style="margin-bottom:3px;">Results from a defect in a <b style="color:{DANGER};">voltage-gated calcium channel</b>.</li>
      <li>Triggered by; <b style="color:{RUST};">strenuous exercise followed by rest, high carbohydrates or sodium meals, and sudden changes in temperature</b>.</li>
    </ul>
  </div>
  <div style="background:{CREAM2};border-radius:8px;padding:9px 12px;border-top:3px solid {RUST};">
    <p style="font-size:13.5px;font-weight:700;color:{DEEP};margin:0 0 4px 0;">Bartter&rsquo;s syndrome</p>
    <ul style="margin:0;padding:0 0 0 16px;color:{INK};font-size:12px;line-height:1.4;">
      <li style="margin-bottom:3px;">The defect is impaired <b style="color:{DANGER};">Na Cl reabsorption in the loop of Henle</b>.</li>
      <li style="margin-bottom:3px;">Salt loss &rarr; volume depletion and activation of the RAAS; findings are <b style="color:{RUST};">similar to administration of a loop diuretic</b>.</li>
      <li style="margin-bottom:3px;"><b style="color:{RUST};">Increased urinary calcium.</b></li>
      <li>The syndrome is usually diagnosed in <b style="color:{RUST};">childhood</b>, sometimes associated with growth and mental retardation.</li>
    </ul>
  </div>
  <div style="background:{CREAM2};border-radius:8px;padding:9px 12px;border-top:3px solid {OLIVE};">
    <p style="font-size:13.5px;font-weight:700;color:{DEEP};margin:0 0 4px 0;">Gitelman&rsquo;s syndrome</p>
    <ul style="margin:0;padding:0 0 0 16px;color:{INK};font-size:12px;line-height:1.4;">
      <li style="margin-bottom:3px;">The defect is in the <b style="color:{DANGER};">Na Cl transporter</b>.</li>
      <li>Findings <b style="color:{RUST};">mimic administration of a thiazide diuretic</b>.</li>
    </ul>
  </div>
</div>
''', accent=BROWN)}
<div style="height:10px;"></div>
{note('Compare: <b>Bartter</b> = loop of Henle defect (like a loop diuretic, hypercalciuria); <b>Gitelman</b> = distal Na-Cl transporter defect (like a thiazide).')}
''')
write_slide(41, hdr('05', 'Hypokalemia &mdash; NB: Associated Syndromes') + s41)

# =====================================================================
# SLIDE 42 — Hk+: Manifestations (incl. ECG)
# =====================================================================
s42 = content(f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card('<b>Symptoms</b>', f'''
  <ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:12.5px;line-height:1.4;">
    <li style="margin-bottom:4px;"><b style="color:{RUST};">GIT;</b> nausea, vomiting, abdominal cramps, constipation.</li>
    <li style="margin-bottom:4px;"><b style="color:{RUST};">Muscles;</b> muscle weakness or cramps, paralysis.</li>
    <li style="margin-bottom:4px;"><b style="color:{RUST};">CNS;</b> paraesthesia, psychosis, delirium, hallucinations, depression.</li>
    <li style="margin-bottom:4px;"><b style="color:{RUST};">Renal;</b> polyuria, nocturia &rarr; polydipsia.</li>
    <li><b style="color:{RUST};">Cardiac;</b> palpitation.</li>
  </ul>
  ''', accent=BROWN)}
  {card('<b>Signs</b>', f'''
  <ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:12.5px;line-height:1.4;">
    <li style="margin-bottom:4px;"><b style="color:{RUST};">GIT;</b> ileus.</li>
    <li style="margin-bottom:4px;"><b style="color:{RUST};">CVS;</b> hypotension, bradycardia or tachycardia, premature beats, arrhythmias.</li>
    <li style="margin-bottom:4px;"><b style="color:{RUST};">Respiratory;</b> hypoventilation, respiratory distress, respiratory failure.</li>
    <li><b style="color:{RUST};">CNS;</b> mental changes (e.g. lethargy), decreased muscle strength, fasciculation, tetany, decreased tendon reflexes.</li>
  </ul>
  ''', accent=DANGER)}
</div>
<div style="height:12px;"></div>
{card('<b>ECG changes</b>',
  '<p style="font-size:13.5px;color:' + INK + ';margin:0;line-height:1.45;"><b style="color:' + DANGER + ';">ST- segments and T- waves depression</b> with <b style="color:' + DANGER + ';">prominent U- waves</b>. <span style="font-style:italic;color:' + SOFT + ';">(Figure: ECG changes of hypokalemia.)</span></p>',
  accent=AMBER, bg=CREAM2)}
''')
write_slide(42, hdr('05', 'Hypokalemia &mdash; Manifestations') + s42)

# =====================================================================
# SLIDE 43 — Hk+: Treatment
# =====================================================================
s43 = content(f'''
{card('<b>Treatment</b>', f'''
<ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:13.5px;line-height:1.45;">
  <li style="margin-bottom:7px;"><b style="color:{DANGER};">Control the cause.</b></li>
  <li style="margin-bottom:7px;"><b style="color:{DANGER};">Potassium therapy:</b>
    <ul style="margin:3px 0 0 0;padding:0 0 0 18px;font-size:12.5px;line-height:1.45;">
      <li style="margin-bottom:5px;"><b style="color:{RUST};">I.V. Potassium chloride infusion</b>, when serum K<sup>+</sup> is <b style="color:{DANGER};">&lt; 2.5 mmol/L</b>. The maximal rate of correction should be <b style="color:{DANGER};">less than 20 mmol/hour</b>.</li>
      <li><b style="color:{RUST};">Oral potassium</b> is the preferred route for K<sup>+</sup> depletion in other cases.</li>
    </ul>
  </li>
</ul>
''', accent=DANGER)}
<div style="height:10px;"></div>
{note('Cellular shift of K<sup>+</sup> into the cells requires <b>less potassium</b> to correct than hypokalemia from potassium loss.')}
<div style="height:10px;"></div>
{card('<b>Monitoring</b>', f'''
<ul style="margin:0;padding:0 0 0 18px;color:{INK};font-size:13px;line-height:1.45;">
  <li style="margin-bottom:5px;">Check <b style="color:{DANGER};">serum Mg levels</b>, since it is difficult to restore potassium if the former is low.</li>
  <li><b style="color:{DANGER};">ECG monitoring</b> is required.</li>
</ul>
''', accent=OLIVE, bg=CREAM2)}
''')
write_slide(43, hdr('05', 'Hypokalemia &mdash; Treatment') + s43)

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
  <p style="font-size:24px;color:{AMBER};margin:10px 0 0 0;">Electrolytes &amp; Acid-Base Disturbances</p>
  <div style="width:70px;height:4px;background:{AMBER};margin:24px 0 18px 0;"></div>
  <p style="font-size:18px;color:{ON_DARK};margin:0;font-weight:400;">References</p>
  <p style="font-size:16px;color:{ON_DARK};margin:8px 0 0 0;opacity:0.85;">&bull; Principles of Nephrology &mdash; <b>Pages 51&ndash;55</b> (Acid-Base Balance)</p>
  <p style="font-size:16px;color:{ON_DARK};margin:4px 0 0 0;opacity:0.85;">&bull; Principles of Nephrology &mdash; <b>Pages 55&ndash;58</b> (Hyponatremia)</p>
  <p style="font-size:16px;color:{ON_DARK};margin:4px 0 0 0;opacity:0.85;">&bull; Principles of Nephrology &mdash; <b>Pages 58&ndash;59</b> (Hypernatremia)</p>
  <p style="font-size:16px;color:{ON_DARK};margin:4px 0 0 0;opacity:0.85;">&bull; Principles of Nephrology &mdash; <b>Pages 59&ndash;61</b> (Hyperkalemia)</p>
  <p style="font-size:16px;color:{ON_DARK};margin:4px 0 0 0;opacity:0.85;">&bull; Principles of Nephrology &mdash; <b>Pages 61&ndash;63</b> (Hypokalemia)</p>
</div>
<div style="position:absolute;bottom:28px;left:80px;z-index:10;">
  <p style="font-size:17px;color:{ON_DARK};margin:0;opacity:0.95;">Dr. Hassan Abd-Elhady &mdash; Menoufia University</p>
</div>
'''
write_slide(44, end, bg=DEEP, badge_num=None)

# ---------------- Index ----------------
index_items = [
    (1, 'Cover &mdash; Electrolytes &amp; Acid-Base Disturbances'),
    (2, 'Table of Contents'),
    (3, 'Section 01 &mdash; Acid-Base Balance (divider)'),
    (4, 'Overview &mdash; Primary Events'),
    (5, 'Overview &mdash; Body Compensation Table'),
    (6, 'Section 1A &mdash; Metabolic Acidosis (divider)'),
    (7, 'MA &mdash; Definition &amp; The Anion Gap'),
    (8, 'MA &mdash; Anion Gap Formula &amp; Types'),
    (9, 'MA &mdash; Causes &amp; Classification'),
    (10, 'MA &mdash; Clinical Features'),
    (11, 'MA &mdash; Investigations'),
    (12, 'MA &mdash; Treatment'),
    (13, 'Section 1B &mdash; Metabolic Alkalosis (divider)'),
    (14, 'MAlk &mdash; Definition &amp; Classification'),
    (15, 'MAlk &mdash; Causes (Chloride-responsive &amp; Other)'),
    (16, 'MAlk &mdash; Causes (Chloride-resistant)'),
    (17, 'MAlk &mdash; Clinical Features'),
    (18, 'MAlk &mdash; Investigations'),
    (19, 'MAlk &mdash; Treatment'),
    (20, 'Section 02 &mdash; Hyponatremia (divider)'),
    (21, 'Hyponatremia &mdash; Definition'),
    (22, 'Hyponatremia &mdash; Pathological Effects &amp; Clinical Manifestations'),
    (23, 'Hyponatremia &mdash; Classification &amp; Clinical Types'),
    (24, 'Hyponatremia &mdash; Causes'),
    (25, 'Hyponatremia &mdash; Diagnostic Algorithm'),
    (26, 'Hyponatremia &mdash; Treatment'),
    (27, 'Section 03 &mdash; Hypernatremia (divider)'),
    (28, 'Hypernatremia &mdash; Definition &amp; Pathogenesis'),
    (29, 'Hypernatremia &mdash; Pathological Effects &amp; Clinical Manifestations'),
    (30, 'Hypernatremia &mdash; Classification &amp; Clinical Types'),
    (31, 'Hypernatremia &mdash; Treatment'),
    (32, 'Section 04 &mdash; Hyperkalemia (divider)'),
    (33, 'Hyperkalemia &mdash; Definition &amp; Causes (I. Increased Release)'),
    (34, 'Hyperkalemia &mdash; Causes (II. Reduced Urinary Excretion)'),
    (35, 'Hyperkalemia &mdash; Manifestations'),
    (36, 'Hyperkalemia &mdash; Treatment (1. Membrane &amp; 2. Cellular Shift)'),
    (37, 'Hyperkalemia &mdash; Treatment (3. Removal &amp; 4. Monitoring)'),
    (38, 'Hyperkalemia &mdash; ECG Changes'),
    (39, 'Section 05 &mdash; Hypokalemia (divider)'),
    (40, 'Hypokalemia &mdash; Definition &amp; Causes'),
    (41, 'Hypokalemia &mdash; NB: Associated Syndromes'),
    (42, 'Hypokalemia &mdash; Manifestations'),
    (43, 'Hypokalemia &mdash; Treatment'),
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
<title>Electrolytes &amp; Acid-Base Slide Deck &mdash; Index</title>
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
<h1>Electrolytes &amp; Acid-Base Disturbances &mdash; Slide Deck Index</h1>
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
