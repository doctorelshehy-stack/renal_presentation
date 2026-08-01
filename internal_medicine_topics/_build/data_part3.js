// ============================================================
// Folder 03 — Chronic Kidney Disease & RRT
// Separate cards per common title
// ============================================================
const folderCKD = {
  label: "03 · Chronic Kidney Disease & RRT",
  children: [
    // ---------------- Topic 11 ----------------
    {
      label: "11. Chronic Kidney Disease",
      children: [
        {
          label: "Definitions",
          children: [
            { label: "CKD: abnormalities of kidney structure or function present >3 months with health implications; classified by cause, GFR category & albuminuria category" },
            { label: "Chronic renal failure (CRF): GFR <60 ml/min for ≥3 months (Grade 3 CKD)" },
            { label: "ESRD: permanent & irreversible renal impairment requiring renal replacement therapy (= Grade 5 CKD)" }
          ]
        },
        {
          label: "Markers of kidney damage",
          children: [
            {
              label: "Functional",
              children: [
                { label: "Albuminuria: AER ≥30 mg/24h or ACR ≥30 mg/g" },
                { label: "Urine sediment abnormalities" },
                { label: "Electrolyte and other abnormalities due to tubular disorders" }
              ]
            },
            {
              label: "Structural",
              children: [
                { label: "Structural abnormalities detected by histology" },
                { label: "Structural abnormalities detected by imaging" },
                { label: "History of kidney transplantation" }
              ]
            }
          ]
        },
        {
          label: "Grades (GFR categories)",
          children: [
            { label: "G1: ≥90 — normal or high" },
            { label: "G2: 60-89 — mildly decreased (relative to young adult level)" },
            { label: "G3a: 45-59 — mildly to moderately decreased" },
            { label: "G3b: 30-44 — moderately to severely decreased" },
            { label: "G4: 15-29 — severely decreased" },
            { label: "G5: <15 — ESRD" },
            { label: "NB: without evidence of kidney damage, G1 & G2 do NOT fulfill criteria for CKD" }
          ]
        },
        {
          label: "Grades (albuminuria categories)",
          children: [
            { label: "A1: AER <30 mg/24h, ACR <30 mg/g — normal to mildly increased" },
            { label: "A2: AER 30-300, ACR 30-300 — moderately increased" },
            { label: "A3: AER >300, ACR >300 — severely increased (nephrotic syndrome usually AER >2200 mg/24h & ACR >2200 mg/g)" }
          ]
        },
        {
          label: "Causes",
          children: [
            { label: "Diabetes mellitus" },
            { label: "Hypertension" },
            { label: "Glomerulopathies (primary or secondary)" },
            { label: "Tubulo-interstitial diseases" },
            { label: "Renal vascular diseases (renal artery stenosis)" },
            { label: "Hereditary renal diseases: PCKD, Alport's syndrome, oxalosis" },
            { label: "Obstructive uropathy: urolithiasis, prostatic enlargement, tumors, retroperitoneal fibrosis" },
            { label: "Recurrent UTI: pyelonephritis, vesicoureteral reflux" },
            { label: "Drugs & toxins: NSAID, chronic lead poisoning" },
            { label: "Uncertain (up to 15% of cases)" }
          ]
        },
        {
          label: "Clinical features & complications",
          children: [
            { label: "Grades 1-3 usually asymptomatic; grades 4 & 5 symptomatic" },
            {
              label: "Gastrointestinal",
              children: [
                { label: "Anorexia, nausea, vomiting, hiccough" },
                { label: "Uremic fetor" },
                { label: "Mucosal ulcerations → GIT bleeding" },
                { label: "Peptic ulcer" },
                { label: "Diverticulosis ↑ (PCKD)" },
                { label: "NB: GIT symptoms improve with dialysis except peptic ulcer & diverticulosis" }
              ]
            },
            {
              label: "Cardiovascular",
              children: [
                { label: "CHF & pulmonary edema" },
                { label: "Arrhythmias" },
                { label: "Hypertension (absence in CKD → salt wasting PCKD, drug effect, volume depletion)" },
                { label: "Pericarditis & pericardial effusion" },
                { label: "Accelerated atherosclerosis" }
              ]
            },
            {
              label: "Respiratory",
              children: [
                { label: "Acidotic breathing, pleurisy, chest infection" }
              ]
            },
            {
              label: "Hematological",
              children: [
                {
                  label: "Anemia",
                  children: [
                    { label: "Decreased EPO production" },
                    { label: "Decreased RBC lifespan" },
                    { label: "Decreased nutrients" },
                    { label: "Bleeding" },
                    { label: "Secondary HPT" },
                    { label: "Inflammatory inhibition" },
                    { label: "Blood loss" }
                  ]
                },
                { label: "Bleeding diathesis: bleeding time, factor III, platelets, prothrombin" },
                { label: "Infection susceptibility: leukocyte dysfunction, mucosal barriers, steroids" }
              ]
            },
            {
              label: "Endocrine & metabolism",
              children: [
                { label: "Insulin resistance" },
                { label: "↓insulin requirement" },
                { label: "Thyroid: ↑TRH → ↑prolactin (galactorrhea, amenorrhea, impotence)" },
                { label: "Hypocalcemia → secondary HPT" },
                { label: "↓testosterone (impotence, infertility)" },
                { label: "Menstrual abnormalities" }
              ]
            },
            {
              label: "Bone (CKD-MBD)",
              children: [
                {
                  label: "Definition: systemic disorder of mineral & bone metabolism due to CKD (Ca/P/PTH/vit D; bone turnover/mineralization; vascular/soft tissue calcification incl. calciphylaxis)"
                },
                {
                  label: "Pathophysiology",
                  children: [
                    { label: "↓P filtration → hyperphosphatemia → ↑PTH secretion" },
                    { label: "↓1α-hydroxylase → ↓calcitriol → ↓Ca absorption → hypocalcemia → SHPT" },
                    { label: "Flow: hyperphosphatemia → ↓calcitriol → hypocalcemia → SHPT → bone disease → vascular calcification → CV mortality" }
                  ]
                },
                {
                  label: "Renal osteodystrophy",
                  children: [
                    { label: "Definition: bone pain, pathological fractures, imaging/biopsy changes" },
                    { label: "Osteitis fibrosa (high turnover)" },
                    { label: "Osteomalacia (low turnover)" },
                    { label: "Adynamic bone disease (↓formation, normal mineralization; aggressive PTH suppression)" },
                    { label: "Osteopenia / osteoporosis" },
                    { label: "Mixed lesions (high PTH + impaired formation; aluminum-related)" },
                    { label: "Spectrum: low turnover (adynamic) ↔ high turnover (osteitis fibrosa)" }
                  ]
                }
              ]
            },
            {
              label: "Neurological",
              children: [
                {
                  label: "CNS — early",
                  children: [
                    { label: "Concentration & memory impairment, drowsiness, insomnia, hiccups, cramps, twitching" }
                  ]
                },
                {
                  label: "CNS — late",
                  children: [
                    { label: "Asterixis, myoclonus, chorea, stupor, seizures, coma" }
                  ]
                },
                {
                  label: "Peripheral",
                  children: [
                    { label: "Sensory & motor neuropathy; restless legs syndrome" }
                  ]
                },
                {
                  label: "Dialysis-related",
                  children: [
                    { label: "Dialysis dementia" },
                    { label: "Dialysis disequilibrium syndrome: first few sessions, rapid urea removal → cerebral edema" }
                  ]
                }
              ]
            },
            {
              label: "Dermatological",
              children: [
                { label: "Earthy face, pallor, ecchymosis/hematomas, pruritus, poor turgor, malnutrition, uremic frost, hemochromatosis discoloration, half-and-half nails, calciphylaxis" },
                { label: "NB: most improve with dialysis except pruritus" }
              ]
            },
            {
              label: "Urinary",
              children: [
                { label: "UTI" },
                { label: "Polyuria/nocturia early; oliguria/anuria late" }
              ]
            },
            {
              label: "Electrolytes & acid-base",
              children: [
                { label: "Hyperkalemia" },
                { label: "Hypocalcemia (tetany rare)" },
                { label: "Hyperphosphatemia (itching, metastatic calcification)" },
                { label: "Metabolic acidosis" }
              ]
            }
          ]
        },
        {
          label: "Investigations",
          children: [
            {
              label: "For degree & complications",
              children: [
                { label: "Urine analysis (albumin, ACR, sediment)" },
                { label: "KFT (urea, creatinine, eGFR)" },
                { label: "Electrolytes, ABG, uric acid" },
                { label: "CBC, iron studies, iPTH" },
                { label: "Skeletal survey" }
              ]
            },
            {
              label: "For underlying disease",
              children: [
                { label: "Electrophoresis" },
                { label: "ANA, dsDNA, C3, C4, ANCA, anti-GBM Ab" },
                { label: "HCV, HBV, HIV" },
                { label: "Imaging: KUB, US, CT, MRI, renogram" },
                { label: "Renal biopsy (not if small atrophic kidney)" }
              ]
            },
            {
              label: "Acute-on-chronic features (help identify CKD even in first presentation)",
              children: [
                { label: "Bone disease (CKD-MBD)" },
                { label: "Uremic neuropathy" },
                { label: "Profound anemia + hyperphosphatemia + high creatinine with mild symptoms" },
                { label: "Small kidneys by US (except: DM, amyloidosis, multiple myeloma, PCKD)" }
              ]
            }
          ]
        },
        {
          label: "Treatment",
          children: [
            {
              label: "Conservative management",
              children: [
                {
                  label: "Correct reversible causes",
                  children: [
                    { label: "Glucose control" },
                    { label: "BP control" },
                    { label: "Hydration" },
                    { label: "Relieve obstruction / treat UTI" },
                    { label: "Control active disease" },
                    { label: "Treat sepsis" },
                    { label: "Proteinuria: ACEI/ARB" },
                    { label: "Dyslipidemia" },
                    { label: "Lifestyle modifications" },
                    { label: "Avoid nephrotoxins" }
                  ]
                },
                {
                  label: "Diet",
                  children: [
                    { label: "Low protein: 0.6-0.8 g/kg/day (↑ to 1.0-1.2 on dialysis)" },
                    { label: "Low potassium" },
                    { label: "Low phosphate" },
                    { label: "Salt restriction" },
                    { label: "Fluid balance" }
                  ]
                },
                {
                  label: "GIT complications",
                  children: [
                    { label: "Prokinetics → consider dialysis" },
                    { label: "PPI (avoid long-term)" }
                  ]
                },
                {
                  label: "CVS complications",
                  children: [
                    { label: "ACEI/ARB/CCB/BB" },
                    { label: "Loop diuretics for volume overload" },
                    { label: "Dialysis for pericarditis" }
                  ]
                },
                {
                  label: "Mineral & bone disorder (CKD-MBD)",
                  children: [
                    {
                      label: "Diet",
                      children: [
                        { label: "Ca 1500-2000 mg/day" },
                        { label: "Low PO4: 800-1000 mg/day" }
                      ]
                    },
                    {
                      label: "Phosphate binders",
                      children: [
                        { label: "Calcium-based: Ca carbonate; hypercalcemia risk; avoid if PTH <130" },
                        { label: "Non-calcium: sevelamer, lanthanum" }
                      ]
                    },
                    { label: "Calcimimetics: cinacalcet" },
                    {
                      label: "Vitamin D analogs",
                      children: [
                        { label: "Alfacalcidol / calcitriol 0.25-2 µg/day" },
                        { label: "Indications: Ca <9.5, PO4 <4.6, ↑PTH" }
                      ]
                    },
                    {
                      label: "Parathyroidectomy",
                      children: [
                        { label: "PTH >800 not responding to medical therapy" }
                      ]
                    }
                  ]
                },
                {
                  label: "Anemia",
                  children: [
                    { label: "Iron: oral / IV" },
                    { label: "EPO alpha / beta" },
                    { label: "Darbepoetin alpha" },
                    { label: "CERA" }
                  ]
                },
                {
                  label: "Pruritus",
                  children: [
                    { label: "Ointment" },
                    { label: "Gabapentin / naltrexone" },
                    { label: "UV therapy" },
                    { label: "Increase dialysis" }
                  ]
                },
                {
                  label: "Electrolytes & acid-base",
                  children: [
                    { label: "See Chapter V" }
                  ]
                }
              ]
            },
            {
              label: "Educational program",
              children: [
                { label: "Explain eventual renal failure & available therapies" },
                { label: "HD: prepare AV fistula early" },
                { label: "PD/transplant: early family education" }
              ]
            },
            {
              label: "Renal replacement therapy",
              children: [
                { label: "Dialysis and transplantation" }
              ]
            }
          ]
        }
      ]
    },
    // ---------------- Topic 12 ----------------
    {
      label: "12. Renal Replacement Therapy",
      children: [
        {
          label: "RRT overview",
          children: [
            { label: "Dialysis (peritoneal & hemodialysis)" },
            { label: "Renal transplantation" }
          ]
        },
        {
          label: "Dialysis",
          children: [
            {
              label: "Definition",
              children: [
                { label: "Diffusion across semipermeable membrane (blood ↔ dialysate)" }
              ]
            },
            {
              label: "Indications",
              children: [
                {
                  label: "Temporary (acute/urgent)",
                  children: [
                    { label: "AKI: early dialysis advice" },
                    { label: "Uremic symptoms & complications: refractory hyperkalemia, intractable acidosis, fluid overload, pericarditis/pleuritis, CNS, GIT, bleeding" },
                    { label: "Dialyzable toxins: alcohols, aspirin, lithium, contrast" }
                  ]
                },
                {
                  label: "Permanent (chronic/maintenance)",
                  children: [
                    { label: "Grade 5 CKD, GFR ≤10 ml/min (Cr 8-10 mg/dL)" }
                  ]
                }
              ]
            },
            {
              label: "Contraindications",
              children: [
                { label: "Refractory hypotension" },
                { label: "Terminal illness" },
                { label: "Organic brain damage" }
              ]
            },
            {
              label: "Types",
              children: [
                {
                  label: "Peritoneal dialysis (PD)",
                  children: [
                    { label: "Principles: peritoneal membrane as semipermeable; equilibration; effluent removal" },
                    {
                      label: "Indications",
                      children: [
                        { label: "Symptomatic uremia" },
                        { label: "Slowly rising urea" },
                        { label: "Cardiovascular instability (unsuitable for HD)" },
                        { label: "No HD facilities" },
                        { label: "Immature AVF" },
                        { label: "Poor vascular access" },
                        { label: "Anticoagulation risk (unsuitable for HD)" }
                      ]
                    },
                    {
                      label: "Contraindications",
                      children: [
                        {
                          label: "Absolute",
                          children: [
                            { label: "Peritoneal fibrosis >50%" },
                            { label: "Pleuro-peritoneal leak" },
                            { label: "Multiple abdominal wounds" }
                          ]
                        },
                        {
                          label: "Relative",
                          children: [
                            { label: "Abdominal problems" },
                            { label: "Hypercatabolism" },
                            { label: "Aortic prosthesis" },
                            { label: "Huge PCKD" },
                            { label: "Diverticulosis" },
                            { label: "Morbid obesity" },
                            { label: "Hyperlipidemia" },
                            { label: "Gastroparesis" },
                            { label: "Self-care inability" }
                          ]
                        }
                      ]
                    },
                    {
                      label: "Advantages",
                      children: [
                        { label: "Safe and easy" },
                        { label: "Preserves residual renal function" },
                        { label: "No anticoagulation" },
                        { label: "No vascular surgery" },
                        { label: "Slow clearance (gentle)" },
                        { label: "Better PTH control" },
                        { label: "Liberal diet & fluid" },
                        { label: "Fewer medications" },
                        { label: "Cheaper" },
                        { label: "Less virus transmission" }
                      ]
                    },
                    {
                      label: "Disadvantages",
                      children: [
                        { label: "Long time (continuous)" },
                        { label: "Low efficiency" },
                        { label: "Inadequate clearance in hypercatabolic/large patients" },
                        { label: "Recent abdominal surgery or severe pulmonary compromise" },
                        { label: "Complications" }
                      ]
                    },
                    {
                      label: "Complications",
                      children: [
                        { label: "Peritonitis" },
                        { label: "Exit-site/tunnel infection" },
                        { label: "Constipation" },
                        { label: "Dialysate leak: pleural (hydrothorax), scrotal" },
                        { label: "Ultrafiltration failure" },
                        { label: "Sclerosing peritonitis" },
                        { label: "Protein loss & malnutrition" },
                        { label: "Hyperlipidemia" },
                        { label: "Obesity" },
                        { label: "Hernias" },
                        { label: "Traumatic catheter perforation" },
                        { label: "Cannula clotting" }
                      ]
                    }
                  ]
                },
                {
                  label: "Hemodialysis (HD)",
                  children: [
                    { label: "Definition: diffusion; remove unwanted, add desirable" },
                    {
                      label: "Advantages",
                      children: [
                        { label: "Short time (intermittent)" },
                        { label: "Efficient" },
                        { label: "Home HD possible" }
                      ]
                    },
                    {
                      label: "Complications",
                      children: [
                        {
                          label: "Surgical (vascular access)",
                          children: [
                            {
                              label: "Catheters",
                              children: [
                                { label: "Bleeding" },
                                { label: "Infection" },
                                { label: "Thrombosis / stenosis" },
                                { label: "Pneumothorax" },
                                { label: "Air embolism" }
                              ]
                            },
                            {
                              label: "AV fistula & graft",
                              children: [
                                { label: "Stenosis" },
                                { label: "Thrombosis" },
                                { label: "Infection" },
                                { label: "Outflow failure" },
                                { label: "Steal syndrome" },
                                { label: "Venous hypertension" },
                                { label: "High-output heart failure" },
                                { label: "Pseudo-aneurysms" }
                              ]
                            }
                          ]
                        },
                        {
                          label: "Acute medical",
                          children: [
                            { label: "IDH (intradialytic hypotension)" },
                            { label: "Hypertension" },
                            { label: "Cramps" },
                            { label: "Nausea & vomiting" },
                            { label: "Headache" },
                            { label: "Fever" },
                            { label: "Hemolysis" },
                            { label: "Bleeding" },
                            { label: "Circuit clotting" },
                            { label: "Chest pain" },
                            { label: "Arrhythmias" },
                            { label: "Cardiac arrest" },
                            { label: "Air embolism" },
                            { label: "Disequilibrium syndrome" }
                          ]
                        },
                        {
                          label: "Chronic",
                          children: [
                            {
                              label: "Cardiovascular",
                              children: [
                                {
                                  label: "Cardiac",
                                  children: [
                                    { label: "Ischemic heart disease" },
                                    { label: "Valvular heart disease" },
                                    { label: "Uremic pericarditis & endocarditis" },
                                    { label: "Dilated cardiomyopathy" }
                                  ]
                                },
                                {
                                  label: "Vascular",
                                  children: [
                                    { label: "Peripheral vascular disease" },
                                    { label: "Metastatic calcification" }
                                  ]
                                }
                              ]
                            },
                            { label: "Neuropsychiatric: anxiety, depression, dementia" },
                            { label: "Malnutrition" },
                            { label: "Dialysis osteomalacia" },
                            { label: "Dialysis-related amyloidosis" },
                            {
                              label: "Rheumatologic",
                              children: [
                                { label: "Crystal arthritis" },
                                { label: "Joint & bone infection" },
                                { label: "Ischemic necrosis" }
                              ]
                            },
                            { label: "Hypersplenism" },
                            { label: "Acquired renal cystic disease (>3 years, malignant change)" }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ]
        },
        {
          label: "Kidney transplantation",
          children: [
            {
              label: "Definition",
              children: [
                { label: "Implantation of a kidney from living or deceased donor" }
              ]
            },
            {
              label: "Donors",
              children: [
                { label: "Living related" },
                { label: "Living unrelated" },
                { label: "Deceased (cadaveric)" }
              ]
            },
            {
              label: "Contraindications",
              children: [
                { label: "Patient refusal" },
                { label: "Psychosis" },
                { label: "Elderly (relative)" },
                { label: "Active sepsis" },
                { label: "Unstable CVD" },
                { label: "Severe respiratory distress" },
                { label: "Cerebrovascular hemorrhage" },
                { label: "Advanced liver disease (unless combined liver-kidney)" },
                { label: "Malignancies" },
                { label: "Urological abnormalities" }
              ]
            },
            {
              label: "Complications",
              children: [
                {
                  label: "Surgical",
                  children: [
                    { label: "Technical failures" },
                    { label: "Vascular thrombosis" },
                    { label: "Urine leak at anastomosis" },
                    { label: "Leg lymphedema" }
                  ]
                },
                {
                  label: "Medical",
                  children: [
                    { label: "ATN (acute tubular necrosis)" },
                    { label: "Rejection: hyperacute, acute, chronic" },
                    { label: "Immunosuppression complications" },
                    { label: "Recurrence of original disease" },
                    { label: "Opportunistic infections" },
                    { label: "Malignancy: Kaposi sarcoma, lymphoproliferative disorders" },
                    { label: "HTN, DM, atherosclerosis, bone disease" },
                    { label: "GIT bleeding, cataract, marrow suppression" },
                    { label: "Nephrotoxicity, hepatotoxicity" }
                  ]
                }
              ]
            }
          ]
        }
      ]
    }
  ]
};