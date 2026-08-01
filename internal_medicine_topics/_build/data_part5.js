// ============================================================
// Folder 05 — Structural & Vascular Renal Diseases
// Separate cards per common title
// ============================================================
const folderStructural = {
  label: "05 · Structural & Vascular Renal Diseases",
  children: [
    // ---------------- Topic 8 ----------------
    {
      label: "8. Cystic Kidney Diseases",
      children: [
        {
          label: "Simple (solitary) renal cysts",
          children: [
            {
              label: "Incidence",
              children: [
                { label: "Increases with age; ~30% >50 years, ~50% >70 years" },
                { label: "Usually solitary, unilateral, cortical" },
                { label: "Multiple cysts → consider PCKD or acquired cystic disease" }
              ]
            },
            {
              label: "Presentations",
              children: [
                { label: "Asymptomatic (most)" },
                { label: "Flank pain (large cyst or hemorrhage)" },
                { label: "Hematuria (cyst hemorrhage or infection)" },
                { label: "Incidental on imaging" }
              ]
            },
            {
              label: "Diagnosis",
              children: [
                { label: "US: well-defined anechoic lesion, thin wall, posterior acoustic enhancement" },
                { label: "CT: water density (0-20 HU), no enhancement" },
                { label: "Bosniak classification for complex cysts" }
              ]
            },
            {
              label: "Differential diagnosis",
              children: [
                { label: "PCKD (multiple bilateral cysts + family history)" },
                { label: "Acquired cystic kidney disease (CKD/dialysis, multiple small cysts)" },
                { label: "Renal cystic neoplasm (Bosniak III/IV)" },
                { label: "Multicystic dysplastic kidney (pediatric, non-functional)" }
              ]
            },
            {
              label: "Treatment",
              children: [
                { label: "Asymptomatic: no treatment, periodic US" },
                { label: "Symptomatic: percutaneous aspiration + sclerotherapy (ethanol)" },
                { label: "Infected: antibiotics + drainage" },
                { label: "Suspected neoplasm (Bosniak III/IV): partial or radical nephrectomy" }
              ]
            }
          ]
        },
        {
          label: "Autosomal Dominant PCKD (ADPKD)",
          children: [
            {
              label: "Incidence & genetics",
              children: [
                { label: "Incidence: 1:400-1:1000 live births" },
                { label: "PKD1 (chr 16, 85%): severe, earlier ESRD (~55 yrs)" },
                { label: "PKD2 (chr 4, 15%): milder, later ESRD (~75 yrs)" },
                { label: "Autosomal dominant, high penetrance, variable expressivity" }
              ]
            },
            {
              label: "Clinical features",
              children: [
                { label: "Flank/abdominal pain (cyst enlargement, hemorrhage, infection, stones)" },
                { label: "Hematuria (cyst rupture into collecting system)" },
                { label: "Hypertension (early, ~60-70%; renin-angiotensin activation by cyst compression)" },
                { label: "UTI (cyst infection, pyelonephritis)" },
                { label: "Renal stones (uric acid, calcium oxalate)" },
                { label: "Progressive renal enlargement → ESRD (median ~55 years PKD1)" },
                { label: "Extrarenal manifestations: hepatic cysts, intracranial aneurysms (berry), mitral valve prolapse, colonic diverticula, inguinal hernia" }
              ]
            },
            {
              label: "Associated abnormalities",
              children: [
                { label: "Hepatic cysts (most common extrarenal, increase with age)" },
                { label: "Intracranial berry aneurysms (~10-15%; screen if family history)" },
                { label: "Mitral valve prolapse (~25%)" },
                { label: "Colonic diverticula" },
                { label: "Inguinal hernia" }
              ]
            },
            {
              label: "Complications",
              children: [
                { label: "Cyst hemorrhage, infection, rupture" },
                { label: "Renal cell carcinoma (slightly ↑ risk)" },
                { label: "Subarachnoid hemorrhage (aneurysm rupture)" }
              ]
            },
            {
              label: "Diagnosis",
              children: [
                {
                  label: "Ultrasound criteria (Ravine / Pei)",
                  children: [
                    { label: "<30 yrs: ≥2 cysts (unilateral or bilateral)" },
                    { label: "30-59 yrs: ≥2 cysts in each kidney" },
                    { label: "≥60 yrs: ≥4 cysts in each kidney" }
                  ]
                },
                { label: "Genetic testing (PKD1/PKD2) for atypical or prenatal" }
              ]
            },
            {
              label: "Treatment",
              children: [
                { label: "BP control: ACEI/ARB first-line (target <130/80; <125/75 if proteinuria)" },
                { label: "Tolvaptan (V2 antagonist): slows cyst growth & eGFR decline in rapidly progressing adults" },
                { label: "Pain: analgesia, cyst aspiration/sclerotherapy, laparoscopic deroofing" },
                { label: "Hematuria: bed rest, hydration, avoid anticoagulants" },
                { label: "Cyst infection: lipophilic antibiotics (fluoroquinolones, TMP-SMX) penetrate cysts" },
                { label: "Stones: hydration, citrate, allopurinol (if uric acid)" },
                { label: "Intracranial aneurysms: screen high-risk; treat if >7mm or symptomatic" },
                { label: "RRT: dialysis & transplantation (excellent outcomes, no recurrence)" }
              ]
            }
          ]
        },
        {
          label: "Autosomal Recessive PCKD (ARPKD)",
          children: [
            {
              label: "Incidence & genetics",
              children: [
                { label: "Incidence: 1:20,000 live births" },
                { label: "PKHD1 (chr 6): fibrocystin / polyductin" },
                { label: "Autosomal recessive" }
              ]
            },
            {
              label: "Clinical features",
              children: [
                { label: "Neonatal: enlarged echogenic kidneys, oligohydramnios → pulmonary hypoplasia (Potter sequence)" },
                { label: "Infantile/childhood: hypertension, CKD, portal hypertension (congenital hepatic fibrosis)" },
                { label: "Hepatic: congenital hepatic fibrosis → portal hypertension, esophageal varices, hypersplenism" },
                { label: "Renal: progressive CKD → ESRD in childhood/adolescence" }
              ]
            },
            {
              label: "Diagnosis",
              children: [
                { label: "US: bilaterally enlarged echogenic kidneys with loss of corticomedullary differentiation; microcysts (1-3mm) radially arranged" },
                { label: "Liver US: hepatomegaly, increased echogenicity, portal hypertension signs" },
                { label: "Genetic testing (PKHD1)" }
              ]
            },
            {
              label: "Treatment",
              children: [
                { label: "Supportive: BP control, nutritional support, growth hormone" },
                { label: "Portal hypertension: β-blockers, endoscopic variceal ligation, shunt/transplant" },
                { label: "RRT: dialysis & combined liver-kidney transplant for hepatic + renal failure" }
              ]
            }
          ]
        }
      ]
    },
    // ---------------- Topic 13 ----------------
    {
      label: "13. Hypertensive Nephrosclerosis",
      children: [
        {
          label: "Definition",
          children: [
            { label: "Chronic renal damage from long-standing essential hypertension" },
            { label: "Arteriolosclerosis (hyaline in benign; hyperplastic in malignant) → ischemic nephron loss → fibrosis" }
          ]
        },
        {
          label: "Risk factors",
          children: [
            { label: "Long-standing, poorly controlled hypertension" },
            { label: "African ancestry" },
            { label: "Age >50 years" },
            { label: "Smoking, dyslipidemia, diabetes" },
            { label: "Family history of hypertension/ESRD" }
          ]
        },
        {
          label: "Diagnosis",
          children: [
            { label: "Clinical: long-standing HTN + slowly progressive CKD + benign urinary sediment (no hematuria/casts)" },
            { label: "US: small, symmetrically shrunken kidneys; thinned cortex" },
            { label: "Exclusion: no primary glomerular disease (biopsy if uncertain)" }
          ]
        },
        {
          label: "Management",
          children: [
            {
              label: "BP goal & salt restriction",
              children: [
                { label: "Target <130/80 (no proteinuria); <125/75 (with proteinuria)" },
                { label: "Salt <2 g/day" }
              ]
            },
            {
              label: "Diuretics",
              children: [
                { label: "Thiazide (early CKD, eGFR >30)" },
                { label: "Loop diuretic (eGFR <30 or volume overload)" }
              ]
            },
            {
              label: "Antihypertensive drugs",
              children: [
                { label: "ACEI/ARB: reno-protective, reduce intraglomerular pressure (cautious if bilateral RAS)" },
                { label: "CCB: non-dihydropyridine (verapamil, diltiazem) have additional reno-protective effect" },
                { label: "β-blockers" },
                { label: "Alpha-blockers, central agents as add-on" }
              ]
            }
          ]
        }
      ]
    }
  ]
};