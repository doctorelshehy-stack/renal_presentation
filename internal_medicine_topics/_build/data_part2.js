// ============================================================
// Folder 02 — Acute Kidney Injury
// Separate cards per common title
// ============================================================
const folderAKI = {
  label: "02 · Acute Kidney Injury",
  children: [
    // ---------------- Topic 9 ----------------
    {
      label: "9. Acute Kidney Injury",
      children: [
        {
          label: "Definition",
          children: [
            { label: "Abrupt (within 48 hours) and sustained decrease in kidney function" },
            { label: "Accompanied by changes in blood biochemistry (e.g. rise in serum creatinine), urine output, or both" },
            { label: "AKI encompasses the whole spectrum: mild transient creatinine rise → overt renal failure requiring RRT" },
            { label: "Term AKI more precise than acute renal failure" }
          ]
        },
        {
          label: "Classification (RIFLE & AKIN)",
          children: [
            { label: "Risk (RIFLE) / Stage 1 (AKIN): serum creatinine ≥1.5-2× baseline, or ↑≥0.3; urine output <0.5 ml/kg/h for 6 hours" },
            { label: "Injury (RIFLE) / Stage 2 (AKIN): serum creatinine ≥2× baseline; urine output <0.5 ml/kg/h for 12 hours" },
            { label: "Failure (RIFLE) / Stage 3 (AKIN): serum creatinine ≥3×, or ≥4.0 with rise ≥0.5; urine output <0.3 ml/kg/h for 24 hours or anuria for 12 hours" },
            { label: "Loss (RIFLE): persistent loss of renal function >4 weeks" },
            { label: "ESRD (RIFLE): permanent loss of renal function >3 months" }
          ]
        },
        {
          label: "Causes",
          children: [
            {
              label: "Pre-renal",
              children: [
                {
                  label: "Decreased effective extracellular volume",
                  children: [
                    { label: "Fluid loss: hemorrhage, vomiting, diarrhea, burns, diuretics" },
                    { label: "Redistribution: liver cell failure, nephrotic syndrome, intestinal obstruction, pancreatitis, malnutrition" }
                  ]
                },
                {
                  label: "Decreased cardiac output",
                  children: [
                    { label: "Cardiogenic shock, valvulopathy, myocarditis, MI, arrhythmias, CHF, pulmonary emboli, cardiac tamponade" }
                  ]
                },
                {
                  label: "Peripheral vasodilatation",
                  children: [
                    { label: "Hypotension, sepsis, hypoxemia, anaphylactic shock" }
                  ]
                },
                {
                  label: "Renal vasoconstriction",
                  children: [
                    { label: "Prostaglandin inhibition, adrenergics, sepsis, hepato-renal syndrome, hypercalcemia" }
                  ]
                },
                {
                  label: "Efferent arteriole vasodilatation",
                  children: [
                    { label: "ACEIs & ARBs → decreased intraglomerular pressure and renal blood flow → renal ischemia" }
                  ]
                }
              ]
            },
            {
              label: "Intra-renal (intrinsic)",
              children: [
                {
                  label: "Acute tubular necrosis (ATN)",
                  children: [
                    {
                      label: "Hemodynamic",
                      children: [
                        { label: "Cardiovascular surgery, sepsis, prolonged pre-renal cause" }
                      ]
                    },
                    {
                      label: "Toxic",
                      children: [
                        { label: "Antimicrobials, iodide contrast agents, immunosuppression or antineoplastic agents, organic solvents, heavy metals, radiation" }
                      ]
                    },
                    {
                      label: "Intratubular deposits",
                      children: [
                        { label: "Acute uric acid nephropathy, myeloma, severe hypercalcemia, primary oxalosis, sulfadiazine" }
                      ]
                    },
                    {
                      label: "Organic pigments (endogenous nephrotoxins)",
                      children: [
                        { label: "Myoglobin (rhabdomyolysis), hemoglobinuria (intravascular hemolysis)" }
                      ]
                    }
                  ]
                },
                { label: "Acute GN e.g. RPGN" },
                { label: "Acute interstitial nephritis" },
                { label: "Renal vascular occlusion" }
              ]
            },
            {
              label: "Post-renal",
              children: [
                { label: "Congenital anomalies: ureterocele, bladder diverticulosis, post-urethral valves, neurogenic bladder" },
                { label: "Acquired uropathies: BPH, ureterolithiasis, papillary necrosis, ureteral ligation" },
                { label: "Malignant disease: prostate, bladder, cervix, colon" },
                { label: "Gynecologic non-neoplastic: uterine prolapse, endometriosis" },
                { label: "Drugs: sulfonamides, aminocaproic acid" },
                { label: "Infections: schistosomiasis, TB, candidiasis, aspergillosis, actinomycosis" },
                { label: "Others: accidental urethral catheter occlusion" }
              ]
            },
            { label: "NB: nearly all cases of ICU-associated AKI result from more than a single insult" }
          ]
        },
        {
          label: "Clinical manifestations",
          children: [
            {
              label: "Oliguria / anuria",
              children: [
                { label: "Oliguria: <300 ml/day, <5 ml/kg/day or 0.5 ml/kg/h" },
                { label: "Oliguria significantly associated with AKI; oliguria alone is the best predictor" },
                { label: "~50% or more of AKI cases are non-oliguric → normal urine output does not assure normal GFR" },
                {
                  label: "Causes of anuric AKI",
                  children: [
                    { label: "Complete UT obstruction (90% of cases)" },
                    {
                      label: "Renal vascular occlusion",
                      children: [
                        { label: "Renal artery thrombosis" },
                        { label: "Renal vein thrombosis" },
                        { label: "Cortical necrosis: sepsis, obstetric accidents, DIC" },
                        { label: "Renal vasculitis and RPGN" }
                      ]
                    },
                    { label: "AKI complicating: sepsis, heat stroke, rhabdomyolysis" }
                  ]
                }
              ]
            },
            {
              label: "Manifestations of loss of kidney function",
              children: [
                { label: "Volume overload: peripheral edema, weight gain, shortness of breath" },
                { label: "GIT symptoms: anorexia, nausea, vomiting, diarrhea" },
                { label: "Flank/back pain (edematous kidneys or UT obstruction)" },
                { label: "Altered mental status or seizures" },
                { label: "Anemia and bleeding" },
                { label: "Other symptoms" }
              ]
            }
          ]
        },
        {
          label: "Investigations",
          children: [
            {
              label: "Urine examination",
              children: [
                { label: "Urine volume / 24 h" },
                { label: "Color: reddish-brown or cola → myoglobin or Hb (positive dipstick with no red cells on microscopy)" },
                {
                  label: "Red blood cells",
                  children: [
                    { label: "Eumorphic → bleeding along the collecting system" },
                    { label: "Dysmorphic or red cell casts → GN" }
                  ]
                },
                {
                  label: "Urinary casts",
                  children: [
                    { label: "Muddy brown casts → ATN (tubular cell casts & oxalate crystals support)" },
                    { label: "WBC casts/cells → pyelonephritis or acute interstitial nephritis (urine eosinophils help confirm AIN)" }
                  ]
                },
                { label: "Proteinuria" }
              ]
            },
            {
              label: "Fractional excretion of sodium (FENa)",
              children: [
                { label: "FENa = (UNa/PNa) / (Ucr/Pcr) × 100" },
                { label: "<1% → pre-renal AKI" },
                { label: ">1% → ATN" },
                { label: "Exceptions (ATN with low FENa): radio-contrast, severe burns, acute GN, rhabdomyolysis" },
                { label: "Valuable in hepato-renal syndrome (extreme renal avidity for Na)" },
                { label: "Useful only in oliguria; NOT in: non-oliguric states, GN, patients receiving diuretics, liver cirrhosis" }
              ]
            },
            {
              label: "Fractional excretion of urea (FEurea)",
              children: [
                { label: "FEurea = (Uur/Pur) / (Ucr/Pcr) × 100" },
                { label: "Used in patients receiving diuretics (urea transport not affected by diuretics)" },
                { label: "Levels <35% suggestive of pre-renal state" }
              ]
            },
            {
              label: "Blood examination & serology",
              children: [
                { label: "Serum creatinine and blood urea" },
                { label: "Serum creatinine better surrogate for GFR than BUN" },
                {
                  label: "BUN/creatinine ratio",
                  children: [
                    { label: "20:1 → pre-renal AKI" },
                    { label: "<20:1 → intrinsic or post-renal AKI" }
                  ]
                },
                { label: "Increased serum uric acid → tumor lysis syndrome" },
                { label: "Increased serum LDH → renal infarction" },
                { label: "Schistocytes in blood film → HUS or TTP" },
                { label: "Increased rouleaux formation → multiple myeloma" },
                { label: "Myoglobin or free Hb → pigment nephropathy" },
                { label: "Serology: complement levels, ANA, ANCA, anti-GBM Ab, HBV & HCV, ASOT" }
              ]
            },
            {
              label: "Bladder pressure (intra-abdominal)",
              children: [
                { label: "<10 mmHg → normal" },
                { label: ">10 mmHg → abnormal" },
                { label: "15-25 mmHg → risk of abdominal compartment syndrome and AKI" }
              ]
            },
            {
              label: "Ultrasound & Doppler",
              children: [
                { label: "US: evaluates existing renal disease & obstruction; small kidney → suggests CKD" },
                { label: "Doppler: reduced flow in pre-renal & renal AKI (little diagnostic value there)" },
                { label: "Doppler useful in thrombo-embolic or renal vascular disease" }
              ]
            },
            {
              label: "Renal biopsy",
              children: [
                { label: "Indicated if cause of intrinsic renal AKI unclear after excluding pre- and post-renal causes" }
              ]
            },
            {
              label: "Biomarkers",
              children: [
                { label: "Serum creatinine and eGFR" }
              ]
            }
          ]
        },
        {
          label: "Treatment (principles)",
          children: [
            { label: "No definitive therapy; supportive care is the mainstay regardless of etiology" },
            {
              label: "First — recognize etiology & risk factors",
              children: [
                { label: "DM, CKD, hypertension, cardiac or liver dysfunction → evaluate and manage" }
              ]
            },
            {
              label: "Second — monitoring",
              children: [
                { label: "Monitor serum creatinine and urine output for staging" }
              ]
            },
            {
              label: "Third — manage comorbidities",
              children: [
                { label: "Tight glucose control with intensive insulin therapy" },
                { label: "Control of hyperkalemia" },
                { label: "Balance nephrotoxic drugs & planned procedures against potential benefits" },
                { label: "Maintain renal perfusion: volume resuscitation, inotropic or vasopressor support" },
                {
                  label: "Small-dose dopamine (1-3 mcg/kg/min)",
                  children: [
                    { label: "Selective dilatation of renal vasculature, enhances renal perfusion" },
                    { label: "Reduces sodium absorption → enhances urine flow → prevents tubular cast obstruction" },
                    { label: "Controversial decision in treating AKI" }
                  ]
                }
              ]
            },
            {
              label: "Fourth — renal replacement therapy",
              children: [
                { label: "No current consensus on indications; RRT itself may introduce complications" },
                {
                  label: "Absolute indications for dialysis in AKI",
                  children: [
                    { label: "Clinically apparent signs & symptoms of uremia" },
                    { label: "Management of refractory hyperkalemia, acidosis, and hypervolemia" }
                  ]
                },
                { label: "Many nephrologists initiate dialysis empirically for BUN >100 mg/dl" }
              ]
            }
          ]
        }
      ]
    },
    // ---------------- Topic 10 ----------------
    {
      label: "10. AKI in Special Situations",
      children: [
        {
          label: "Situations",
          children: [
            { label: "1. Contrast-induced nephropathy (CIN)" },
            { label: "2. Tumor lysis syndrome (TLS)" },
            { label: "3. AKI in pregnancy" },
            { label: "4. AKI in rhabdomyolysis" }
          ]
        },
        {
          label: "Contrast-induced nephropathy (CIN)",
          children: [
            {
              label: "Definition",
              children: [
                { label: "Rise of serum creatinine ≥0.5 mg/dl or 25% above baseline within 48 hours after contrast administration" }
              ]
            },
            {
              label: "Risk factors",
              children: [
                {
                  label: "Patient-related",
                  children: [
                    { label: "Pre-existing CKD — most potent risk factor; ~60% of CIN patients have CKD; incidence parallels severity of pre-existing renal impairment" },
                    { label: "Diabetes mellitus" },
                    { label: "Congestive heart failure" },
                    { label: "Hypotension" },
                    { label: "Volume depletion" },
                    { label: "Old age" }
                  ]
                },
                {
                  label: "Contrast-related",
                  children: [
                    { label: "Large volume (dose) of parenteral contrast material" },
                    { label: "Type of contrast (osmolarity): high osmolar contrast → higher incidence of CIN" }
                  ]
                }
              ]
            },
            {
              label: "Pathogenesis",
              children: [
                {
                  label: "Renal ischemia",
                  children: [
                    { label: "Production of vasoconstrictive compounds: endothelin, adenosine" },
                    { label: "Increased oxygen utilization in renal tubules" }
                  ]
                },
                {
                  label: "Hyperosmolarity (intra-tubular)",
                  children: [
                    { label: "↑intra-tubular hydrostatic pressure → ↓glomerular filtration" },
                    { label: "↑tubular cell apoptosis" }
                  ]
                },
                { label: "Generation of oxygen free radicals" },
                { label: "Direct cellular toxicity" }
              ]
            },
            {
              label: "Diagnosis",
              children: [
                { label: "Vast majority: no symptoms or signs" },
                { label: "Smaller subset: oliguria ± volume overload" },
                { label: "Rarely: symptoms & signs of uremia" },
                {
                  label: "Laboratory (serum creatinine)",
                  children: [
                    { label: "Begins to rise 24-48 h after exposure" },
                    { label: "Peaks within 3-5 days" },
                    { label: "Returns to baseline within 7-10 days" },
                    { label: "Severe cases: peaks 5-10 days, may have oliguria & require dialysis" }
                  ]
                },
                { label: "Imaging: to exclude other causes of AKI" }
              ]
            },
            {
              label: "Management",
              children: [
                {
                  label: "Prevention",
                  children: [
                    { label: "Use non-iodinated contrast media" },
                    { label: "Use low osmolar contrast media" },
                    { label: "Minimize contrast volume: formula = 5 ml contrast/kg body weight (max 300 ml) / serum creatinine (mg/dl)" },
                    { label: "Space between contrast administrations" },
                    { label: "Avoid nephrotoxic drugs before and after the procedure" },
                    { label: "Adequate hydration before, during, and after the procedure" },
                    { label: "N-acetyl cysteine: unclear benefit (conflicting studies)" }
                  ]
                },
                {
                  label: "Treatment (no specific therapy)",
                  children: [
                    { label: "Manage fluid and electrolytes" },
                    { label: "Adjust medications eliminated by the kidney" },
                    { label: "Regular monitoring of electrolytes, creatinine, BUN" },
                    { label: "Dialysis as needed" }
                  ]
                }
              ]
            },
            {
              label: "Prognosis",
              children: [
                { label: "Most patients: complete recovery of renal function" },
                { label: "Small minority: may progress to CKD" }
              ]
            }
          ]
        },
        {
          label: "Tumor lysis syndrome (TLS)",
          children: [
            {
              label: "Definition",
              children: [
                { label: "Acute critical illness: severe hyperuricemia, hyperphosphatemia, hyperkalemia, hypocalcemia, and AKI" },
                { label: "Seen in rapidly growing cancers (especially Burkitt's lymphoma) after chemotherapy" },
                { label: "Electrolyte disorders from massive sudden tumor cell death → release of uric acid, phosphorus, potassium" },
                { label: "Hypocalcemia secondary to hyperphosphatemia (maintains calcium-phosphorus balance)" }
              ]
            },
            {
              label: "Patients at risk",
              children: [
                { label: "Hematological & lymphoproliferative malignancy with marked elevation of serum LDH" },
                { label: "Volume depletion" },
                { label: "Acidic urinary pH" },
                { label: "Patients with CKD (renal clearance is primary excretion mechanism of uric acid & phosphates)" }
              ]
            },
            {
              label: "Clinical features",
              children: [
                { label: "Varying degrees of AKI" },
                { label: "Intra-tubular precipitation of uric acid (acute UA nephropathy)" },
                { label: "Acute nephrocalcinosis secondary to marked hyperphosphatemia" },
                { label: "AKI most marked during induction of chemotherapy" }
              ]
            },
            {
              label: "Diagnosis",
              children: [
                { label: "Known/suspected malignancy (especially Burkitt's lymphoma) + AKI + hyperuricemia + elevated LDH" },
                { label: "Concomitant volume depletion, hyperkalemia, hyperphosphatemia & hypocalcemia strongly support diagnosis" }
              ]
            },
            {
              label: "Differential diagnosis (AKI in cancer patients)",
              children: [
                { label: "UT obstruction" },
                { label: "Severe volume depletion" },
                {
                  label: "Parenchymal renal diseases",
                  children: [
                    { label: "GN secondary to cryoglobulinemia or tumor-related Ag-Ab complexes" },
                    { label: "Vasculitis" },
                    { label: "Hypercalcemic nephropathy" },
                    { label: "Tumor infiltrating the kidney parenchyma" },
                    { label: "Myeloma kidney (cast nephropathy)" },
                    { label: "Nephrotoxic drugs: methotrexate, cisplatinum, mitomycin C, INF-alpha, antibiotics" }
                  ]
                }
              ]
            },
            {
              label: "Prevention (prophylactic)",
              children: [
                { label: "Early identification of patients at risk" },
                {
                  label: "Before anti-neoplastic drug therapy",
                  children: [
                    { label: "Correct initial electrolyte and fluid disorders" },
                    { label: "Maintain adequate hydration and urine output" },
                    { label: "Alkalinize urine to pH >7.0 (enhances UA solubility, prevents precipitation)" },
                    { label: "Oral phosphate-binding antacids" },
                    { label: "Allopurinol 300 mg/m2, 1-2 days before chemotherapy" },
                    { label: "Correct any renal or pre-renal dysfunction" }
                  ]
                }
              ]
            },
            {
              label: "Treatment of established AKI",
              children: [
                { label: "Allopurinol 600 mg/day" },
                { label: "IV isotonic NaHCO3 at 200-300 ml/h: expand volume, wash out renal medulla, alkalinize urine" },
                {
                  label: "Dialysis (HD life-saving; consider for every patient; generally required during induction)",
                  children: [
                    { label: "Decrease plasma levels of uric acid, phosphorus, potassium" },
                    { label: "Restore volume overload" },
                    { label: "Control uremia" }
                  ]
                },
                {
                  label: "Post-chemotherapy measures",
                  children: [
                    { label: "Discontinue urine alkalinization once UA homeostasis achieved (avoid Ca3PO4 precipitation)" },
                    { label: "Treat symptomatic hypocalcemia after correction of hyperphosphatemia" }
                  ]
                }
              ]
            }
          ]
        },
        {
          label: "Rhabdomyolysis",
          children: [
            {
              label: "Definition",
              children: [
                { label: "Injury or metabolic defect in skeletal muscle cell → lysis of cell membrane" },
                { label: "Leakage of contents (myoglobin, enzymes, phosphorus, potassium) into blood" }
              ]
            },
            {
              label: "Causes",
              children: [
                {
                  label: "Direct trauma",
                  children: [
                    { label: "Crush syndrome" },
                    { label: "Electrical shock" },
                    { label: "Prolonged pressure with coma" },
                    { label: "Thermal burns & freezing" }
                  ]
                },
                {
                  label: "Excessive exercise",
                  children: [
                    { label: "Athletic injury" },
                    { label: "Convulsive seizures" }
                  ]
                },
                {
                  label: "Hereditary myopathies",
                  children: [
                    { label: "Myophosphorylase deficiency (McArdle's disease)" }
                  ]
                },
                {
                  label: "Acquired metabolic disorders",
                  children: [
                    { label: "Hyperthyroidism" },
                    { label: "Hypokalemia (acute)" },
                    { label: "Diabetic ketoacidosis" },
                    { label: "Hypophosphatemia (acute)" },
                    { label: "Alcoholism" },
                    { label: "Hyponatremia (acute)" }
                  ]
                },
                {
                  label: "Hypoxia and ischemia",
                  children: [
                    { label: "Carbon monoxide poisoning" },
                    { label: "Vascular occlusion" },
                    { label: "Atheromatous embolism" },
                    { label: "Compartment syndrome" }
                  ]
                },
                {
                  label: "Drugs",
                  children: [
                    { label: "Statins & lipid-lowering drugs" },
                    { label: "Cocaine" },
                    { label: "Amphetamine derivatives" }
                  ]
                },
                {
                  label: "Infectious diseases",
                  children: [
                    { label: "Viral: Coxsackie, HIV, influenza" },
                    { label: "Bacterial: Clostridia, Legionella, streptococcal, staphylococcal, pneumococcal pneumonia" }
                  ]
                },
                {
                  label: "Toxins",
                  children: [
                    { label: "Snake venom, poisonous mushrooms, fish poisoning (Haff disease)" }
                  ]
                },
                {
                  label: "Miscellaneous",
                  children: [
                    { label: "Malignant hyperthermia, neuroleptic malignant syndrome" }
                  ]
                }
              ]
            },
            {
              label: "Pathogenesis",
              children: [
                { label: "Mild/moderate (intense exertion, violent repetitive activity, grand mal seizure): direct muscle injury + energy store depletion → muscle pain & weakness" },
                {
                  label: "Severe acute (crush injury / pigmented nephropathy) — AKI due to",
                  children: [
                    {
                      label: "Renal ischemia",
                      children: [
                        { label: "Myoglobin has intense vasoconstrictive effect" }
                      ]
                    },
                    {
                      label: "Tubular obstruction and injury",
                      children: [
                        { label: "Filtered myoglobin enters PCT cells → releases elemental iron & iron compounds → toxic products injure cells" },
                        { label: "Unabsorbed pigment passes to distal nephron, interacts with Tamm-Horsfall protein (in acidic urine) → gel obstructs urine flow" },
                        { label: "Tubular pigment concentration rises → augments proximal tubular absorption & toxicity" }
                      ]
                    }
                  ]
                }
              ]
            },
            {
              label: "Diagnosis",
              children: [
                {
                  label: "Clinical features (depend on severity)",
                  children: [
                    { label: "Mild/moderate: muscular pain, tenderness, edema, stiffness, weakness, impaired mobility" },
                    { label: "Severe acute (crush injury): AKI" }
                  ]
                },
                {
                  label: "Laboratory",
                  children: [
                    { label: "Total serum CK >500 IU/L → high suspicion of acute rhabdomyolysis" },
                    { label: "CK-MM isoform → most sensitive test to confirm diagnosis" }
                  ]
                }
              ]
            },
            {
              label: "Treatment (severe cases in ICU)",
              children: [
                { label: "Aggressive & urgent volume replacement to maintain organ perfusion (avoid volume overload & pulmonary edema)" },
                { label: "Alkalinization of urine with bicarbonate infusion (prevent obstructive cast formation)" },
                { label: "Special care for respiratory failure due to diaphragmatic weakness if severe" },
                { label: "Monitor hyperkalemia by ECG and serum potassium" },
                { label: "Dialysis for severe AKI" }
              ]
            },
            {
              label: "Prognosis",
              children: [
                { label: "Survivors at risk of permanent disability (muscle fibrosis)" }
              ]
            }
          ]
        }
      ]
    }
  ]
};
