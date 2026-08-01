#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chronic Kidney Disease & RRT — full-content HTML slides (light mode, brown harmony palette)
Pipeline: medical1 (light cards) adapted with a warm brown palette:
  bg cream-brown light, deep chocolate text, caramel/amber/terracotta/olive harmony accents,
  high-contrast dark blocks for important information.
960x540, Times New Roman, inline CSS, page badge, no summarization.
"""

import os, html as H

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'slides')
os.makedirs(OUT, exist_ok=True)

# ---------------------------------------------------------------- palette ---
BG    = '#F1E8D9'   # warm cream-brown background (light mode)
CARD  = '#FBF4E7'   # card background
CARD2 = '#F5EAD6'   # alt card
INK   = '#3A2B22'   # main text — deep warm brown
HEAD  = '#4B3223'   # headings — dark chocolate
SUB   = '#7A5C3E'   # muted subtitle brown
CARAM = '#B97A2E'   # caramel — primary accent (harmony)
AMBER = '#D9A45B'   # amber — highlight
TERRA = '#A84A2A'   # terracotta — emphasis / warning (contrast)
OLIVE = '#6E7A48'   # olive — secondary harmony accent
CREAM = '#FFF6E4'   # cream — text on dark blocks
DARK  = '#2E2118'   # dark chocolate — contrast blocks for important info
DARK2 = '#3D2C20'   # slightly lighter chocolate
LINEC = '#E2D3B8'   # table border line

# ---------------------------------------------------------------- wrapper ---
TMPL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
html, body { margin:0; padding:0; width:100%; height:100%; overflow:hidden; display:flex; justify-content:center; align-items:center; background:#000; }
.slide-content { width:960px; height:540px; position:relative; transform-origin:center center; }
</style>
<script>
function scaleSlide(){var s=document.querySelector('.slide-content');if(!s)return;var sx=window.innerWidth/960;var sy=window.innerHeight/540;var sc=Math.min(sx,sy);s.style.width='960px';s.style.height='540px';s.style.transform='scale('+sc+')';s.style.transformOrigin='center center';s.style.flexShrink='0';}
window.addEventListener('load',scaleSlide);window.addEventListener('resize',scaleSlide);
</script>
</head>
<body>
<div class="slide-content" style="width:960px;height:540px;background:BG;font-family:'Times New Roman',serif;color:INK;overflow:hidden;">
BODY
BADGE
</div>
</body>
</html>"""

def badge(n):
    return ('<svg style="position:absolute;right:30px;bottom:20px;width:40px;height:32px;z-index:100;" aria-hidden="true">'
            '<rect x="0" y="0" width="40" height="32" rx="6" fill="%s"/>'
            '<text x="20" y="23" font-family="Times New Roman,serif" font-size="15" font-weight="700" fill="#FFFDF6" text-anchor="middle">%d</text></svg>'
            % (CARAM, n))

def slide(body, n=None, cover=False):
    t = TMPL.replace('BODY', body).replace('BADGE', '' if cover else badge(n))
    t = t.replace('BG', BG).replace('INK', INK)
    return t

def write(n, body, cover=False):
    with open(os.path.join(OUT, 'slide-%02d.html' % n), 'w', encoding='utf-8') as f:
        f.write(slide(body, n, cover))

# ---------------------------------------------------------------- helpers ---
def title(text, accent=CARAM, size=30, sub=None):
    s = ('<div style="position:absolute;top:26px;left:60px;right:60px;z-index:5;">'
         '<p style="font-size:%dpx;font-weight:700;color:%s;margin:0;line-height:1.1;">%s</p>'
         '<div style="width:64px;height:4px;background:%s;margin:8px 0 0 0;border-radius:2px;"></div>%s</div>'
         % (size, HEAD, text, accent, ('<p style="font-size:15px;color:%s;margin:6px 0 0 0;">%s</p>' % (SUB, sub) if sub else '')))
    return s

def card(body, accent=CARAM, bg=CARD, pad='14px 16px', border='left'):
    if border == 'left':
        return ('<div style="background:%s;border-radius:10px;padding:%s;border-left:4px solid %s;box-shadow:0 2px 8px rgba(62,40,25,0.10);">%s</div>'
                % (bg, pad, accent, body))
    return ('<div style="background:%s;border-radius:10px;padding:%s;border:2px solid %s;box-shadow:0 2px 8px rgba(62,40,25,0.10);">%s</div>'
            % (bg, pad, accent, body))

def ch(title_, accent=CARAM, color=HEAD):
    return '<p style="font-size:18px;font-weight:700;color:%s;margin:0 0 6px 0;">%s</p>' % (color, title_)

def ul(items, size=15, color=INK, gap='7px', pad='0 0 0 20px'):
    li = ''
    for it in items:
        li += '<li style="margin:0 0 %s 0;">%s</li>' % (gap, it)
    return '<ul style="margin:0;padding:%s;font-size:%dpx;color:%s;line-height:1.45;">%s</ul>' % (pad, size, color, li)

def warnbox(title_, items, size=15):
    lis = ''
    for it in items:
        lis += '<li style="margin:0 0 5px 0;">%s</li>' % it
    return ('<div style="background:%s;border-radius:10px;padding:14px 18px;box-shadow:0 3px 10px rgba(62,40,25,0.22);">'
            '<p style="font-size:18px;font-weight:700;color:%s;margin:0 0 6px 0;">%s</p>'
            '<ul style="margin:0;padding:0 0 0 20px;font-size:%dpx;color:%s;line-height:1.4;">%s</ul></div>'
            % (DARK, AMBER, title_, size, CREAM, lis))

def keybox(title_, body_, accent=CARAM, bg='#FFF3DC'):
    return ('<div style="background:%s;border-radius:10px;padding:10px 16px;border-left:4px solid %s;box-shadow:0 2px 6px rgba(62,40,25,0.08);">'
            '<p style="font-size:14px;margin:0;color:%s;"><b style="color:%s;">%s</b> %s</p></div>'
            % (bg, accent, INK, accent, title_, body_))

def nb(text):
    return keybox('NB: ', text, TERRA, '#FDE9DC')

def grid(cols, gap='14px'):
    return '<div style="display:grid;grid-template-columns:%s;gap:%s;">' % (cols, gap)

def table(headers, rows, width='100%', fs=13.5):
    hd = ''
    for hh in headers:
        hd += '<th style="padding:8px 12px;text-align:left;font-size:%dpx;background:%s;color:%s;">%s</th>' % (fs, DARK2, CREAM, hh)
    trs = ''
    for i, r in enumerate(rows):
        bg = CARD if i % 2 == 0 else CARD2
        tds = ''
        for j, c in enumerate(r):
            bold = 'font-weight:700;' if j == 0 else ''
            tds += '<td style="padding:7px 12px;font-size:%dpx;color:%s;%s">%s</td>' % (fs, INK, bold, c)
        trs += '<tr style="border-bottom:1px solid %s;background:%s;">%s</tr>' % (LINEC, bg, tds)
    return ('<div style="background:%s;border-radius:10px;overflow:hidden;box-shadow:0 2px 8px rgba(62,40,25,0.10);border:1px solid %s;">'
            '<table style="width:%s;border-collapse:collapse;">%s%s</table></div>'
            % (CARD, LINEC, width, '<tr>%s</tr>' % hd, trs))

def flow(boxes, arrows=None):
    """Horizontal flow diagram: boxes joined by arrows."""
    cells = []
    for i, b in enumerate(boxes):
        cells.append('<div style="background:%s;border:2px solid %s;border-radius:8px;padding:8px 6px;text-align:center;font-size:13px;font-weight:700;color:%s;box-shadow:0 2px 6px rgba(62,40,25,0.12);">%s</div>'
                     % (CARD, CARAM, HEAD, b))
        if arrows and i < len(boxes) - 1:
            cells.append('<div style="display:flex;align-items:center;justify-content:center;color:%s;font-size:18px;font-weight:700;">%s</div>' % (TERRA, arrows[i] if i < len(arrows) else '&#8594;'))
    return '<div style="display:grid;grid-template-columns:%s;align-items:stretch;gap:4px;">%s</div>' % (
        ' '.join(['1fr'] * (2 * len(boxes) - 1)), ''.join(cells))

def sp(text):
    return '<span style="color:%s;font-weight:700;">%s</span>' % (TERRA, text)

def B(text):
    return '<b style="color:%s;">%s</b>' % (HEAD, text)

# ================================================================ SLIDE 1 ====
write(1, '''
<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:linear-gradient(135deg,#5C3A24 0%,#8A5A33 100%);"></div>
<div style="position:absolute;top:0;left:0;width:960px;height:540px;">
  <svg width="960" height="540" xmlns="http://www.w3.org/2000/svg">
    <circle cx="820" cy="90" r="210" fill="rgba(217,164,91,0.12)"/>
    <circle cx="120" cy="470" r="170" fill="rgba(168,74,42,0.12)"/>
    <line x1="70" y1="170" x2="170" y2="170" stroke="#D9A45B" stroke-width="5"/>
  </svg>
</div>
<div style="position:absolute;top:118px;left:75px;z-index:5;">
  <p style="font-size:26px;color:rgba(255,240,214,0.85);margin:0;font-weight:400;letter-spacing:2px;">INTERNAL MEDICINE &mdash; NEPHROLOGY</p>
  <p style="font-size:50px;color:#FFE9C2;margin:18px 0 0 0;font-weight:700;line-height:1.12;">Chronic Kidney Disease<br><span style="color:#E8B46A;">&amp; Renal Replacement Therapy</span></p>
  <p style="font-size:21px;color:rgba(255,240,214,0.9);margin:26px 0 0 0;font-weight:400;">CKD &middot; Dialysis (Peritoneal &amp; Hemodialysis) &middot; Kidney Transplantation</p>
  <p style="font-size:15px;color:rgba(255,240,214,0.55);margin:46px 0 0 0;">Principles of Nephrology &mdash; Dr. Hassan Abd-Elhady, Menoufia University</p>
</div>
''', cover=True)

# ================================================================ SLIDE 2 ====
write(2, '''
<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:%s;"></div>
<div style="position:absolute;top:26px;left:60px;right:60px;z-index:5;">
  <p style="font-size:32px;font-weight:700;color:%s;margin:0;">Table of Contents</p>
  <div style="width:64px;height:4px;background:%s;margin:8px 0 22px 0;border-radius:2px;"></div>
</div>
<div style="position:absolute;top:92px;left:60px;right:60px;z-index:5;">
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px 26px;">
    <div style="display:flex;align-items:center;gap:14px;background:%s;border-radius:8px;padding:11px 14px;border-left:4px solid %s;box-shadow:0 2px 6px rgba(62,40,25,0.08);">
      <span style="font-size:19px;font-weight:700;color:%s;min-width:30px;">01</span>
      <span style="font-size:17px;color:%s;">Chronic Kidney Disease &mdash; Definitions &amp; Markers</span>
    </div>
    <div style="display:flex;align-items:center;gap:14px;background:%s;border-radius:8px;padding:11px 14px;border-left:4px solid %s;box-shadow:0 2px 6px rgba(62,40,25,0.08);">
      <span style="font-size:19px;font-weight:700;color:%s;min-width:30px;">02</span>
      <span style="font-size:17px;color:%s;">CKD &mdash; Grades, Causes &amp; Clinical Features</span>
    </div>
    <div style="display:flex;align-items:center;gap:14px;background:%s;border-radius:8px;padding:11px 14px;border-left:4px solid %s;box-shadow:0 2px 6px rgba(62,40,25,0.08);">
      <span style="font-size:19px;font-weight:700;color:%s;min-width:30px;">03</span>
      <span style="font-size:17px;color:%s;">CKD &mdash; Bone Disease, Investigations</span>
    </div>
    <div style="display:flex;align-items:center;gap:14px;background:%s;border-radius:8px;padding:11px 14px;border-left:4px solid %s;box-shadow:0 2px 6px rgba(62,40,25,0.08);">
      <span style="font-size:19px;font-weight:700;color:%s;min-width:30px;">04</span>
      <span style="font-size:17px;color:%s;">CKD &mdash; Treatment (Conservative)</span>
    </div>
    <div style="display:flex;align-items:center;gap:14px;background:%s;border-radius:8px;padding:11px 14px;border-left:4px solid %s;box-shadow:0 2px 6px rgba(62,40,25,0.08);">
      <span style="font-size:19px;font-weight:700;color:%s;min-width:30px;">05</span>
      <span style="font-size:17px;color:%s;">RRT &mdash; Dialysis &amp; Peritoneal Dialysis</span>
    </div>
    <div style="display:flex;align-items:center;gap:14px;background:%s;border-radius:8px;padding:11px 14px;border-left:4px solid %s;box-shadow:0 2px 6px rgba(62,40,25,0.08);">
      <span style="font-size:19px;font-weight:700;color:%s;min-width:30px;">06</span>
      <span style="font-size:17px;color:%s;">RRT &mdash; Hemodialysis &amp; Kidney Transplantation</span>
    </div>
  </div>
</div>
''' % (BG, HEAD, CARAM, CARD, CARAM, CARAM, INK, CARD, TERRA, TERRA, INK,
       CARD, OLIVE, OLIVE, INK, CARD, AMBER, AMBER, INK, CARD, CARAM, CARAM, INK,
       CARD, CARAM, CARAM, INK))

# ================================================================ SLIDE 3 ====
write(3, '''
<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:linear-gradient(135deg,#5C3A24 0%%,#7A4A2B 100%%);"></div>
<div style="position:absolute;top:0;right:0;width:380px;height:540px;background:%s;opacity:0.16;"></div>
<div style="position:absolute;top:0;left:0;width:10px;height:540px;background:%s;"></div>
<div style="position:absolute;top:130px;left:80px;z-index:5;">
  <p style="font-size:92px;font-weight:700;color:%s;margin:0;line-height:1;">01</p>
  <div style="width:80px;height:4px;background:%s;margin:14px 0 16px 0;"></div>
  <p style="font-size:40px;font-weight:700;color:#FFF3DC;margin:0;">Chronic Kidney Disease</p>
  <p style="font-size:19px;color:#E8B46A;margin:10px 0 0 0;">Definitions &middot; Markers &middot; Grades &middot; Causes &middot; Clinical Picture &middot; Investigations &middot; Treatment</p>
</div>
''' % (AMBER, AMBER, AMBER, AMBER))

# ================================================================ SLIDE 4 ====
write(4, '''
%s
<div style="position:absolute;top:96px;left:60px;right:60px;z-index:5;display:grid;grid-template-columns:1fr;gap:14px;">
  %s
  %s
  %s
</div>
''' % (title('Definitions'),
card(B('CKD ') + 'is defined as ' + sp('abnormalities of kidney structure or function, present for &gt; 3 months') + ' with implications for health, and is classified based on ' + sp('cause, GFR category and albuminuria category') + '.', CARAM),
card(B('Chronic Renal Failure (CRF): ') + 'GFR is ' + sp('&lt; 60 ml/min/1.73 m&#178; for &#8805; 3 months') + ' (Grade 3 CKD).', TERRA),
card(B('End Stage Renal Disease (ESRD): ') + 'a ' + sp('permanent and irreversible renal impairment') + ' which ' + sp('necessitates renal replacement therapy') + ' = Grade 5 CKD.', OLIVE)))

# ================================================================ SLIDE 5 ====
write(5, '''
%s
<div style="position:absolute;top:96px;left:60px;right:60px;z-index:5;display:grid;grid-template-columns:1fr 1fr;gap:16px;">
  %s
  %s
</div>
''' % (title('Markers of Kidney Damage'),
card(ch('Functional Markers', TERRA) +
     ul([B('Albuminuria:') + ' albumin excretion rate (AER) &#8805; 30 mg/24 h, or albumin/creatinine ratio (ACR) &#8805; 30 mg/g.',
         B('Urine sediment abnormalities.'),
         B('Electrolytes and other abnormalities') + ' due to tubular disorders.'])),
card(ch('Structural Markers', OLIVE) +
     ul([B('Structural abnormalities detected by histology.'),
         B('Structural abnormalities detected by imaging.'),
         B('History of kidney transplantation.')]))))

# ================================================================ SLIDE 6 ====
write(6, '''
%s
<div style="position:absolute;top:92px;left:60px;right:60px;z-index:5;">
  <p style="font-size:15px;color:%s;margin:0 0 10px 0;">Classified according to GFR category (five grades) and albuminuria category (3 grades).</p>
  %s
  <div style="margin-top:10px;">%s</div>
</div>
''' % (title('Grades (Stages) of CKD'),
       SUB,
       table(['Grade', 'GFR (ml/min/1.73 m&#178;)', 'Terms'],
             [['G1', '&#8805; 90', 'Normal or high'],
              ['G2', '60 &ndash; 89', 'Mildly decreased*'],
              ['G3a', '45 &ndash; 89', 'Mildly to moderately decreased'],
              ['G3b', '30 &ndash; 44', 'Moderately to severely decreased'],
              ['G4', '15 &ndash; 29', 'Severely decreased'],
              ['G5', '&lt; 15', 'ESRD']]),
       nb('In the absence of evidence of kidney damage, neither GFR category G1 nor G2 fulfill the criteria for CKD. *Relative to young adult level.')))

# ================================================================ SLIDE 7 ====
write(7, '''
%s
<div style="position:absolute;top:92px;left:60px;right:60px;z-index:5;">
  %s
  <div style="margin-top:12px;">%s</div>
</div>
''' % (title('Albuminuria Categories in CKD'),
       table(['Category', 'AER (mg/24 h)', 'ACR (mg/g)', 'Terms'],
             [['A1', '&lt; 30', '&lt; 30', 'Normal to mildly increased'],
              ['A2', '30 &ndash; 300', '30 &ndash; 300', 'Moderately increased*'],
              ['A3', '&gt; 300', '&gt; 300', 'Severely increased**']]),
       nb('**Including nephrotic syndrome (albumin excretion usually &gt; 2200 mg/24 h &amp; ACR &gt; 2200 mg/g). *Relative to young adult level.')))

# ================================================================ SLIDE 8 ====
write(8, '''
%s
<div style="position:absolute;top:96px;left:60px;right:60px;z-index:5;">
  %s
</div>
''' % (title('Causes of CKD'),
card(ul(['<b>%s</b> Diabetes mellitus.' % '1.',
         '<b>%s</b> Hypertension.' % '2.',
         '<b>%s</b> Glomerulopathies, either primary or secondary.' % '3.',
         '<b>%s</b> Tubulo-interstitial diseases.' % '4.',
         '<b>%s</b> Renal vascular diseases (renal artery stenosis).' % '5.',
         '<b>%s</b> Hereditary renal diseases e.g. PCKD, Alport&rsquo;s syndrome, oxalosis.' % '6.',
         '<b>%s</b> Obstructive uropathy e.g. urolithiasis, prostatic enlargement, tumors, retroperitoneal fibrosis.' % '7.',
         '<b>%s</b> Recurrent UTI (pyelonephritis, vesicoureteral reflux).' % '8.',
         '<b>%s</b> Drugs and toxins; NSAID, chronic lead poisoning.' % '9.',
         '<b>%s</b> Uncertain (in up to 15%% of cases).' % '10.']),
     CARAM)))

# ================================================================ SLIDE 9 ====
write(9, '''
%s
<div style="position:absolute;top:96px;left:60px;right:60px;z-index:5;">
  %s
  <div style="margin-top:12px;">%s</div>
</div>
''' % (title('Diagnosis &mdash; Clinical Features (GIT)'),
       keybox('Overview: ', 'CKD leads to disturbances in the function of every system in the body. The presentation and severity vary greatly from patient to patient depending on the grade/severity of disease. ' + sp('Grades 1&ndash;3 are usually asymptomatic; Grades 4 &amp; 5 are symptomatic.')),
       card(ch('Gastrointestinal', TERRA) +
            ul(['<b>%s</b> Anorexia, nausea, vomiting &amp; hiccough (early &amp; controlled by protein restriction).' % '1.',
                '<b>%s</b> Uremic fetor; uriniferous odor of breath (breakdown of urea to ammonia).' % '2.',
                '<b>%s</b> Mucosal ulcerations (in late stages) &#8594; GIT bleeding.' % '3.',
                '<b>%s</b> Peptic ulcer; increased gastric acidity, gastrin secretion, secondary hyperparathyroidism.' % '4.',
                '<b>%s</b> Increased incidence of diverticulosis (in patients with PCKD).' % '5.'],
               size=14.5) +
            nb('GIT symptoms are improved by dialysis, except peptic ulcers and diverticulosis.'), TERRA)))

# =============================================================== SLIDE 10 ====
write(10, '''
%s
<div style="position:absolute;top:96px;left:60px;right:60px;z-index:5;">
  %s
</div>
''' % (title('Clinical Features &mdash; Cardiovascular'),
       card(ch('Cardiovascular', TERRA) +
            ul(['<b>%s</b> CHF and pulmonary edema; dyspnea, orthopnea, increased jugular venous pressure, lower limb edema due to volume overload.' % '1.',
                '<b>%s</b> Arrhythmias; due to electrolyte abnormalities.' % '2.',
                '<b>%s</b> Hypertension.' % '3.',
                '<b>%s</b> Pericarditis and pericardial effusion.' % '4.',
                '<b>%s</b> Accelerated atherosclerosis.' % '5.'],
               size=14.5) +
            nb('Absence of hypertension in a CKD patient may be due to: salt wasting nephropathy e.g. PCKD &middot; use of anti-hypertensive drugs &middot; volume depletion e.g. GIT loss or diuretic overdose.'), TERRA)))

# =============================================================== SLIDE 11 ====
write(11, '''
%s
<div style="position:absolute;top:96px;left:60px;right:60px;z-index:5;display:grid;grid-template-columns:1fr 1fr;gap:16px;">
  %s
  %s
</div>
''' % (title('Clinical Features &mdash; Respiratory &amp; Hematological'),
       card(ch('Respiratory', OLIVE) +
            ul(['Acidotic breathing.',
                'Pleurisy.',
                'Chest infection.'])),
       card(ch('Hematological &mdash; Anemia', TERRA) +
            ul([B('Anemia') + ' &#8594; easy fatigability, palpitation &amp; tachycardia, due to:',
                'Erythropoietin deficiency.',
                'Decreased life span of RBCs and toxic bone marrow suppression.',
                'Decreased nutrient intake and absorption; iron, vitamin B12, folate.',
                'Bleeding tendency.',
                'Secondary hyperparathyroidism.',
                'Chronic inflammation.',
                'Blood loss during dialysis and from GIT.'], size=13.5, gap='4px'))))

# =============================================================== SLIDE 12 ====
write(12, '''
%s
<div style="position:absolute;top:96px;left:60px;right:60px;z-index:5;display:grid;grid-template-columns:1fr;gap:14px;">
  %s
  %s
</div>
''' % (title('Clinical Features &mdash; Hematological (cont.)'),
       card(ch('Bleeding Diathesis', TERRA) +
            ul(['Due to: prolongation of bleeding time, decreased factor III activity, abnormal platelet aggregation and adhesion, and impaired prothrombin consumption.'], size=14.5)),
       card(ch('Enhanced Susceptibility to Infection', TERRA) +
            ul([B('Impaired leukocyte formation and function') + ' due to: acidosis, hyperglycemia, hyperosmolarity of serum and tissues by azotemia, and malnutrition.',
                B('Defective mucosal barriers.'),
                B('Use of steroids and immunosuppressive drugs.')], size=14.5))))

# =============================================================== SLIDE 13 ====
write(13, '''
%s
<div style="position:absolute;top:96px;left:60px;right:60px;z-index:5;">
  %s
</div>
''' % (title('Clinical Features &mdash; Endocrine &amp; Metabolism'),
       card(ul(['<b>%s</b> Insulin resistance and impaired glucose tolerance.' % '1.',
                '<b>%s</b> Decreased insulin metabolism and degradation by the diseased kidney &#8594; decreased insulin requirement for diabetic patients.' % '2.',
                '<b>%s</b> Thyroid dysfunction; increased TRH &#8594; release of prolactin with impaired prolactin clearance &#8594; galactorrhea, amenorrhea, and impotence.' % '3.',
                '<b>%s</b> Hypocalcemia &#8594; secondary hyperparathyroidism.' % '4.',
                '<b>%s</b> Decreased serum testosterone level &#8594; impotence, decreased spermatogenesis and infertility.' % '5.',
                '<b>%s</b> Menstrual abnormalities (oligomenorrhea, amenorrhea) and infertility.' % '6.'],
               size=14.5), CARAM)))

# =============================================================== SLIDE 14 ====
write(14, '''
%s
<div style="position:absolute;top:96px;left:60px;right:60px;z-index:5;display:grid;grid-template-columns:1fr 1fr;gap:16px;">
  %s
  %s
</div>
''' % (title('Bone &mdash; CKD-MBD: Definition &amp; Pathophysiology'),
       card(ch('Definition of CKD-MBD', TERRA) +
            ul(['A systemic disorder of mineral and bone metabolism due to CKD, manifested by one or a combination of:',
                '<b>%s</b> Abnormalities of calcium, phosphorus, PTH, or vitamin D metabolism.' % '1.',
                '<b>%s</b> Abnormalities in bone turnover, mineralization, volume, linear growth or strength (renal osteodystrophy).' % '2.',
                '<b>%s</b> Vascular or other soft tissue calcification e.g. cardiac valve, arterial calcification and calciphylaxis.' % '3.'],
               size=13.5, gap='5px')),
       card(ch('Pathophysiology (Figure 10, Martin et al., 2007)', OLIVE) +
            ul(['<b>%s</b> Reduction of GFR &lt; 60 ml/min &#8594; decreased phosphorus filtration &#8594; hyperphosphatemia &#8594; PTH secretion stimulation.' % '1.',
                '<b>%s</b> Decreased renal production of 1&#945;-hydroxylase &#8594; decreased active vitamin D3 &ldquo;1,25(OH)&#8322; vit. D&rdquo; &#8594; hypocalcemia &#8594; in addition to hyperphosphatemia &#8594; secondary hyperparathyroidism (SHPT).' % '2.'],
               size=13.5, gap='8px'))))

# =============================================================== SLIDE 15 ====
write(15, '''
%s
<div style="position:absolute;top:92px;left:60px;right:60px;z-index:5;">
  <p style="font-size:15px;color:%s;margin:0 0 8px 0;">Figure 10 &mdash; Pathophysiology of CKD-MBD (flow diagram):</p>
  <div style="background:%s;border-radius:10px;padding:14px 16px;box-shadow:0 2px 8px rgba(62,40,25,0.10);">
    %s
  </div>
  <div style="margin-top:12px;display:grid;grid-template-columns:1fr 1fr;gap:12px;">
    %s
    %s
    %s
    %s
  </div>
</div>
''' % (title('Figure 10 &mdash; CKD-MBD Pathophysiology Diagram'),
       SUB, CARD,
       flow(['&#8595; Renal Mass', 'Pi Retention', 'Abn PT Growth &amp; Function', '&#8595; Calcitriol', 'Skeletal Resistance', 'Hypocalcemia', 'Hyperpara-thyroidism']),
       card(ch('Above &ldquo;Abn PT Growth &amp; Function&rdquo;', TERRA) + ul(['Hypocalcemia, &#8595; Calcitriol, Calcitriol resistance, &#8593; Set-point, &#8595; VDR, PTG Hyperplasia, &#8593; TGF-&#945; &#8593; EGF-R, &#8593; PTG Mass, &#8595; Ca Receptor, &#8593; Phosphorus, ? PTH mRNA stability'], size=12, gap='0px')),
       card(ch('Above &ldquo;Hypocalcemia&rdquo;', OLIVE) + ul(['&#8593; Phosphorus, &#8595; Calcitriol, Calcitriol Resistance, Skeletal Resistance'], size=12, gap='0px')),
       card(ch('Below &ldquo;&#8595; Calcitriol&rdquo;', CARAM) + ul(['&#8593; Phosphorus, &#8595; Renal Mass, ? &#8595; 25(OH)D, ? &#8595; 1-25, ? acidosis, ? other'], size=12, gap='0px')),
       card(ch('Below &ldquo;Skeletal Resistance&rdquo;', AMBER) + ul(['&#8593; Phosphorus, Desens. to PTH, ? &#8595; PTH-R, &#8595; calcitriol, ? Uremic toxins, ? PTH inhibitors'], size=12, gap='0px'))))

# =============================================================== SLIDE 16 ====
write(16, '''
%s
<div style="position:absolute;top:96px;left:60px;right:60px;z-index:5;display:grid;grid-template-columns:1fr;gap:14px;">
  %s
  %s
</div>
''' % (title('Renal Osteodystrophy &mdash; Definition &amp; Types'),
       card(B('Definition: ') + 'the skeletal component of the systemic disorder of MBD that occurs in patients with CKD. Patients may suffer from; bone pain, pathological (spontaneous) fractures, and bone changes in bone imaging and bone biopsy.', CARAM),
       card(ch('It includes (Figure 11):', TERRA) +
            ul(['<b>%s</b> <b>Osteitis fibrosa (high turnover bone disease):</b> a manifestation of hyperparathyroidism characterized by increased osteoclast and osteoblast activity (turnover) and peritrabecular fibrosis.' % '1.',
                '<b>%s</b> <b>Osteomalacia:</b> a condition characterized by abnormally low bone turnover.' % '2.',
                '<b>%s</b> <b>Adynamic bone disease:</b> decreased rates of bone formation with normal bone mineralization; due to aggressive suppression of PTH leading to hypoparathyroidism.' % '3.',
                '<b>%s</b> <b>Osteopenia or osteoporosis:</b> increased skeletal fragility as a result of reduced bone quantity and quality.' % '4.',
                '<b>%s</b> <b>Mixed lesions:</b> combination of these abnormalities; high PTH levels + impaired bone formation and mineralization. Usually seen in patients with previously established hyperparathyroid bone disease who develop aluminum-related bone disease.' % '5.'],
               size=13.5, gap='6px'))))

# =============================================================== SLIDE 17 ====
write(17, '''
%s
<div style="position:absolute;top:92px;left:60px;right:60px;z-index:5;">
  <p style="font-size:15px;color:%s;margin:0 0 10px 0;">Figure 11 &mdash; Skeletal abnormalities in renal bone disease (spectrum of renal osteodystrophy; Martin et al., 2015):</p>
  <div style="background:%s;border-radius:10px;padding:18px 20px;box-shadow:0 2px 8px rgba(62,40,25,0.10);">
    <div style="display:flex;align-items:center;gap:6px;">
      <div style="flex:1;background:#FFF3DC;border:2px solid %s;border-radius:8px;padding:12px 8px;text-align:center;">
        <p style="font-size:13px;font-weight:700;color:%s;margin:0;">Adynamic bone / Osteomalacia</p>
        <p style="font-size:12px;color:%s;margin:4px 0 0 0;"><b>Low turnover</b></p>
      </div>
      <div style="font-size:16px;color:%s;font-weight:700;">&#8594;</div>
      <div style="flex:1;background:%s;border:2px dashed %s;border-radius:8px;padding:12px 8px;text-align:center;">
        <p style="font-size:13px;font-weight:700;color:%s;margin:0;">Normal</p>
      </div>
      <div style="font-size:16px;color:%s;font-weight:700;">&#8594;</div>
      <div style="flex:1;background:%s;border:2px dashed %s;border-radius:8px;padding:12px 8px;text-align:center;">
        <p style="font-size:13px;font-weight:700;color:%s;margin:0;">Mild</p>
      </div>
      <div style="font-size:16px;color:%s;font-weight:700;">&#8594;</div>
      <div style="flex:1;background:#FDE9DC;border:2px solid %s;border-radius:8px;padding:12px 8px;text-align:center;">
        <p style="font-size:13px;font-weight:700;color:%s;margin:0;">Osteitis fibrosa</p>
        <p style="font-size:12px;color:%s;margin:4px 0 0 0;"><b>High turnover &mdash; Hyperparathyroidism</b></p>
      </div>
    </div>
    <div style="display:flex;justify-content:center;margin-top:12px;">
      <div style="background:%s;border:2px solid %s;border-radius:8px;padding:8px 22px;text-align:center;">
        <p style="font-size:13px;font-weight:700;color:%s;margin:0;">Mixed</p>
        <p style="font-size:11px;color:%s;margin:2px 0 0 0;">(between Adynamic/Osteomalacia and Osteitis fibrosa)</p>
      </div>
    </div>
    <div style="margin-top:12px;text-align:center;font-size:13px;color:%s;">
      <b>Below the spectrum:</b> Calcium, calcitriol and Aluminum
    </div>
  </div>
</div>
''' % (title('Figure 11 &mdash; Spectrum of Renal Osteodystrophy'),
       SUB, CARD, OLIVE, OLIVE, SUB, TERRA, CARD2, SUB, SUB, TERRA, CARD2, SUB, SUB, TERRA,
       TERRA, TERRA, SUB, DARK2, CARAM, CREAM, SUB, SUB))

# =============================================================== SLIDE 18 ====
write(18, '''
%s
<div style="position:absolute;top:96px;left:60px;right:60px;z-index:5;display:grid;grid-template-columns:1fr;gap:13px;">
  %s
  %s
  %s
</div>
''' % (title('Clinical Features &mdash; Neurological'),
       card(ch('CNS', TERRA) +
            ul([B('Early: ') + 'inability to concentrate, loss of memory, drowsiness, insomnia, hiccups, cramps and muscle twitching.',
                B('Late: ') + 'asterixis, myoclonus, chorea, stupor, seizures and coma.'], size=14, gap='5px')),
       card(ch('Peripheral Nerves', OLIVE) +
            ul(['Sensory (early) and motor neuropathy.',
                B('Restless legs syndrome: ') + 'discomfort in the feet and legs with frequent leg movement. ' + B('Treatment: ') + 'early dialysis or transplantation.'], size=14, gap='5px')),
       card(ch('In Dialysis Patients', CARAM) +
            ul([B('Dialysis dementia (encephalopathy).'),
                B('Dialysis disequilibrium syndrome: ') + '(nausea, vomiting, drowsiness, headache, seizures). Occurs in the first few sessions of dialysis; due to rapid removal of urea with rapid reduction of osmolality of the extracellular compartment within the cranium &#8594; cerebral edema and increased intracranial pressure.'], size=14, gap='5px'))))

# =============================================================== SLIDE 19 ====
write(19, '''
%s
<div style="position:absolute;top:96px;left:60px;right:60px;z-index:5;">
  %s
</div>
''' % (title('Clinical Features &mdash; Dermatological'),
       card(ul(['<b>%s</b> Earthy (muddy) face due to combination of anemia and retention of urochrome pigment.' % '1.',
                '<b>%s</b> Pallor due to anemia.' % '2.',
                '<b>%s</b> Ecchymosis and hematomas due to defective hemostasis.' % '3.',
                '<b>%s</b> Pruritus due to calcium deposition and secondary hyperparathyroidism.' % '4.',
                '<b>%s</b> Poor skin turgor and dry mucous membranes due to dehydration.' % '5.',
                '<b>%s</b> Evidence of malnutrition.' % '6.',
                '<b>%s</b> Uremic frost (in advanced cases); a fine white powder due to high urea concentration in sweat which precipitates on skin after evaporation.' % '7.',
                '<b>%s</b> Slate-gray-bronze discoloration of skin (hemochromatosis) due to multiple blood transfusions in dialysis patients.' % '8.',
                '<b>%s</b> Half and half nails.' % '9.',
                '<b>%s</b> Calciphylaxis (calcific uremic arteriolopathy): vascular calcification of skin, muscles and subcutaneous tissues. The skin shows violaceous rashes, nonhealing ulcers, and gangrene &#8594; high mortality.' % '10.'],
               size=13.5, gap='4px'), CARAM) +
            nb('Most skin abnormalities improve with dialysis, except pruritus which persists.')))

# =============================================================== SLIDE 20 ====
write(20, '''
%s
<div style="position:absolute;top:96px;left:60px;right:60px;z-index:5;display:grid;grid-template-columns:1fr 1fr;gap:16px;">
  %s
  %s
</div>
''' % (title('Clinical Features &mdash; Urinary &amp; Electrolytes'),
       card(ch('Urinary System', OLIVE) +
            ul([B('UTI.'),
                B('Urine volume:'),
                'Early; polyuria and nocturia.',
                'Late; oliguria and anuria.'], size=14)),
       card(ch('Electrolytes &amp; Acid-Base Disturbances', TERRA) +
            ul(['<b>%s</b> Hyperkalemia &#8594; muscle weakness, arrhythmias, cardiac arrest.' % '1.',
                '<b>%s</b> Hypocalcemia &#8594; tetany is rare as acidosis increases ionized calcium.' % '2.',
                '<b>%s</b> Hyperphosphatemia &#8594; itching, metastatic calcification.' % '3.',
                '<b>%s</b> Metabolic acidosis &#8594; rapid deep breathing, convulsions.' % '4.'],
               size=14, gap='5px'))))

# =============================================================== SLIDE 21 ====
write(21, '''
%s
<div style="position:absolute;top:92px;left:60px;right:60px;z-index:5;">
  <p style="font-size:16px;font-weight:700;color:%s;margin:0 0 8px 0;">2. Investigations</p>
  %s
</div>
''' % (title('Investigations &mdash; Part A', sub='A. To establish the degree of renal impairment and complications'),
       HEAD,
       card(ul(['<b>%s</b> Urine analysis with evaluation of albuminuria, broad casts, and low fixed specific gravity.' % '1.',
                '<b>%s</b> Kidney function tests; urea, creatinine and eGFR.' % '2.',
                '<b>%s</b> Serum electrolytes: Sodium, Potassium, Calcium and Phosphorus.' % '3.',
                '<b>%s</b> Arterial blood gases.' % '4.',
                '<b>%s</b> Serum uric acid.' % '5.',
                '<b>%s</b> Complete blood count.' % '6.',
                '<b>%s</b> Iron profile.' % '7.',
                '<b>%s</b> iPTH level.' % '8.',
                '<b>%s</b> Skeletal survey.' % '9.'],
               size=14.5, gap='4px'), CARAM)))

# =============================================================== SLIDE 22 ====
write(22, '''
%s
<div style="position:absolute;top:92px;left:60px;right:60px;z-index:5;">
  <p style="font-size:16px;font-weight:700;color:%s;margin:0 0 8px 0;">2. Investigations</p>
  %s
</div>
''' % (title('Investigations &mdash; Part B', sub='B. To determine the underlying disease (if the cause is not clear)'),
       HEAD,
       card(ul(['<b>%s</b> Serum and urine protein electrophoresis.' % '1.',
                '<b>%s</b> ANA, anti-ds DNA ab, C3 &amp; C4, ANCA, AGBM ab.' % '2.',
                '<b>%s</b> Hepatitis C and B and HIV serology.' % '3.',
                '<b>%s</b> Renal imaging: kidney ureter bladder X-ray (KUB), ultrasound, CT, MRI, radionuclide scan (renogram).' % '4.',
                '<b>%s</b> Renal biopsy: ' % '5.'] +
               [sp('not indicated') + ' if there is a small atrophic kidney.'], size=14.5, gap='6px'), CARAM)))

# =============================================================== SLIDE 23 ====
write(23, '''
%s
<div style="position:absolute;top:92px;left:60px;right:60px;z-index:5;">
  <p style="font-size:16px;font-weight:700;color:%s;margin:0 0 8px 0;">2. Investigations</p>
  %s
  <div style="margin-top:10px;">%s</div>
</div>
''' % (title('Investigations &mdash; Part C', sub='C. To diagnose a patient with acute RF on top of CKD'),
       HEAD,
       card(ul(['<b>%s</b> Bone disease.' % '1.',
                '<b>%s</b> Uremic neuropathy.' % '2.',
                '<b>%s</b> Profound anemia, hyperphosphatemia, and high serum creatinine with mild symptoms.' % '3.',
                '<b>%s</b> Small sized kidney ' % '4.'] +
               [B('except in;') + ' DM, amyloidosis, multiple myeloma and PCKD.'], size=14.5, gap='6px'), CARAM),
       keybox('NB: ', 'Part C &mdash; the listed features suggest chronicity (CKD) rather than acute kidney injury.', TERRA, '#FDE9DC')))

# =============================================================== SLIDE 24 ====
write(24, '''
%s
<div style="position:absolute;top:96px;left:60px;right:60px;z-index:5;">
  %s
  <div style="margin-top:12px;">%s</div>
</div>
''' % (title('Treatment &mdash; Conservative (Overview)'),
       keybox('I) Conservative treatment includes: ', '1. Correction of any reversible cause and underlying disease &middot; 2. Control of symptoms &middot; 3. Educational programs to the patients and their relatives', CARAM),
       card(ch('Correction of Any Reversible Cause (to delay CKD progression)', TERRA) +
            ul(['<b>%s</b> Good blood glucose control.' % '1.',
                '<b>%s</b> Good blood pressure control.' % '2.',
                '<b>%s</b> Good hydration.' % '3.',
                '<b>%s</b> Correction of renal obstruction and UTI.' % '4.',
                '<b>%s</b> Treatment of active primary renal disease.' % '5.',
                '<b>%s</b> Treatment of sepsis.' % '6.',
                '<b>%s</b> Reduction of proteinuria (ACEI/ARBs, avoid combination).' % '7.',
                '<b>%s</b> Control of dyslipidemia.' % '8.',
                '<b>%s</b> Lifestyle modification (diet, weight reduction, smoking &amp; alcohol cessation, exercise).' % '9.',
                '<b>%s</b> Avoid nephrotoxins and large doses of contrast agents.' % '10.'],
               size=13.5, gap='4px'))))

# =============================================================== SLIDE 25 ====
write(25, '''
%s
<div style="position:absolute;top:96px;left:60px;right:60px;z-index:5;display:grid;grid-template-columns:1fr 1fr;gap:16px;">
  %s
  %s
</div>
''' % (title('Control of Symptoms &mdash; Diet &amp; GIT'),
       card(ch('Diet (low protein, potassium, phosphate, and salts) + fluid balance', CARAM) +
            ul(['<b>%s</b> Low protein diet (0.6&ndash;0.8 gm/kg/day). Protein diet should be increased when the patient starts dialysis.' % '1.',
                '<b>%s</b> Low potassium diet (if the patient is hypokalemic, increase potassium diet).' % '2.',
                '<b>%s</b> Low phosphate diet.' % '3.',
                '<b>%s</b> Salt restriction (free salt intake in salt-losing nephropathy).' % '4.',
                '<b>%s</b> Fluid balance; depends on urine output.' % '5.'],
               size=13.5, gap='5px')),
       card(ch('GIT', TERRA) +
            ul(['<b>%s</b> Hiccough and vomiting &#8594; prokinetics. If persist &#8594; dialysis.' % '1.',
                '<b>%s</b> Gastritis; proton pump inhibitors (avoid long term use as may cause interstitial nephropathy).' % '2.'],
               size=14, gap='8px'))))

# =============================================================== SLIDE 26 ====
write(26, '''
%s
<div style="position:absolute;top:96px;left:60px;right:60px;z-index:5;">
  %s
</div>
''' % (title('Control of Symptoms &mdash; Cardiovascular'),
       card(ul(['<b>%s</b> Control of hypertension; ACEI/ARBs, CCB, BB.' % '1.',
                '<b>%s</b> ACEI or ARBs are preferred if there is proteinuria, but with careful monitoring of serum creatinine and potassium levels.' % '2.',
                '<b>%s</b> Volume overload &#8594; loop diuretics.' % '3.',
                '<b>%s</b> Pericarditis &#8594; dialysis.' % '4.'],
               size=15, gap='8px'), TERRA)))

# =============================================================== SLIDE 27 ====
write(27, '''
%s
<div style="position:absolute;top:92px;left:60px;right:60px;z-index:5;display:grid;grid-template-columns:1fr;gap:12px;">
  <p style="font-size:16px;font-weight:700;color:%s;margin:0;">Mineral Bone Disease (MBD) &mdash; Control of hypocalcemia, hyperphosphatemia, vitamin D deficiency and secondary hyperparathyroidism</p>
  %s
  %s
</div>
''' % (title('Treatment &mdash; Mineral Bone Disease (1)'),
       HEAD,
       card(ch('Diet Control', CARAM) +
            ul(['<b>%s</b> Increased elementary dietary calcium to 1500&ndash;2000 mg/day (hold if there is hypercalcemia).' % '1.',
                '<b>%s</b> Low phosphate diet (800&ndash;1000 mg/day) adjusted by requirement of protein in grades 3&ndash;5 CKD patients.' % '2.'],
               size=14, gap='6px')),
       card(ch('Phosphate Binders &mdash; indicated when dietary phosphate restriction is insufficient to control phosphate and PTH levels', TERRA) +
            ul([B('Calcium-based phosphate binders; ') + 'e.g. Ca carbonate, given orally during meals.',
                'A. Decreases serum phosphate level effectively and can be used for initial phosphate binding treatment.',
                'B. Long-term administration can result in hypercalcemia.',
                'C. Should not be used in dialysis patients with hypercalcemia and in patients with plasma PTH level &lt; 130 pg/dL. In these conditions use calcium-free phosphate binders.',
                B('Non-calcium-based phosphate binders; ') + 'Sevelamer (Renagel) hydrochloride or bicarbonate &mdash; safe and effective but expensive.',
                B('Lanthanum carbonate.')], size=13.5, gap='4px'))))

# =============================================================== SLIDE 28 ====
write(28, '''
%s
<div style="position:absolute;top:96px;left:60px;right:60px;z-index:5;display:grid;grid-template-columns:1fr;gap:13px;">
  %s
  %s
  %s
</div>
''' % (title('Treatment &mdash; Mineral Bone Disease (2)'),
       card(B('Calcimimetic agents (cinacalcet)') + ' &mdash; inhibits iPTH secretion.', OLIVE),
       card(B('Vitamin D analogs (alfacalcidol/calcitriol; 0.25&ndash;2 &#181;g daily)') + ' according to serum Ca, PO&#8324; and iPTH levels. ' + sp('Hold if there is hypercalcemia and/or hyperphosphatemia.') + ' Treatment with vitamin D is recommended for renal patients with:' +
            ul(['<b>%s</b> Total serum calcium level &lt; 9.5 mg/dl.' % '1.',
                '<b>%s</b> Serum phosphate level &lt; 4.6 mg/dl.' % '2.',
                '<b>%s</b> Elevated serum PTH level.' % '3.'], size=14, gap='4px'), TERRA),
       card(B('Parathyroidectomy') + ' in severe hyperparathyroidism (PTH &gt; 800 pg/dL) not responding to medications.', TERRA)))

# =============================================================== SLIDE 29 ====
write(29, '''
%s
<div style="position:absolute;top:96px;left:60px;right:60px;z-index:5;display:grid;grid-template-columns:1fr 1fr;gap:16px;">
  %s
  %s
</div>
''' % (title('Treatment &mdash; Anemia &amp; Pruritus'),
       card(ch('Management of Anemia', TERRA) +
            ul(['<b>%s</b> Iron therapy: oral in pre-dialysis patients and better I.V. for HD patients.' % '1.',
                '<b>%s</b> Erythropoietin; subcutaneous or intravenous:' % '2.',
                '&bull; Erythropoietin alpha or beta.',
                '&bull; Long acting darbepoetin alfa.',
                '&bull; Continuous erythropoiesis receptor activator (CERA).'],
               size=13.5, gap='4px')),
       card(ch('Pruritus', OLIVE) +
            ul(['<b>%s</b> Moistening ointment.' % '1.',
                '<b>%s</b> Gabapentin, Naltrexone.' % '2.',
                '<b>%s</b> Short wave ultraviolet.' % '3.',
                '<b>%s</b> Increase dose of dialysis.' % '4.'],
               size=14, gap='6px'))))

# =============================================================== SLIDE 30 ====
write(30, '''
%s
<div style="position:absolute;top:92px;left:60px;right:60px;z-index:5;display:grid;grid-template-columns:1fr;gap:12px;">
  <p style="font-size:15px;color:%s;margin:0 0 2px 0;">Correction of electrolyte and acid-base disorders &mdash; see Chapter V (Electrolytes &amp; Acid-Base).</p>
  %s
  %s
</div>
''' % (title('Treatment &mdash; Educational Program &amp; RRT'),
       SUB,
       card(ch('Educational Program', CARAM) +
            ul(['Explain the possibility of eventual renal failure and forms of therapy.',
                B('Patients planning for HD') + ' &#8594; preparation of A-V fistula.',
                B('Patients planning for PD or transplantation') + ' &#8594; early education of family members for selection and preparation of a home dialysis helper or a related donor.'],
               size=14.5, gap='6px')),
       warnbox('II) Renal Replacement Therapy', ['Dialysis and renal transplantation.'], 16)))

# =============================================================== SLIDE 31 ====
write(31, '''
<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:linear-gradient(135deg,#5C3A24 0%%,#7A4A2B 100%%);"></div>
<div style="position:absolute;top:0;right:0;width:380px;height:540px;background:%s;opacity:0.16;"></div>
<div style="position:absolute;top:0;left:0;width:10px;height:540px;background:%s;"></div>
<div style="position:absolute;top:130px;left:80px;z-index:5;">
  <p style="font-size:92px;font-weight:700;color:%s;margin:0;line-height:1;">02</p>
  <div style="width:80px;height:4px;background:%s;margin:14px 0 16px 0;"></div>
  <p style="font-size:40px;font-weight:700;color:#FFF3DC;margin:0;">Renal Replacement Therapy</p>
  <p style="font-size:19px;color:#E8B46A;margin:10px 0 0 0;">Dialysis (Peritoneal &amp; Hemodialysis) &middot; Kidney Transplantation</p>
</div>
''' % (AMBER, AMBER, AMBER, AMBER))

# =============================================================== SLIDE 32 ====
write(32, '''
%s
<div style="position:absolute;top:96px;left:60px;right:60px;z-index:5;display:grid;grid-template-columns:1fr 1fr;gap:16px;">
  %s
  %s
</div>
''' % (title('RRT &mdash; Overview &amp; Definition of Dialysis'),
       card(ch('Renal Replacement Therapy (RRT)', CARAM) +
            ul(['Dialysis (Peritoneal and hemodialysis).',
                'Renal transplantation.'], size=15)),
       card(ch('Dialysis &mdash; Definition', TERRA) +
            ul(['A process of diffusion of substances and water across a semipermeable membrane in both directions (blood on one side and fluid &ldquo;dialysate&rdquo; on the other side of the membrane).'], size=14.5))))

# =============================================================== SLIDE 33 ====
write(33, '''
%s
<div style="position:absolute;top:92px;left:60px;right:60px;z-index:5;display:grid;grid-template-columns:1fr;gap:12px;">
  %s
  %s
</div>
''' % (title('Indications of Dialysis'),
       card(ch('I) Temporary (acute / urgent) dialysis', TERRA) +
            ul(['<b>%s</b> In AKI: many nephrologists advise early dialysis in AKI in all patients, at least for some periods of time, to simplify management which enhances recovery and minimizes development of complications.' % '1.',
                '<b>%s</b> Control of some uremic symptoms and complications (in both AKI and CKD) as:' % '2.',
                '&bull; Refractory hyperkalemia.',
                '&bull; Intractable metabolic acidosis.',
                '&bull; Progressive fluid overload unresponsive to diuretics.',
                '&bull; Pericarditis and pleuritis.',
                '&bull; CNS complications.',
                '&bull; GIT complications.',
                '&bull; Bleeding due to uremia.',
                '<b>%s</b> Removal of dialyzable toxins &amp; drugs as; alcohols, aspirin, lithium, contrast dyes.' % '3.'],
               size=13.5, gap='4px')),
       card(ch('II) Permanent (chronic, regular or maintenance) dialysis', OLIVE) +
            ul(['Grade 5 CKD (ESRD) as replacement therapy when GFR &#8804; 10 ml/min, which may correspond to a serum creatinine of 8&ndash;10 mg/dL.'], size=14.5))))

# =============================================================== SLIDE 34 ====
write(34, '''
%s
<div style="position:absolute;top:96px;left:60px;right:60px;z-index:5;display:grid;grid-template-columns:1fr 1fr;gap:16px;">
  %s
  %s
</div>
''' % (title('Dialysis &mdash; Contraindications &amp; Types'),
       warnbox('Contraindications', ['Refractory hypotension unresponsive to vasopressors.',
                                     'Terminal illness.',
                                     'Organic brain damage.'], 14.5),
       card(ch('Types', CARAM) +
            ul(['Peritoneal dialysis (PD).',
                'Hemodialysis (HD).'], size=15.5))))

# =============================================================== SLIDE 35 ====
write(35, '''
%s
<div style="position:absolute;top:92px;left:60px;right:60px;z-index:5;display:grid;grid-template-columns:1fr 1fr;gap:16px;">
  %s
  %s
</div>
''' % (title('Peritoneal Dialysis &mdash; Principles &amp; Indications'),
       card(ch('Principles', OLIVE) +
            ul(['Utilizes the peritoneal membrane (with its capillaries) as a semipermeable membrane.',
                'When fluid is introduced into the peritoneal cavity it equilibrates with the extracellular fluid.',
                'Removal of the introduced fluid (effluent) results in removal of waste products (solutes) and excess fluid from the body.'], size=13.5, gap='5px')),
       card(ch('Indications &mdash; all patients with symptomatic uremia; specific indications:', TERRA) +
            ul(['<b>%s</b> A slowly rising urea.' % '1.',
                '<b>%s</b> Patients with cardiovascular or hemodynamic instability.' % '2.',
                '<b>%s</b> Absence of H.D. facilities.' % '3.',
                '<b>%s</b> Patients with immature A-V fistula.' % '4.',
                '<b>%s</b> Poor vascular access.' % '5.',
                '<b>%s</b> High risk of anticoagulation in a dialysis dependent patient.' % '6.'],
               size=13.5, gap='4px'))))

# =============================================================== SLIDE 36 ====
write(36, '''
%s
<div style="position:absolute;top:92px;left:60px;right:60px;z-index:5;display:grid;grid-template-columns:1fr 1fr;gap:16px;">
  %s
  %s
</div>
''' % (title('Peritoneal Dialysis &mdash; Contraindications'),
       card(ch('Absolute Contraindications', TERRA) +
            ul(['<b>%s</b> Peritoneal fibrosis (&gt; 50%%) &mdash; inadequate peritoneal surface area for dialysis.' % '1.',
                '<b>%s</b> Pleuro-peritoneal leak &#8594; hydrothorax.' % '2.',
                '<b>%s</b> Multiple large abdominal wounds with drains.' % '3.'],
               size=13.5, gap='5px')),
       card(ch('Relative Contraindications', CARAM) +
            ul(['<b>%s</b> Abdominal problems; colostomy, nephrostomy, recent abdominal or thoracic surgery, extensive abdominal adhesions, hernia, abdominal malignancy.' % '1.',
                '<b>%s</b> Severe hypercatabolic states e.g. burn.' % '2.',
                '<b>%s</b> Fresh or infected aortic prosthesis.' % '3.',
                '<b>%s</b> Huge polycystic kidneys (insufficient intraperitoneal space).' % '4.',
                '<b>%s</b> Active diverticulosis.' % '5.',
                '<b>%s</b> Morbid obesity (inadequate clearance).' % '6.',
                '<b>%s</b> Hyperlipidemia.' % '7.',
                '<b>%s</b> Severe gastroparesis (worsening vomiting).' % '8.',
                '<b>%s</b> For self-care (home dialysis) patient.' % '9.'],
               size=12.5, gap='3px'))))

# =============================================================== SLIDE 37 ====
write(37, '''
%s
<div style="position:absolute;top:96px;left:60px;right:60px;z-index:5;">
  %s
</div>
''' % (title('Peritoneal Dialysis &mdash; Advantages'),
       card(ul(['<b>%s</b> Safe and easy to perform.' % '1.',
                '<b>%s</b> Preserves residual renal function.' % '2.',
                '<b>%s</b> No routine anticoagulation.' % '3.',
                '<b>%s</b> Avoidance of vascular surgery.' % '4.',
                '<b>%s</b> Slow clearance rate &#8594; fewer dialysis-related symptoms e.g. disequilibrium or hypotension.' % '5.',
                '<b>%s</b> Better control of PTH.' % '6.',
                '<b>%s</b> More liberal diet.' % '7.',
                '<b>%s</b> Fewer medications.' % '8.',
                '<b>%s</b> Less expensive than HD.' % '9.',
                '<b>%s</b> Less risk of transmission of blood-borne viruses.' % '10.'],
               size=14.5, gap='4px'), OLIVE)))

# =============================================================== SLIDE 38 ====
write(38, '''
%s
<div style="position:absolute;top:96px;left:60px;right:60px;z-index:5;display:grid;grid-template-columns:1fr 1fr;gap:16px;">
  %s
  %s
</div>
''' % (title('Peritoneal Dialysis &mdash; Disadvantages &amp; Complications (1)'),
       card(ch('Disadvantages', TERRA) +
            ul(['<b>%s</b> Long time.' % '1.',
                '<b>%s</b> Low efficiency.' % '2.',
                '<b>%s</b> Inadequate clearance in some patients e.g. malignant hypertension, peritoneal disease, vasculitis.' % '3.',
                '<b>%s</b> Contraindicated in recent abdominal surgery or pulmonary compromise.' % '4.',
                '<b>%s</b> Associated complications.' % '5.'],
               size=13.5, gap='5px')),
       card(ch('Complications (1&ndash;6)', CARAM) +
            ul(['<b>%s</b> Peritonitis.' % '1.',
                '<b>%s</b> Catheter exit site infection.' % '2.',
                '<b>%s</b> Constipation.' % '3.',
                '<b>%s</b> Leakage of dialysate through a diaphragmatic defect into the thoracic cavity &#8594; massive pleural effusion and respiratory embarrassment, or to the scrotum.' % '4.',
                '<b>%s</b> Failure of peritoneal membrane function &#8594; ultrafiltration failure.' % '5.',
                '<b>%s</b> Sclerosing peritonitis (rare but potentially fatal).' % '6.'],
               size=13, gap='4px'))))

# =============================================================== SLIDE 39 ====
write(39, '''
%s
<div style="position:absolute;top:96px;left:60px;right:60px;z-index:5;">
  %s
</div>
''' % (title('Peritoneal Dialysis &mdash; Complications (2)'),
       card(ul(['<b>%s</b> Moderate protein loss &#8594; malnutrition.' % '7.',
                '<b>%s</b> Hyperlipidemia &#8594; accelerated atherosclerosis.' % '8.',
                '<b>%s</b> Obesity due to mobilization of glucose from the dialysate to the body.' % '9.',
                '<b>%s</b> Inguinal and abdominal hernias.' % '10.',
                '<b>%s</b> Traumatic perforation of an abdominal organ (bowel, bladder, blood vessel).' % '11.',
                '<b>%s</b> Clotting of the cannula.' % '12.'],
               size=15, gap='8px'), TERRA)))

# =============================================================== SLIDE 40 ====
write(40, '''
%s
<div style="position:absolute;top:92px;left:60px;right:60px;z-index:5;display:grid;grid-template-columns:1fr 1fr;gap:16px;">
  %s
  %s
</div>
''' % (title('Hemodialysis &mdash; Definition &amp; Advantages'),
       card(ch('Definition', TERRA) +
            ul(['A process of diffusion across a semipermeable membrane, to remove unwanted substances from blood while adding desirable components.'], size=14.5)),
       card(ch('Advantages of HD', OLIVE) +
            ul(['<b>%s</b> Relatively short time, causing minimal interruption of lifestyle between treatments.' % '1.',
                '<b>%s</b> More efficient than PD.' % '2.',
                '<b>%s</b> Can be performed in the home.' % '3.'],
               size=14, gap='6px'))))

# =============================================================== SLIDE 41 ====
write(41, '''
%s
<div style="position:absolute;top:92px;left:60px;right:60px;z-index:5;display:grid;grid-template-columns:1fr 1fr;gap:16px;">
  %s
  %s
</div>
''' % (title('HD &mdash; Surgical Complications (Vascular Access)'),
       card(ch('Of Catheters', TERRA) +
            ul(['Bleeding.',
                'Infection.',
                'Thrombosis or stenosis of the vessels.',
                'Pneumothorax.',
                'Air embolism.'], size=13.5, gap='4px')),
       card(ch('Of A-V Fistula and of Graft', CARAM) +
            ul(['<b>%s</b> Stenosis &#8594; inadequate blood flow.' % '1.',
                '<b>%s</b> Thrombosis.' % '2.',
                '<b>%s</b> Infection.' % '3.',
                '<b>%s</b> Failure to develop adequate venous outflow.' % '4.',
                '<b>%s</b> Vascular steal &#8594; limb ischemia.' % '5.',
                '<b>%s</b> Venous hypertension syndrome (distal venous stasis &#8594; skin necrosis).' % '6.',
                '<b>%s</b> High output heart failure.' % '7.',
                '<b>%s</b> Pseudo-aneurysms.' % '8.'],
               size=12.5, gap='3px'))))

# =============================================================== SLIDE 42 ====
write(42, '''
%s
<div style="position:absolute;top:92px;left:60px;right:60px;z-index:5;">
  %s
</div>
''' % (title('HD &mdash; Acute Medical Complications'),
       card(ul(['<b>%s</b> Intradialytic hypotension (IDH).' % '1.',
                '<b>%s</b> Hypertension.' % '2.',
                '<b>%s</b> Cramps.' % '3.',
                '<b>%s</b> Nausea and vomiting.' % '4.',
                '<b>%s</b> Headache.' % '5.',
                '<b>%s</b> Fever.' % '6.',
                '<b>%s</b> Hemolysis: rare, but potentially serious.' % '7.',
                '<b>%s</b> Bleeding: anticoagulant overdose.' % '8.',
                '<b>%s</b> Clotting of extracorporeal circuit (blood lines and dialyzer).' % '9.',
                '<b>%s</b> Chest pain.' % '10.',
                '<b>%s</b> Arrhythmias.' % '11.',
                '<b>%s</b> Cardiac arrest in the dialysis unit.' % '12.',
                '<b>%s</b> Air embolism.' % '13.',
                '<b>%s</b> Disequilibrium syndrome.' % '14.'],
               size=14, gap='3px'), TERRA)))

# =============================================================== SLIDE 43 ====
write(43, '''
%s
<div style="position:absolute;top:92px;left:60px;right:60px;z-index:5;">
  <p style="font-size:16px;font-weight:700;color:%s;margin:0 0 8px 0;">Chronic (Long-term) HD Complications &mdash; 1. Cardiovascular Disease</p>
  %s
</div>
''' % (title('HD &mdash; Chronic Complications (1): Cardiovascular'),
       HEAD,
       card(ch('Dialysis patients are more likely to die from CV disease than the general population. The cause is multifactorial; cardiac or vascular.', TERRA) +
            grid('1fr 1fr') +
            card(ch('Cardiac', TERRA) +
                 ul(['Ischemic heart disease.',
                     'Valvular heart disease (aortic and mitral valves).',
                     'Uremic pericarditis and pericardial effusion.',
                     'Uremic endocarditis.',
                     'Cardiomyopathy (dilated).'], size=13.5, gap='4px'), TERRA) +
            card(ch('Vascular', OLIVE) +
                 ul([B('Peripheral vascular disease') + ' due to:',
                     '&bull; Decreased peripheral blood flow, related to vascular access.',
                     '&bull; Hypertension and dyslipidemia.',
                     B('Metastatic calcification:') + ' abnormal calcification of soft tissues due to persistent elevation of plasma phosphate and calcium.'],
                    size=13.5, gap='4px'), OLIVE) +
            '</div>')))

# =============================================================== SLIDE 44 ====
write(44, '''
%s
<div style="position:absolute;top:96px;left:60px;right:60px;z-index:5;display:grid;grid-template-columns:1fr 1fr;gap:16px;">
  %s
  %s
</div>
''' % (title('HD &mdash; Chronic Complications (2)'),
       card(ch('Neuropsychiatric, Nutrition &amp; Bone', CARAM) +
            ul([B('Neuropsychiatric complications: ') + 'anxiety, depression, dementia.',
                B('Malnutrition.'),
                B('Dialysis osteomalacia.'),
                B('Dialysis related amyloidosis (DRA).')], size=13.5, gap='5px')),
       card(ch('Rheumatologic &amp; Other', OLIVE) +
            ul([B('Rheumatologic complications:'),
                '&bull; Crystal-induced arthritis.',
                '&bull; Infection of joints and bone.',
                '&bull; Ischemic necrosis of bone.',
                B('Hypersplenism.'),
                B('Acquired renal cystic disease:'),
                '&bull; In patients with prolonged dialysis &gt; 3 years.',
                '&bull; May show malignant changes.'], size=13.5, gap='4px'))))

# =============================================================== SLIDE 45 ====
write(45, '''
%s
<div style="position:absolute;top:92px;left:60px;right:60px;z-index:5;display:grid;grid-template-columns:1fr 1fr;gap:16px;">
  %s
  %s
</div>
''' % (title('Kidney Transplantation &mdash; Definition, Donors &amp; Contraindications'),
       card('<div style="margin-bottom:10px;">' + ch('Definition', TERRA) +
            ul(['Surgical implantation of a kidney obtained from either a healthy kidney donor or a brain stem dead cadaver (deceased).'], size=13.5) + '</div>' +
            ch('Types of Donors', OLIVE) +
            ul(['Living (blood related, unrelated) donor.',
                'Deceased (cadaveric) donor.'], size=13.5)),
       card(ch('Contraindications', TERRA) +
            ul(['<b>%s</b> Patient&rsquo;s refusal.' % '1.',
                '<b>%s</b> Psychosis.' % '2.',
                '<b>%s</b> Elderly (relative contraindication).' % '3.',
                '<b>%s</b> Active sepsis.' % '4.',
                '<b>%s</b> Unstable cardiovascular disease.' % '5.',
                '<b>%s</b> Severe respiratory distress.' % '6.',
                '<b>%s</b> Cerebro-vascular hemorrhage.' % '7.',
                '<b>%s</b> Advanced liver disease; unless combined liver and kidney transplantation.' % '8.',
                '<b>%s</b> Malignancies.' % '9.',
                '<b>%s</b> Un-repairable urological abnormalities.' % '10.'],
               size=12.5, gap='2px'))))

# =============================================================== SLIDE 46 ====
write(46, '''
%s
<div style="position:absolute;top:92px;left:60px;right:60px;z-index:5;display:grid;grid-template-columns:1fr 1fr;gap:16px;">
  %s
  %s
</div>
''' % (title('Transplantation &mdash; Common Complications'),
       card(ch('Surgical Complications', TERRA) +
            ul(['<b>%s</b> Technical failures.' % '1.',
                '<b>%s</b> Renal vein and renal artery thrombosis.' % '2.',
                '<b>%s</b> Urine leakage at uretero-vesical anastomosis.' % '3.',
                '<b>%s</b> Leg edema (lymphedema) on the same side of the implanted kidney.' % '4.'],
               size=13.5, gap='5px')),
       card(ch('Medical Complications', OLIVE) +
            ul(['<b>%s</b> Acute tubular necrosis (ATN).' % '1.',
                '<b>%s</b> Rejection (hyperacute, acute, chronic).' % '2.',
                '<b>%s</b> Complications of immunosuppression.' % '3.',
                '<b>%s</b> Recurrence of the primary renal disease.' % '4.',
                '<b>%s</b> Infection (opportunistic).' % '5.',
                '<b>%s</b> Malignancy (Kaposi sarcoma of the skin, lymphoproliferative).' % '6.',
                '<b>%s</b> Hypertension, DM, atherosclerosis, bone disease.' % '7.',
                '<b>%s</b> GIT bleeding, cataract, bone marrow suppression.' % '8.',
                '<b>%s</b> Nephrotoxicity and hepatotoxicity.' % '9.'],
               size=12.5, gap='2px'))))

# =============================================================== SLIDE 47 ====
write(47, '''
%s
<div style="position:absolute;top:26px;left:60px;right:60px;z-index:5;">
  <p style="font-size:30px;font-weight:700;color:%s;margin:0;">Summary</p>
  <div style="width:64px;height:4px;background:%s;margin:8px 0 18px 0;border-radius:2px;"></div>
</div>
<div style="position:absolute;top:86px;left:60px;right:60px;z-index:5;display:grid;grid-template-columns:1fr 1fr 1fr;gap:13px;">
  %s
  %s
  %s
  %s
  %s
  %s
</div>
''' % ('', HEAD, AMBER,
       card(ch('CKD Essentials', TERRA) + ul(['Structure/function abnormalities &gt; 3 months.',
       'Classified by cause + GFR (G1&ndash;G5) + albuminuria (A1&ndash;A3).',
       'ESRD = Grade 5 = needs RRT.'], size=12.5, gap='4px'), TERRA),
       card(ch('Clinical Picture', CARAM) + ul(['GIT: anorexia, vomiting, uremic fetor.',
       'CVS: CHF, HTN, pericarditis, atherosclerosis.',
       'Hematological: anemia, bleeding, infections.',
       'Bone: CKD-MBD &amp; renal osteodystrophy.',
       'Neuro, skin, urinary &amp; electrolyte disturbances.'], size=12.5, gap='4px'), CARAM),
       card(ch('Investigations', OLIVE) + ul(['Urine analysis, KFT (urea, creatinine, eGFR), electrolytes, ABG.',
       'Iron profile, iPTH, skeletal survey.',
       'Serology, renal imaging, biopsy (not if small atrophic kidneys).'], size=12.5, gap='4px'), OLIVE),
       card(ch('Conservative Treatment', OLIVE) + ul(['Correct reversible causes &amp; underlying disease.',
       'Control BP, glucose, proteinuria (ACEI/ARBs), lipids, lifestyle.',
       'Diet, GIT, CVS, MBD, anemia &amp; pruritus management.',
       'Educational programs.'], size=12.5, gap='4px'), OLIVE),
       card(ch('Dialysis', CARAM) + ul(['PD: peritoneum as membrane; safe, preserves residual function.',
       'HD: efficient, short time; vascular-access surgical complications + acute/chronic medical complications.',
       'Indications: AKI, uremic complications, toxins, ESRD (GFR &#8804; 10).'], size=12.5, gap='4px'), CARAM),
       card(ch('Transplantation', TERRA) + ul(['Living or deceased donor.',
       'Contraindications: refusal, psychosis, sepsis, malignancy, etc.',
       'Complications: rejection, immunosuppression, infection, malignancy.'], size=12.5, gap='4px'), TERRA)))

# =============================================================== SLIDE 48 ====
write(48, '''
<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:linear-gradient(135deg,#5C3A24 0%,#8A5A33 100%);"></div>
<div style="position:absolute;top:0;left:0;width:960px;height:540px;">
  <svg width="960" height="540" xmlns="http://www.w3.org/2000/svg">
    <circle cx="150" cy="120" r="180" fill="rgba(217,164,91,0.10)"/>
    <circle cx="840" cy="460" r="200" fill="rgba(168,74,42,0.12)"/>
    <line x1="70" y1="180" x2="170" y2="180" stroke="#D9A45B" stroke-width="5"/>
  </svg>
</div>
<div style="position:absolute;top:150px;left:75px;z-index:5;">
  <p style="font-size:44px;color:#FFE9C2;font-weight:700;margin:0;">Thank You</p>
  <p style="font-size:20px;color:rgba(255,240,214,0.85);margin:14px 0 0 0;">Chronic Kidney Disease &amp; Renal Replacement Therapy</p>
  <p style="font-size:16px;color:rgba(255,240,214,0.55);margin:34px 0 0 0;">Principles of Nephrology &mdash; Dr. Hassan Abd-Elhady, Menoufia University</p>
</div>
''', cover=True)

print('Generated %d slides in %s' % (48, OUT))
