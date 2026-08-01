#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convert MD files -> full-content HTML slides (960x540).
Brown light-mode theme, harmony colors, contrast for important info.
Palette:
  bg        #F4EADA  light warm brown parchment
  panel     #FBF5E9  cream card
  panel2    #ECDDC2  tan card
  ink       #3B2A1A  main dark text
  sub       #7A5A3A  muted brown
  heading   #55361C  dark chocolate headings
  caramel   #C08A3E  golden-brown accent
  amber     #E8B84B  light label on dark boxes
  terracotta #B0502A strong contrast accent (important)
  terraDark #7A2E12
  olive     #6E7A3E  secondary harmony accent
  deep      #4A3118  dark important-box background
"""

import os

C = {
    'bg': '#F4EADA', 'panel': '#FBF5E9', 'panel2': '#ECDDC2',
    'ink': '#3B2A1A', 'sub': '#7A5A3A', 'heading': '#55361C',
    'caramel': '#C08A3E', 'amber': '#E8B84B', 'terracotta': '#B0502A',
    'terraDark': '#7A2E12', 'olive': '#6E7A3E', 'deep': '#4A3118',
}

def badge(num):
    return f'''<svg style="position:absolute;right:32px;bottom:22px;width:44px;height:34px;z-index:100;" aria-hidden="true">
  <rect x="0" y="0" width="44" height="34" rx="6" fill="#C08A3E"/>
  <text x="22" y="24" font-family="Times New Roman,serif" font-size="17" font-weight="700" fill="#FBF5E9" text-anchor="middle">{num}</text>
</svg>'''

def slide_html(body, num):
    b = badge(num)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
html, body {{ margin:0; padding:0; width:100%; height:100%; overflow:hidden; display:flex; justify-content:center; align-items:center; background:#2E2012; }}
.slide-content {{ width:960px; height:540px; position:relative; transform-origin:center center; }}
</style>
<script>
function scaleSlide(){{const s=document.querySelector('.slide-content');if(!s)return;const sx=window.innerWidth/960;const sy=window.innerHeight/540;const sc=Math.min(sx,sy);s.style.width='960px';s.style.height='540px';s.style.transform='scale('+sc+')';s.style.transformOrigin='center center';s.style.flexShrink='0';}}
window.addEventListener('load',scaleSlide);window.addEventListener('resize',scaleSlide);
</script>
</head>
<body>
<div class="slide-content" style="width:960px;height:540px;background:#F4EADA;font-family:'Times New Roman',serif;overflow:hidden;">
{body}
{b}
</div>
</body>
</html>'''

def header(kicker, title):
    return f'''<div style="position:absolute;top:24px;left:56px;right:56px;z-index:10;">
  <p style="font-size:13px;letter-spacing:2.5px;color:#6E7A3E;margin:0 0 3px 0;font-weight:700;text-transform:uppercase;">{kicker}</p>
  <p style="font-size:28px;font-weight:700;color:#55361C;margin:0;line-height:1.12;">{title}</p>
  <div style="width:74px;height:4px;background:#C08A3E;margin-top:7px;border-radius:2px;"></div>
</div>'''

def content_open(extra=''):
    return f'<div style="position:absolute;top:100px;left:56px;right:56px;bottom:56px;z-index:10;{extra}">'

def content_close():
    return '</div>'

def card(title, accent, body_html, bg=None, pad='12px 14px'):
    b = bg or C['panel']
    return f'''<div style="background:{b};border-radius:10px;padding:{pad};border-left:4px solid {accent};box-shadow:0 1px 4px rgba(85,54,28,0.12);">
  <p style="font-size:17px;font-weight:700;color:#55361C;margin:0 0 5px 0;">{title}</p>
  {body_html}
</div>'''

def bullets(items, size='14px', gap='5px', color=None, pad='0 0 0 17px'):
    col = color or C['ink']
    lis = ''
    for it in items:
        lis += f'<li style="margin-bottom:{gap};line-height:1.42;">{it}</li>'
    return f'<ul style="margin:0;padding:{pad};font-size:{size};color:{col};">{lis}</ul>'

def important(label, text):
    return f'''<div style="background:#4A3118;border-radius:10px;padding:11px 15px;border-left:4px solid #C08A3E;box-shadow:0 1px 5px rgba(74,49,24,0.35);">
  <p style="font-size:14px;color:#FBF5E9;margin:0;line-height:1.45;"><b style="color:#E8B84B;">{label}:</b> {text}</p>
</div>'''

def caution(label, text):
    return f'''<div style="background:#F7E3D8;border:1.5px solid #B0502A;border-radius:9px;padding:8px 13px;">
  <p style="font-size:13.5px;color:#7A2E12;margin:0;line-height:1.42;"><b>{label}:</b> {text}</p>
</div>'''

def keyterm(text):
    return f'<b style="color:#B0502A;">{text}</b>'

def data_table(headers, rows, widths=None, size='13.5px'):
    ths = ''.join(f'<th style="padding:8px 10px;text-align:left;font-size:{size};color:#FBF5E9;">{h}</th>' for h in headers)
    trs = ''
    for i, row in enumerate(rows):
        bg = '#FBF5E9' if i % 2 == 0 else '#F1E4CC'
        tds = ''.join(f'<td style="padding:7px 10px;text-align:left;font-size:{size};color:#3B2A1A;vertical-align:top;">{c}</td>' for c in row)
        trs += f'<tr style="background:{bg};border-bottom:1px solid #E0CDAA;">{tds}</tr>'
    return f'''<table style="width:100%;border-collapse:collapse;border-radius:10px;overflow:hidden;box-shadow:0 1px 4px rgba(85,54,28,0.12);">
  <tr style="background:#4A3118;">{ths}</tr>
  {trs}
</table>'''

def cover(title, subtitle, kicker, topics, source):
    return f'''<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:linear-gradient(150deg,#EBD8B8 0%,#DEC399 55%,#D3B485 100%);"></div>
<svg style="position:absolute;top:-70px;right:-90px;width:520px;height:420px;z-index:1;" aria-hidden="true">
  <ellipse cx="260" cy="210" rx="230" ry="300" fill="#C08A3E" opacity="0.16"/>
</svg>
<svg style="position:absolute;bottom:-110px;left:-70px;width:420px;height:360px;z-index:1;" aria-hidden="true">
  <circle cx="210" cy="180" r="230" fill="#6E7A3E" opacity="0.10"/>
</svg>
<div style="position:absolute;top:0;left:0;width:14px;height:540px;background:#B0502A;"></div>
<div style="position:absolute;top:0;right:0;width:6px;height:540px;background:#C08A3E;"></div>
<div style="position:absolute;top:118px;left:72px;z-index:10;">
  <div style="width:84px;height:5px;background:#B0502A;margin-bottom:16px;border-radius:2px;"></div>
  <p style="font-size:22px;color:#6E7A3E;margin:0;font-weight:700;letter-spacing:3px;text-transform:uppercase;">{kicker}</p>
  <p style="font-size:56px;color:#3B2A1A;margin:10px 0 0 0;font-weight:700;line-height:1.08;">{title}</p>
  <p style="font-size:30px;color:#B0502A;margin:8px 0 0 0;font-weight:700;">{subtitle}</p>
  <div style="width:60px;height:4px;background:#C08A3E;margin:22px 0 14px 0;border-radius:2px;"></div>
  <p style="font-size:19px;color:#55361C;margin:0;">{topics}</p>
</div>
<div style="position:absolute;bottom:26px;left:72px;z-index:10;">
  <p style="font-size:15px;color:#3B2A1A;margin:0;font-weight:700;">Internal Medicine · Nephrology</p>
  <p style="font-size:13px;color:#7A5A3A;margin:3px 0 0 0;">{source}</p>
</div>'''

def toc(items):
    rows = ''
    for n, (t, d) in enumerate(items, 1):
        rows += f'''<div style="display:flex;align-items:center;gap:14px;background:#FBF5E9;padding:9px 16px;border-radius:9px;border-left:4px solid #C08A3E;box-shadow:0 1px 4px rgba(85,54,28,0.10);">
      <span style="font-size:19px;font-weight:700;color:#B0502A;min-width:34px;">{n:02d}</span>
      <span style="font-size:17.5px;color:#3B2A1A;">{t}</span>
      <span style="flex:1;"></span>
      <span style="font-size:12.5px;color:#7A5A3A;font-style:italic;">{d}</span>
    </div>'''
    return f'''<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:#F4EADA;"></div>
<div style="position:absolute;top:30px;left:60px;z-index:10;">
  <p style="font-size:32px;font-weight:700;color:#55361C;margin:0;">Table of Contents</p>
  <div style="width:74px;height:4px;background:#B0502A;margin-top:10px;border-radius:2px;"></div>
</div>
<div style="position:absolute;top:100px;left:60px;right:60px;z-index:10;display:grid;grid-template-columns:1fr 1fr;gap:12px 26px;">
{rows}
</div>'''

def divider(num, title, subtitle, desc):
    return f'''<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:linear-gradient(150deg,#EFE0C6 0%,#E4CEA9 100%);"></div>
<div style="position:absolute;top:0;right:0;width:330px;height:540px;background:#6E7A3E;opacity:0.14;"></div>
<div style="position:absolute;top:0;left:0;width:10px;height:540px;background:#B0502A;"></div>
<div style="position:absolute;top:0;right:0;width:5px;height:540px;background:#C08A3E;"></div>
<div style="position:absolute;top:150px;left:82px;z-index:10;">
  <p style="font-size:92px;font-weight:700;color:#C08A3E;margin:0;line-height:1;">{num}</p>
  <div style="width:84px;height:4px;background:#B0502A;margin:12px 0 14px 0;border-radius:2px;"></div>
  <p style="font-size:37px;font-weight:700;color:#3B2A1A;margin:0;line-height:1.1;">{title}</p>
  <p style="font-size:20px;color:#B0502A;margin:9px 0 0 0;font-weight:700;">{subtitle}</p>
  <p style="font-size:15px;color:#7A5A3A;margin:14px 0 0 0;max-width:600px;line-height:1.45;">{desc}</p>
</div>'''

slides = []

# ---------- 1. COVER ----------
slides.append(cover(
    'Structural & Vascular Renal Diseases',
    'Cystic Kidney Diseases · Hypertensive Nephrosclerosis',
    'Internal Medicine · Nephrology',
    'Simple Renal Cysts · ADPKD · ARPKD · Hypertensive Nephrosclerosis',
    'Principles of Nephrology — Dr. Hassan Abd-Elhady, Menoufia University'
))

# ---------- 2. TOC ----------
slides.append(toc([
    ('Cystic Kidney Diseases', 'Chapters 1–3'),
    ('I- Simple (Solitary) Renal Cysts', 'Ch. 1'),
    ('II- ADPKD', 'Ch. 2'),
    ('II- ARPKD', 'Ch. 3'),
    ('Hypertensive Nephrosclerosis', 'Chapter 4'),
    ('Definition & Risk Factors', 'Ch. 4'),
    ('Diagnosis & Management', 'Ch. 4'),
    ('Summary & References', 'Recap'),
]))

# ---------- 3. DIVIDER Ch1 ----------
slides.append(divider('01', 'Cystic Kidney Diseases',
    'Simple Renal Cysts · ADPKD · ARPKD',
    'Hereditary and non-hereditary cystic diseases of the kidney — incidence, clinical picture, diagnosis and treatment.'))

# ---------- 4. Simple cysts: incidence ----------
body = header('Cystic Kidney Diseases · I- Simple (Solitary) Renal Cysts', 'Incidence')
body += content_open()
body += card('Epidemiology & Nature', C['terracotta'], bullets([
    f'Are <b>common</b> — present in <b>50% of persons aged &gt;50 years</b>.',
    f'They are <b>not inherited</b> and do <b>not affect the renal function</b>.',
    f'Commonly <b>&lt; 2 cm</b> &amp; typically <b>solitary</b>, but occasionally may be <b>multiple &amp; bilateral</b>.',
    f'Most of them are <b>cortical</b> in site and often <b>bulge through the renal capsule</b>.',
]))
body += content_close()
slides.append(body)

# ---------- 5. Simple cysts: presentations ----------
body = header('Cystic Kidney Diseases · I- Simple (Solitary) Renal Cysts', 'Presentations')
body += content_open()
body += f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;height:100%;">
  {card('Commonly Asymptomatic', C['olive'], bullets([
      f'Discovered <b>incidentally</b> in clinical exam or imaging.',
  ]), bg=C['panel'])}
  {card('Rarely Symptomatic — There May Be', C['terracotta'], bullets([
      f'<b>Abdominal mass</b>.',
      f'<b>Hematuria</b> (rare and should {keyterm("raise a suspicion")} of {keyterm("renal cell carcinoma")}).',
      f'Occasionally, <b>hypertension</b> caused by compression of intra-renal vessels.',
      f'<b>Normal renal functions</b>, and <b>prognosis is excellent</b> without treatment.',
      f'<b>Complications</b>; e.g. <b>hemorrhage</b>, <b>infection</b> (fever, pain, pyuria), or <b>carcinoma</b>.',
  ]), bg=C['panel'])}
</div>'''
body += content_close()
slides.append(body)

# ---------- 6. Simple cysts: diagnosis (US) ----------
body = header('Cystic Kidney Diseases · I- Simple (Solitary) Renal Cysts', 'Diagnosis — by Renal Imaging (US / CT)')
body += content_open()
body += f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;height:225px;">
  {card('Ultrasound — 3 Sonographic Criteria', C['caramel'], f'''<ol style="margin:0;padding-left:19px;font-size:14px;color:#3B2A1A;line-height:1.5;">
    <li style="margin-bottom:6px;">{keyterm('Echoes-free')} (i.e. homogeneous)</li>
    <li style="margin-bottom:6px;">{keyterm('Sharply demarcated')} with smooth thin wall</li>
    <li>An <b>enhanced back wall</b>.</li>
  </ol>''', bg=C['panel'])}
  {card('CT', C['terracotta'], bullets([
      f'{keyterm("Sharply demarcated")}, smooth thin wall cyst.',
      f'<b>Not enhanced</b> with contrast media ({keyterm("renal cell carcinoma does")}).',
  ]), bg=C['panel'])}
</div>
<div style="margin-top:13px;">
  {important('Key Point', 'The enhancement pattern with contrast distinguishes a simple cyst from <b>renal cell carcinoma</b> — a simple cyst does not enhance, RCC does.')}
</div>'''
body += content_close()
slides.append(body)

# ---------- 7. Simple cysts: DDx ----------
body = header('Cystic Kidney Diseases · I- Simple (Solitary) Renal Cysts', 'Differential Diagnosis')
body += content_open()
body += f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;height:100%;">
  {card('Renal Abscess', C['olive'], bullets([
      f'Infected fluid collection — usually with <b>fever, pain and pyuria</b>.',
      f'Differentiated by <b>clinical picture</b> and <b>imaging</b> (thick irregular wall, internal echoes / debris).',
  ]), bg=C['panel2'])}
  {card('Polycystic Kidney Disease (PCKD)', C['terracotta'], bullets([
      f'<b>Multiple bilateral cysts</b> with <b>family history</b> and systemic involvement.',
      f'Associated with <b>renal failure</b>, hypertension and extra-renal cysts.',
  ]), bg=C['panel2'])}
</div>'''
body += content_close()
slides.append(body)

# ---------- 8. Simple cysts: treatment ----------
body = header('Cystic Kidney Diseases · I- Simple (Solitary) Renal Cysts', 'Treatment')
body += content_open()
rows = [
    ('Asymptomatic cysts', 'Periodic reevaluation.'),
    ('Large cyst', f'May require <b>aspiration and alcohol instillation</b>. If contains <b>&gt; 500 ml</b> of fluid should be <b>drained surgically</b>.'),
    ('Infected cyst', 'Should be differentiated from <b>abscess</b> &amp; treated with <b>antibiotics</b>.'),
    ('Hypertension', 'May <b>improve after decompression</b> of the cyst.'),
]
body += data_table(['Condition', 'Management'], rows)
body += f'''<div style="margin-top:13px;">
  {caution('Remember', 'Rare hematuria should always raise a suspicion of <b>renal cell carcinoma</b>.')}
</div>'''
body += content_close()
slides.append(body)

# ---------- 9. DIVIDER Ch2 ADPKD ----------
slides.append(divider('02', 'Autosomal Dominant Polycystic Kidney Disease (ADPKD)',
    'Hereditary Polycystic Kidney Disease',
    'Inherited as autosomal dominant; genetic defect on chromosome 16 (ADPKD-1) and chromosome 4 (ADPKD-2).'))

# ---------- 10. ADPKD incidence ----------
body = header('Cystic Kidney Diseases · II- Hereditary PKD · ADPKD', 'Incidence')
body += content_open()
body += f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;height:250px;">
  {card('Epidemiology', C['caramel'], bullets([
      f'It is a <b>relatively common familial condition</b>.',
      f'Common age: <b>middle age (40 years)</b>, but may present at <b>any age</b>.',
  ]), bg=C['panel'])}
  {card('Genetics', C['terracotta'], bullets([
      f'Inherited as a simple <b>autosomal dominant (AD)</b>.',
      f'Genetic defect on <b>chromosome 16</b> → <b>ADPKD-1</b>.',
      f'Genetic defect on <b>chromosome 4</b> → <b>ADPKD-2</b>.',
  ]), bg=C['panel'])}
</div>
<div style="margin-top:13px;">
  {important('Important', 'ADPKD is a <b>systemic disease</b> — it involves organs other than the kidneys.')}
</div>'''
body += content_close()
slides.append(body)

# ---------- 11. ADPKD clinical features (table 1) ----------
body = header('Cystic Kidney Diseases · ADPKD', 'Clinical Features — Symptoms & Causes (1/2)')
body += content_open()
rows = [
    (f'{keyterm("Hematuria")}',
     'Due to; <b>rupture of a cyst</b> into the renal pelvis, <b>renal stone</b> or <b>UTI</b>.'),
    (f'{keyterm("Renal infection")}',
     'Flank pain, fever, and leukocytosis. Blood cultures may be positive and urine analysis may be normal because the cyst <b>does not communicate directly with the urinary tract</b>.'),
]
body += data_table(['Symptom', 'Cause'], rows)
body += f'''<div style="margin-top:13px;">
  {important('Exam Pearl', 'In ADPKD, <b>urine analysis may be normal</b> during cyst infection — the infected cyst does not communicate with the urinary tract; blood cultures are more reliable.')}
</div>'''
body += content_close()
slides.append(body)

# ---------- 12. ADPKD clinical features (table 2) ----------
body = header('Cystic Kidney Diseases · ADPKD', 'Clinical Features — Symptoms & Causes (2/2)')
body += content_open()
rows = [
    (f'{keyterm("Nephrolithiasis")}', 'Mainly <b>calcium oxalate</b> stone.'),
    (f'{keyterm("Abdominal Pain or flank pain")}', 'Due to <b>infection</b>, <b>bleeding into cyst</b>, <b>rupture of cysts</b>, or <b>nephrolithiasis</b>.'),
    (f'{keyterm("Hypertension")}', f'In <b>50% of patients</b> and increases with renal failure. Due to <b>cyst-induced ischemia with activation of RAAS</b> (cyst decompression can lower blood pressure temporarily).'),
    (f'{keyterm("Mild anemia")}', 'Relative to the <b>degree of renal failure</b>.'),
    (f'{keyterm("Kidney Enlargement")}', 'The kidneys may be <b>palpable</b> with <b>irregular surface</b>.'),
]
body += data_table(['Symptom', 'Cause'], rows)
body += content_close()
slides.append(body)

# ---------- 13. ADPKD associated abnormalities ----------
body = header('Cystic Kidney Diseases · ADPKD', 'Associated Abnormalities — Systemic Disease')
body += content_open()
body += f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;height:250px;">
  {card('Abdominal / Visceral', C['olive'], bullets([
      f'<b>Hepatic cysts</b> (in <b>50% of patients</b>) — usually cause <b>no functional impairment</b>.',
      f'<b>Pancreatic</b> and <b>splenic cysts</b>.',
      f'<b>Colonic diverticulosis</b>.',
  ]), bg=C['panel'])}
  {card('Cardiovascular & Cerebral', C['terracotta'], bullets([
      f'<b>Aneurysms of the cerebral arteries</b> → <b>subarachnoid hemorrhage</b>.',
      f'<b>Mitral valve prolapse</b>, <b>aortic valve abnormalities</b> and <b>aortic aneurysms</b>.',
  ]), bg=C['panel'])}
</div>
<div style="margin-top:13px;">
  {important('High-Yield', 'Cerebral (berry) aneurysms with subarachnoid hemorrhage are a life-threatening extra-renal feature of ADPKD.')}
</div>'''
body += content_close()
slides.append(body)

# ---------- 14. ADPKD complications ----------
body = header('Cystic Kidney Diseases · ADPKD', 'Complications')
body += content_open()
body += f'''<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;height:100%;">
  {card('Renal', C['terracotta'], bullets([
      f'Cyst infection',
      f'Renal tumor',
      f'Cyst rupture',
      f'Hematuria',
      f'Renal stones',
      f'Renal failure',
  ], size='13.5px'), bg=C['panel'])}
  {card('Vascular', C['olive'], bullets([
      f'Malignant hypertension.',
      f'Subarachnoid hemorrhage.',
  ], size='13.5px'), bg=C['panel'])}
  {card('Other', C['caramel'], bullets([
      f'Intractable pain',
      f'Liver failure (rare).',
  ], size='13.5px'), bg=C['panel'])}
</div>'''
body += content_close()
slides.append(body)

# ---------- 15. ADPKD diagnosis ----------
body = header('Cystic Kidney Diseases · ADPKD', 'Diagnosis')
body += content_open()
body += f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;height:100%;">
  {card('Clinical Clues', C['terracotta'], bullets([
      f'<b>Middle age</b>.',
      f'Positive <b>family history</b> of cystic kidney disease (in <b>75% of cases</b>).',
      f'Urine analysis may show <b>hematuria</b> and <b>mild proteinuria</b>.',
      f'<b>Slow and steady decline</b> in renal function.',
  ]), bg=C['panel'])}
  {card('Imaging', C['caramel'], bullets([
      f'<b>US:</b> <b>5 cysts</b> scattered in the <b>cortex and medulla</b> of each kidney.',
      f'<b>CT:</b> if US results are unclear.',
      f'<b>IVP:</b> <b>stretching and distortion</b> of the renal calyces.',
  ]), bg=C['panel'])}
</div>'''
body += content_close()
slides.append(body)

# ---------- 16. ADPKD treatment (1) ----------
body = header('Cystic Kidney Diseases · ADPKD', 'Treatment (1/2)')
body += content_open()
rows = [
    ('Control of hypertension',
     'Treated <b>aggressively</b>; <b>ACEIs and ARBs</b> should be used with <b>caution</b> in the presence of renal impairment especially in patients with <b>large cysts</b>. Diuretics should be used cautiously to avoid <b>hypokalemia</b> which is a factor in development of renal cyst?'),
    ('Renal infection: difficult to treat.',
     '<b>Parenteral antibiotics with cyst penetration</b> (e.g. <b>ciprofloxacin</b> and <b>trimethoprim-sulfamethoxazole</b>), for <b>2 weeks</b> followed by <b>long-term oral therapy (months)</b>.'),
    ('Pain',
     '<b>Bed rest</b> and <b>analgesics</b>. <b>Cyst decompression</b> may help.'),
]
body += data_table(['Problem', 'Management'], rows)
body += f'''<div style="margin-top:13px;">
  {caution('Caution', 'ACEIs/ARBs: use with caution in renal impairment (especially with large cysts). Diuretics: use cautiously — hypokalemia is a factor in the development of renal cyst?')}
</div>'''
body += content_close()
slides.append(body)

# ---------- 17. ADPKD treatment (2) ----------
body = header('Cystic Kidney Diseases · ADPKD', 'Treatment (2/2)')
body += content_open()
rows = [
    ('Hematuria',
     f'Usually <b>resolves within 7 days</b> with <b>bed rest and hydration</b>. {keyterm("Recurrent bleeding suggests underlying renal cell carcinoma")}.'),
    ('Renal stone',
     '<b>Good hydration</b> (2–3 L/day).'),
    ('Renal failure',
     f'As usual but <b>avoid peritoneal dialysis</b>.'),
]
body += data_table(['Problem', 'Management'], rows)
body += f'''<div style="margin-top:13px;">
  {important('Important', 'Recurrent bleeding → suspect <b>renal cell carcinoma</b>; renal failure → <b>avoid peritoneal dialysis</b>.')}
</div>'''
body += content_close()
slides.append(body)

# ---------- 18. DIVIDER Ch3 ARPKD ----------
slides.append(divider('03', 'Autosomal Recessive Polycystic Kidney Disease (ARPKD)',
    'Hereditary Polycystic Kidney Disease',
    'A rare autosomal recessive disorder with a defect on chromosome 6 — parents are not affected.'))

# ---------- 19. ARPKD incidence + symptoms overview ----------
body = header('Cystic Kidney Diseases · ARPKD', 'Incidence & Symptoms')
body += content_open()
body += f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;height:250px;">
  {card('Incidence', C['terracotta'], bullets([
      f'A rare <b>autosomal recessive (AR)</b> disorder with a defect on <b>chromosome 6</b>.',
      f'<b>Parents are not affected</b> and occurrence in sibling is <b>variable</b>.',
  ]), bg=C['panel'])}
  {card('When Does It Present?', C['caramel'], bullets([
      f'Presentation may be seen in the <b>perinatal period</b>, <b>early childhood</b> or <b>early adulthood</b>.',
      f'<b>Perinatal presentation:</b> high mortality due to <b>pulmonary hypoplasia</b>.',
  ]), bg=C['panel'])}
</div>
<div style="margin-top:13px;">
  {important('High-Yield', 'Perinatal presentation of ARPKD → <b>pulmonary hypoplasia</b> → high mortality.')}
</div>'''
body += content_close()
slides.append(body)

# ---------- 20. ARPKD symptoms detail + NB ----------
body = header('Cystic Kidney Diseases · ARPKD', 'Symptoms — Presentation by Age')
body += content_open()
body += f'''<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;height:310px;">
  {card('Perinatal Period', C['terracotta'], bullets([
      f'<b>High mortality</b> due to <b>pulmonary hypoplasia</b>.',
  ], size='13.5px'), bg=C['panel'])}
  {card('Early Life — Liver Dominant', C['olive'], bullets([
      f'Presentation dominated by features of <b>liver disease</b>.',
      f'<b>Hepatic cysts are uncommon</b>, but symptoms result from <b>hepatic fibrosis</b> and <b>portal hypertension</b> (i.e. <b>GI bleeding</b>, <b>hepato-splenomegaly</b> and <b>hypersplenism</b>).',
  ], size='13.5px'), bg=C['panel'])}
  {card('Increasing Age — Renal Prominent', C['caramel'], bullets([
      f'Symptoms of <b>renal involvement</b> become prominent; e.g. <b>abdominal mass</b>, <b>hypertension</b>, <b>recurrent UTIs</b>, and <b>renal failure in adolescence</b>.',
  ], size='13.5px'), bg=C['panel'])}
</div>
<div style="margin-top:10px;">
  {important('NB', 'ARPKD may be associated with <b>berry aneurysms</b>, <b>aortic aneurysms</b> and <b>Ehlers-Danlos syndrome</b>.')}
</div>'''
body += content_close()
slides.append(body)

# ---------- 21. ARPKD diagnosis ----------
body = header('Cystic Kidney Diseases · ARPKD', 'Diagnosis')
body += content_open()
body += f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;height:250px;">
  {card('Ultrasound — Test of Choice', C['caramel'], bullets([
      f'<b>Enlarged kidneys</b> of <b>smooth appearance</b> with <b>increased echogenicity</b>.',
      f'However, <b>normal US may not exclude</b> the diagnosis.',
  ]), bg=C['panel'])}
  {card('Confirmation', C['terracotta'], bullets([
      f'The diagnosis is confirmed by <b>absence of</b>:',
      f'&nbsp;&nbsp;• <b>Family history</b> (i.e. <b>normal US in parents</b>).',
      f'&nbsp;&nbsp;• <b>Liver cysts</b>.',
      f'&nbsp;&nbsp;• Other manifestations of ARPKD.',
  ]), bg=C['panel'])}
</div>
<div style="margin-top:13px;">
  {important('Key Point', 'Normal US of the parents helps confirm ARPKD — parents are carriers (autosomal recessive) and are not affected.')}
</div>'''
body += content_close()
slides.append(body)

# ---------- 22. ARPKD treatment ----------
body = header('Cystic Kidney Diseases · ARPKD', 'Treatment')
body += content_open()
body += f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;height:100%;">
  {card('Neonatal Presentation', C['terracotta'], bullets([
      f'<b>No good treatment</b>.',
  ]), bg=C['panel'])}
  {card('Childhood', C['olive'], bullets([
      f'<b>CKD</b> and <b>liver disease</b> are treated <b>as usual</b>.',
      f'<b>Hypertension</b> and <b>UTIs</b> are treated <b>aggressively</b>.',
  ]), bg=C['panel'])}
</div>'''
body += content_close()
slides.append(body)

# ---------- 23. DIVIDER Ch4 ----------
slides.append(divider('04', 'Hypertensive Nephrosclerosis',
    'Chronic Kidney Disease complicating Arterial Hypertension',
    'Clinical diagnosis in chronic hypertension — risk factors, criteria of diagnosis and management.'))

# ---------- 24. definition ----------
body = header('Hypertensive Nephrosclerosis', 'Definition')
body += content_open()
body += f'''{card('Definition', C['terracotta'], f'''<p style="font-size:17px;color:#3B2A1A;margin:0;line-height:1.5;">
  Generally, the term <b>hypertensive nephrosclerosis</b> is used for <b>chronic kidney disease</b> which <b>complicates arterial hypertension (AHT)</b>.
</p>''', bg=C['panel'], pad='18px 20px')}
<div style="margin-top:16px;">
  {important('Key Point', 'It is a diagnosis based on <b>clinical criteria</b>, not renal biopsy criteria.')}
</div>'''
body += content_close()
slides.append(body)

# ---------- 25. risk factors ----------
body = header('Hypertensive Nephrosclerosis', 'Risk Factors')
body += content_open()
body += f'''<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;height:100%;">
  {card('Demographic', C['terracotta'], bullets([
      f'<b>Age (&gt; 50 years)</b>',
      f'<b>Male gender</b>',
      f'<b>Low socioeconomic status</b>',
      f'<b>Family history</b> of hypertensive nephrosclerosis',
  ], size='13.5px'), bg=C['panel'])}
  {card('Lifestyle', C['olive'], bullets([
      f'<b>Cigarette smoking</b>',
  ], size='13.5px'), bg=C['panel'])}
  {card('Hypertension & Metabolic', C['caramel'], bullets([
      f'<b>Systolic hypertension</b> (persistently high)',
      f'<b>Dyslipidemia</b>',
      f'<b>Proteinuria</b>',
      f'<b>Decreased GFR</b>',
  ], size='13.5px'), bg=C['panel'])}
</div>'''
body += content_close()
slides.append(body)

# ---------- 26. diagnosis criteria ----------
body = header('Hypertensive Nephrosclerosis', 'Diagnosis — Clinical Criteria (Not Biopsy)')
body += content_open()
body += f'''<div style="background:#4A3118;border-radius:10px;padding:13px 18px;border-left:4px solid #C08A3E;box-shadow:0 1px 5px rgba(74,49,24,0.35);">
  <p style="font-size:14.5px;color:#FBF5E9;margin:0;line-height:1.5;">
    The diagnosis of hypertensive nephrosclerosis is generally based on <b style="color:#E8B84B;">clinical criteria</b> not renal biopsy criteria.
  </p>
</div>
<div style="margin-top:14px;">
{card('The 5 Clinical Criteria of Diagnosis', C['terracotta'], f'''<ol style="margin:0;padding-left:19px;font-size:14.5px;color:#3B2A1A;line-height:1.6;">
  <li>History of <b>prolonged hypertension (&gt; 10 years)</b>.</li>
  <li><b>Low grade proteinuria (&lt; 2 gm/day)</b>.</li>
  <li><b>Grade I or II hypertensive retinopathy</b>.</li>
  <li><b>Small scarred kidneys</b>.</li>
  <li><b>No evidence of primary renal disease</b>.</li>
</ol>''', bg=C['panel'], pad='14px 18px')}
</div>'''
body += content_close()
slides.append(body)

# ---------- 27. management: BP goal + salt ----------
body = header('Hypertensive Nephrosclerosis', 'Management — BP Goal & Salt Restriction')
body += content_open()
body += f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;height:245px;">
  {card('Intensive BP Goal', C['terracotta'], f'''<p style="font-size:16px;color:#3B2A1A;margin:0;line-height:1.45;">
    In patients with CKD, an intensive BP goal of <b style="color:#B0502A;font-size:19px;">&lt; 130/80 mmHg</b> has been recommended.
  </p>''', bg=C['panel'])}
  {card('Salt Restriction', C['olive'], bullets([
      f'A <b>low salt diet</b> is <b>critical</b> to achieve BP control while maintaining a simple BP medication regimen.',
      f'A <b>modest dietary sodium restriction</b> can <b>enhance the effects of antihypertensive medications</b>.',
  ]), bg=C['panel'])}
</div>
<div style="margin-top:13px;">
  {important('Important', 'Intensive BP control <b>&lt; 130/80 mmHg</b> is recommended in CKD patients.')}
</div>'''
body += content_close()
slides.append(body)

# ---------- 28. management: diuretics ----------
body = header('Hypertensive Nephrosclerosis', 'Management — Diuretics')
body += content_open()
body += f'''{card('Diuretics — Cornerstone in CKD', C['caramel'], bullets([
    f'<b>Diuretics are commonly used</b> and represent the <b>cornerstone</b> in the management of CKD patients.',
    f'In general, as <b>GFR falls</b>, <b>higher doses of diuretics</b> are needed to achieve a <b>natriuretic response</b>.',
]), bg=C['panel'], pad='16px 20px')}
<div style="margin-top:14px;">
  {important('Physiology Link', 'Falling GFR → higher diuretic doses required → the dose is titrated to achieve a natriuretic response.')}
</div>'''
body += content_close()
slides.append(body)

# ---------- 29. management: drugs (ACEI ARB CCB) ----------
body = header('Hypertensive Nephrosclerosis', 'Antihypertensive Drugs (1/2)')
body += content_open()
body += f'''<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;height:270px;">
  {card('1- ACEIs', C['terracotta'], bullets([
      f'<b>Angiotensin Converting Enzyme Inhibitors</b>',
  ], size='13.5px'), bg=C['panel'])}
  {card('2- ARBs', C['terracotta'], bullets([
      f'<b>Angiotensin Receptor Blockers</b>',
  ], size='13.5px'), bg=C['panel'])}
  {card('3- Calcium Channel Blockers (CCBs)', C['caramel'], bullets([
      f'<b>Non-dihydropyridine CCBs</b> consistently <b>reduce albuminuria</b> and <b>slow the decline in kidney function</b>.',
      f'<b>Dihydropyridine CCBs</b> should <b>not be used as monotherapy</b> in proteinuric CKD patients — always in <b>combination with a RAAS blocker</b>.',
  ], size='13px'), bg=C['panel'])}
</div>
<div style="margin-top:12px;">
  {caution('Caution', 'Dihydropyridine CCBs in proteinuric CKD → never as monotherapy; always combine with a <b>RAAS blocker</b> (ACEI or ARB).')}
</div>'''
body += content_close()
slides.append(body)

# ---------- 30. management: MRA + others ----------
body = header('Hypertensive Nephrosclerosis', 'Antihypertensive Drugs (2/2)')
body += content_open()
body += f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;height:250px;">
  {card('4- Mineralocorticoid (Aldosterone) Antagonists', C['terracotta'], bullets([
      f'Constitute an <b>important fourth-line BP agent</b> in the treatment of <b>resistant HTN</b> in later stages of CKD.',
      f'However, <b>risks of hyperkalemia and AKI</b> have <b>limited</b> mineralocorticoid antagonist use in <b>advanced CKD</b>.',
  ]), bg=C['panel'])}
  {card('5- Other Agents', C['olive'], bullets([
      f'Other agents are used when <b>treatment with the other agents have failed</b>.',
  ]), bg=C['panel'])}
</div>
<div style="margin-top:13px;">
  {important('Important', 'MRA use in advanced CKD is limited by the risks of <b>hyperkalemia</b> and <b>AKI</b>.')}
</div>'''
body += content_close()
slides.append(body)

# ---------- 31. summary ----------
body = header('Recap', 'Summary — Key Points')
body += content_open()
body += f'''<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;height:100%;">
  {card('Simple Renal Cysts', C['olive'], bullets([
      f'Common &gt; 50 y; <b>asymptomatic</b>; excellent prognosis.',
      f'US: echoes-free, thin smooth wall, enhanced back wall; CT: no enhancement.',
      f'Hematuria → suspect <b>RCC</b>.',
  ], size='13px'), bg=C['panel'])}
  {card('ADPKD', C['terracotta'], bullets([
      f'AD inheritance; chr 16 (ADPKD-1) &amp; chr 4 (ADPKD-2).',
      f'HTN in 50%, hepatic cysts in 50%, cerebral aneurysms → SAH.',
      f'Treatment: control BP; cyst-penetrating antibiotics; avoid peritoneal dialysis.',
  ], size='13px'), bg=C['panel'])}
  {card('ARPKD', C['caramel'], bullets([
      f'AR inheritance; chr 6; parents unaffected.',
      f'Perinatal → pulmonary hypoplasia; early life → hepatic fibrosis / portal HTN.',
      f'US is test of choice (enlarged echogenic kidneys).',
  ], size='13px'), bg=C['panel'])}
  {card('Hypertensive Nephrosclerosis', C['terracotta'], bullets([
      f'CKD complicating AHT; <b>clinical</b> diagnosis (5 criteria).',
      f'BP goal <b>&lt; 130/80</b>; low salt diet; diuretics cornerstone.',
      f'ACEI/ARB + CCB combination; MRA fourth-line (hyperkalemia/AKI risk).',
  ], size='13px'), bg=C['panel'])}
  {card('Management Principles', C['olive'], bullets([
      f'Intensive BP control; dose diuretics to GFR.',
      f'RAAS blockade central; avoid DHP-CCB monotherapy in proteinuric CKD.',
      f'Watch for hypokalemia, hyperkalemia, AKI.',
  ], size='13px'), bg=C['panel'])}
  {card('Exam Pearls', C['caramel'], bullets([
      f'Normal urine in ADPKD cyst infection — use blood cultures.',
      f'Recurrent hematuria → RCC; SAH → berry aneurysm.',
      f'CRF in ADPKD: avoid peritoneal dialysis.',
  ], size='13px'), bg=C['panel'])}
</div>'''
body += content_close()
slides.append(body)

# ---------- 32. closing ----------
body = f'''<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:linear-gradient(150deg,#EBD8B8 0%,#DEC399 55%,#D3B485 100%);"></div>
<svg style="position:absolute;top:-70px;right:-90px;width:520px;height:420px;z-index:1;" aria-hidden="true">
  <ellipse cx="260" cy="210" rx="230" ry="300" fill="#C08A3E" opacity="0.16"/>
</svg>
<svg style="position:absolute;bottom:-110px;left:-70px;width:420px;height:360px;z-index:1;" aria-hidden="true">
  <circle cx="210" cy="180" r="230" fill="#6E7A3E" opacity="0.10"/>
</svg>
<div style="position:absolute;top:0;left:0;width:14px;height:540px;background:#B0502A;"></div>
<div style="position:absolute;top:150px;left:72px;z-index:10;">
  <div style="width:84px;height:5px;background:#B0502A;margin-bottom:16px;border-radius:2px;"></div>
  <p style="font-size:44px;color:#3B2A1A;margin:0;font-weight:700;">Thank You</p>
  <p style="font-size:21px;color:#B0502A;margin:10px 0 0 0;font-weight:700;">Structural &amp; Vascular Renal Diseases</p>
  <div style="width:60px;height:4px;background:#C08A3E;margin:22px 0 16px 0;border-radius:2px;"></div>
  <p style="font-size:15px;color:#55361C;margin:0;line-height:1.6;">
    <b>References:</b><br>
    Principles of Nephrology — Dr. Hassan Abd-Elhady, Menoufia University<br>
    Cystic Kidney Diseases — Page 22-25 · Hypertensive Nephrosclerosis — Page 49-51
  </p>
</div>'''
slides.append(body)

# ---------- write files ----------
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'slides')
os.makedirs(out, exist_ok=True)
for i, body in enumerate(slides, 1):
    with open(os.path.join(out, f'slide-{i:02d}.html'), 'w') as f:
        f.write(slide_html(body, i))
print(f'Wrote {len(slides)} slides to {out}')
