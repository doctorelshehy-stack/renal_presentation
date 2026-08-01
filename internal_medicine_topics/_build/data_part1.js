// ============================================================
// Folder 01 — Glomerular Diseases
// Separate cards per common title (Definition / Causes /
// Pathology / Clinical / Investigations / Treatment / Course)
// ============================================================
const folderGlomerular = {
  label: "01 · Glomerular Diseases",
  children: [
    // ---------------- Topic 1 ----------------
    {
      label: "1. Principles of Glomerulopathies",
      children: [
        {
          label: "Definition",
          children: [
            { label: "Group of glomerular disorders" },
            { label: "Characterized clinically, pathologically & etiologically" },
            { label: "5 cardinal features, singly or combined: proteinuria, hematuria, oliguria, hypertension, edema" },
            { label: "Both kidneys involved symmetrically" },
            { label: "Primary GN = unknown cause (idiopathic)" },
            { label: "Secondary GN = various causes" }
          ]
        },
        {
          label: "Causes",
          children: [
            {
              label: "Primary (idiopathic)",
              children: [
                { label: "Unknown causes" }
              ]
            },
            {
              label: "Secondary",
              children: [
                {
                  label: "Infections (post-infectious)",
                  children: [
                    {
                      label: "Bacterial",
                      children: [
                        { label: "Streptococcal β-hemolytic types 1, 4, 12, 49 → post-streptococcal GN" },
                        { label: "Non-streptococcal: staphylococci, gonococci, salmonella, meningococcal, secondary syphilis, leprosy" }
                      ]
                    },
                    {
                      label: "Viral",
                      children: [
                        { label: "HBV, HCV, HIV, EBV (infectious mononucleosis), mumps, measles, coxsackie, varicella" }
                      ]
                    },
                    {
                      label: "Parasitic",
                      children: [
                        { label: "Malaria, schistosomiasis, filariasis, toxoplasmosis" }
                      ]
                    }
                  ]
                },
                {
                  label: "Multisystem diseases",
                  children: [
                    { label: "SLE, rheumatoid arthritis, dermatomyositis, Sjögren's syndrome, Goodpasture's syndrome" },
                    { label: "Vasculitis: PAN, Wegener's granulomatosis, Henoch-Schönlein purpura" }
                  ]
                },
                {
                  label: "Malignant diseases & paraproteinemias",
                  children: [
                    { label: "Carcinoma: lung, colon, melanoma" },
                    { label: "Hematological: lymphomas (HL, non-HL) and leukemias" },
                    { label: "Paraproteinemias: multiple myeloma, amyloidosis, Waldenström's macroglobulinemia, cryoglobulinemia" }
                  ]
                },
                {
                  label: "Drugs & toxins",
                  children: [
                    { label: "Penicillin, heavy metals (mercury, gold), heroin, captopril, antivenom, antitoxins, contrast media" }
                  ]
                },
                {
                  label: "Metabolic",
                  children: [
                    { label: "Diabetes mellitus and gout" }
                  ]
                },
                {
                  label: "Heredofamilial",
                  children: [
                    { label: "Thin basement membrane disease, Alport's syndrome, Fabry's disease, Nail-Patella syndrome, sickle cell disease" }
                  ]
                },
                {
                  label: "Others",
                  children: [
                    { label: "Sarcoidosis, pre-eclampsia, thyrotoxicosis & myxedema, serum sickness, chronic graft rejection" },
                    { label: "Allergic: bee stings, pollens, cow milk" }
                  ]
                }
              ]
            }
          ]
        },
        {
          label: "Pathology",
          children: [
            {
              label: "Macroscopic",
              children: [
                { label: "Of no value (evaluated by ultrasound)" },
                {
                  label: "Acute GN",
                  children: [
                    { label: "Kidney size: normal or increased" },
                    { label: "Surface: punctate hemorrhage" }
                  ]
                },
                {
                  label: "Chronic GN",
                  children: [
                    { label: "Kidney size: normal or decreased" },
                    { label: "Surface: fine granular or cortical scars" }
                  ]
                }
              ]
            },
            {
              label: "Microscopic (renal biopsy)",
              children: [
                {
                  label: "LM (light microscopy)",
                  children: [
                    { label: "Histopathological type" },
                    { label: "Severity / degree of disease" }
                  ]
                },
                {
                  label: "EM (electron microscopy)",
                  children: [
                    { label: "Site of immune deposition: subendothelial, subepithelial, mesangial" }
                  ]
                },
                {
                  label: "IF (immunofluorescence)",
                  children: [
                    { label: "Type of immune deposition e.g. IgA, C3, C4" },
                    { label: "Immune-complex GN → diffuse granular pattern" },
                    { label: "Anti-GBM antibody → smooth linear pattern" }
                  ]
                }
              ]
            }
          ]
        },
        {
          label: "Histopathological types",
          children: [
            {
              label: "Minimal lesion GN (Minimal Change Disease, MCD)",
              children: [
                { label: "LM: normal or mild increase in mesangial cells" },
                { label: "EM: fusion of foot processes of podocytes" },
                { label: "IF: no deposits" }
              ]
            },
            {
              label: "Membranous GN (MGN)",
              children: [
                { label: "LM: diffuse thickening of glomerular basement membrane" }
              ]
            },
            {
              label: "Proliferative GN",
              children: [
                {
                  label: "Diffuse proliferative",
                  children: [
                    { label: "Proliferation of all glomerular cells (endothelial, epithelial & mesangial)" },
                    { label: "Acute diffuse proliferative GN" },
                    { label: "Diffuse proliferation with crescents (crescentic GN, RPGN)" },
                    { label: "Mesangio-proliferative GN (MPGN): increased mesangial cells & matrix" },
                    { label: "Mesangio-capillary GN (MCGN): mesangial proliferation + matrix + GBM thickening" }
                  ]
                },
                {
                  label: "Focal proliferative",
                  children: [
                    { label: "Focal segmental GN (FSGN): cellular proliferation of some segments in some glomeruli" }
                  ]
                }
              ]
            },
            {
              label: "Focal segmental glomerulosclerosis (FSGS)",
              children: [
                { label: "Sclerosis of some segments in some glomeruli" }
              ]
            }
          ]
        },
        {
          label: "Clinical presentations (5 syndromes)",
          children: [
            {
              label: "Acute GN (acute nephritic syndrome)",
              children: [
                { label: "Onset: relatively abrupt" },
                { label: "Features: hematuria, proteinuria, oliguria, edema, hypertension" },
                { label: "Pathology: DPGN" },
                { label: "Course: spontaneous resolution" }
              ]
            },
            {
              label: "Nephrotic syndrome",
              children: [
                { label: "Onset: variable" },
                { label: "Features: albumin <2.5 g/dl, proteinuria ≥3+, hyperlipidemia, edema, hypertension (MCGN)" },
                { label: "Pathology: variable lesions" },
                { label: "Course: variable" },
                { label: "Notes: variable onset, pathology & course" }
              ]
            },
            {
              label: "Chronic GN",
              children: [
                { label: "Onset: insidious / progressive" },
                { label: "Features: proteinuria 0-1+, hypertension, urinary sediment +, slow progressive GFR decline" },
                { label: "Pathology: glomerulosclerosis, chronic interstitial fibrosis" },
                { label: "Course: progress to renal failure" },
                { label: "Notes: the common path to ESRD" }
              ]
            },
            {
              label: "Rapidly Progressive GN (RPGN)",
              children: [
                { label: "Onset: rapid decline in GFR" },
                { label: "Features: hematuria, proteinuria, oliguria, absent or mild hypertension" },
                { label: "Pathology: DPGN with crescents" },
                { label: "Course: rapidly progress to AKI" },
                { label: "Notes: renal emergency, intensive therapy" }
              ]
            },
            {
              label: "Asymptomatic proteinuria ± hematuria",
              children: [
                { label: "Onset: insidious" },
                { label: "Features: hematuria/proteinuria, hypertension ±, normal GFR" },
                { label: "Pathology: FSGN" },
                { label: "Course: persist or recurrent" },
                { label: "Notes: accidentally discovered, relatively benign" }
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
                { label: "Volume in 24 hours: may be decreased or normal" },
                { label: "24-hour urinary protein or urinary protein/creatinine ratio" },
                { label: "Microscopy of sediment: red cells may or may not be present" },
                { label: "Dysmorphic red cells → strongly suggestive of GN" },
                { label: "Granular & red cell casts → diagnostic of acute GN" }
              ]
            },
            {
              label: "Blood examination",
              children: [
                { label: "Blood urea" },
                { label: "Serum creatinine" },
                { label: "Serum electrolytes (Ca, PO4, K+, Na+)" },
                { label: "Assessment of GFR (normal 90-120 ml/min)" }
              ]
            },
            {
              label: "Renal imaging (US)",
              children: [
                { label: "To exclude other renal pathology" },
                { label: "Smooth renal outline" },
                { label: "Normal pelvicalyceal system & lower urinary tract" }
              ]
            },
            {
              label: "Renal biopsy",
              children: [
                { label: "Accurate histopathological diagnosis" },
                { label: "Assess severity & response to treatment" },
                { label: "Prognosis" }
              ]
            },
            {
              label: "Specific investigations (for cause)",
              children: [
                { label: "Blood glucose → diabetes mellitus" },
                { label: "ASOT + throat/skin swab → recent streptococcal infection" },
                { label: "ANA & anti-dsDNA → systemic disease e.g. SLE" },
                { label: "Anti-GBM antibody → Goodpasture's disease" },
                { label: "Serum IgA → IgA nephropathy (Berger's disease)" },
                {
                  label: "Serum complement — decreased in",
                  children: [
                    { label: "Post-infection e.g. acute post-streptococcal GN (transient ~8 weeks), infective endocarditis, shunt nephropathy" },
                    { label: "SLE" },
                    { label: "Cryoglobulinemia" },
                    { label: "Serum sickness" }
                  ]
                }
              ]
            }
          ]
        },
        {
          label: "Treatment",
          children: [
            {
              label: "General aims",
              children: [
                { label: "Control of symptoms" },
                { label: "Prevent complications" },
                { label: "Slow progression of the disease" }
              ]
            },
            {
              label: "Diet",
              children: [
                { label: "Salt & water restriction for edematous and/or hypertensive patients, especially with oliguria" },
                { label: "High protein intake → ↑proteinuria in RF patients, nephron damage → progression" },
                { label: "Low protein intake → negative nitrogen balance and malnutrition" },
                { label: "Normal GFR → physiological needs (1 g/kg/day) + daily urinary protein loss" },
                { label: "↓GFR → moderate protein restriction (0.6-0.8 g/kg/day) to control anorexia, nausea, vomiting" }
              ]
            },
            {
              label: "Control of edema",
              children: [
                { label: "Bed rest" },
                { label: "Salt restriction (<2 g/day) & fluid restriction" },
                { label: "Diuretics: preferably loop diuretics; thiazides can be combined" },
                { label: "Salt-poor albumin (in resistant cases with hypoalbuminemia)" },
                { label: "Ultrafiltration" },
                { label: "Hemodialysis" }
              ]
            },
            {
              label: "Control of proteinuria",
              children: [
                { label: "Avoid high protein diet (0.8-1 g/day + estimated daily loss)" },
                {
                  label: "ACEIs & ARBs",
                  children: [
                    { label: "Compete with vasoconstriction of angiotensin II on efferent arterioles → efferent VD → ↓intraglomerular pressure → ↓GFR → ↓filtered protein → ↓proteinuria" },
                    { label: "Small doses in normotensives; cautious in renal failure & hyperkalemia" }
                  ]
                }
              ]
            },
            {
              label: "Control of hypertension",
              children: [
                {
                  label: "Value of BP control",
                  children: [
                    { label: "Relief of symptoms" },
                    { label: "Prevent hypertensive complications on other systems" },
                    { label: "Decrease progression of renal disease (reno-protective)" }
                  ]
                },
                {
                  label: "Targets by proteinuria",
                  children: [
                    { label: "Proteinuria >1 g/day → BP <125/75 (mean <92)" },
                    { label: "Proteinuria <1 g/day → BP <130/80 (mean <98)" }
                  ]
                },
                {
                  label: "Agents",
                  children: [
                    { label: "ACEIs/ARBs" },
                    { label: "CCBs" },
                    { label: "All have reno-protective effect" }
                  ]
                }
              ]
            },
            {
              label: "Control of hyperlipidemia",
              children: [
                { label: "Avoid high-fat diet" },
                { label: "Physical activity" },
                { label: "Statins (not used in HD patients)" }
              ]
            },
            {
              label: "Hypercoagulability & thrombosis",
              children: [
                { label: "Prophylactic anticoagulation in nephrotic syndrome with high thromboembolism risk" },
                { label: "Increased venous thrombosis risk (albumin <2.5) → anticoagulants" },
                { label: "Increased arterial thrombosis risk → aspirin" }
              ]
            },
            {
              label: "Specific treatment (by etiology)",
              children: [
                {
                  label: "Primary GN",
                  children: [
                    { label: "Immunosuppressive + cytotoxic agents" },
                    { label: "Other measures e.g. plasma exchange" }
                  ]
                },
                {
                  label: "Secondary GN",
                  children: [
                    { label: "Treat the cause: control infection, treat malignancy, stop toxins & drugs, control disease activity (SLE, DM, gout)" }
                  ]
                }
              ]
            }
          ]
        },
        {
          label: "Course",
          children: [
            { label: "Variable depending on renal pathology & etiology" },
            { label: "Anti-GBM & ANCA-associated crescentic GN → rapid progression to ESRD unless treated" },
            { label: "IgA nephropathy & FSGS → indolent but persistent course → renal failure" },
            { label: "Post-streptococcal GN → tends to resolve completely, little risk of ESRD" },
            { label: "MGN → unpredictable: may remit spontaneously, persist/relapse, or progress over years to ESRD" }
          ]
        }
      ]
    },
    // ---------------- Topic 2 ----------------
    {
      label: "2. Acute GN — Nephritic Syndrome",
      children: [
        {
          label: "Definition",
          children: [
            { label: "Acute onset of: hematuria (macro or microscopic)" },
            { label: "Proteinuria <3.5 g/day/1.73 m2" },
            { label: "Hypertension" },
            { label: "Edema" },
            { label: "Oliguria (<300 ml/day) in severe cases" }
          ]
        },
        {
          label: "Clinical features",
          children: [
            {
              label: "Hematuria",
              children: [
                {
                  label: "Macroscopic",
                  children: [
                    { label: "Red color urine in alkaline urine" },
                    { label: "Smoky / reddish-brown in acidic urine: denaturation of Hb → acid hematin; methemoglobin gives smoky color; prolonged transit time" }
                  ]
                },
                {
                  label: "Microscopic",
                  children: [
                    { label: "Dysmorphic red cells: small & distorted (mechanical injury through damaged glomerular capillary walls)" },
                    { label: "Low Hb content" },
                    { label: "Best seen by phase-contrast microscopy" }
                  ]
                }
              ]
            },
            {
              label: "Proteinuria",
              children: [
                { label: "Glomerular origin (mainly albumin)" },
                { label: "Non-nephrotic range <3.5 g/day" },
                { label: "Due to: increased glomerular capillary permeability" },
                { label: "Mechanical disruption of glomerular capillary walls" },
                { label: "Altered glomerular hemodynamics" }
              ]
            },
            {
              label: "Edema",
              children: [
                { label: "Early: eyelids (puffiness) — low tissue pressure" },
                { label: "Then legs and other parts" },
                { label: "Salt & water retention: increased distal Na+ reabsorption + decreased GFR → decreased salt delivery" }
              ]
            },
            {
              label: "Hypertension",
              children: [
                { label: "Salt & water retention → volume-dependent" }
              ]
            },
            {
              label: "Oliguria",
              children: [
                { label: "Urine output <300 ml/day due to decreased GFR" }
              ]
            },
            {
              label: "Manifestations of associated specific disease",
              children: [
                { label: "Infection (PSGN), SLE, vasculitis, malignancy" }
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
                { label: "Color: red or smoky (dark brown)" },
                { label: "Oliguria <300 ml/day in severe cases" },
                { label: "Proteinuria <3.5 g/day" },
                { label: "Hematuria" },
                { label: "Dysmorphic red cells & red cell casts — pathognomonic for acute GN" },
                { label: "Granular casts" }
              ]
            },
            {
              label: "Blood",
              children: [
                { label: "Urea, creatinine & GFR: variable impairment of renal function" }
              ]
            },
            {
              label: "Renal imaging",
              children: [
                { label: "Usually unnecessary" }
              ]
            },
            {
              label: "Renal biopsy",
              children: [
                { label: "Most acute GN pathology is proliferative (focal or diffuse)" },
                {
                  label: "Indications",
                  children: [
                    { label: "Unusual clinical features" },
                    { label: "Uncertain diagnosis" },
                    { label: "Rapid deterioration of renal function → crescentic GN" }
                  ]
                }
              ]
            },
            {
              label: "Specific investigations (etiology)",
              children: [
                { label: "ANA, ds-DNA → SLE" },
                { label: "Throat swab & ASOT + transient decrease of C3 (<8 weeks) → PSGN" }
              ]
            }
          ]
        },
        {
          label: "Treatment",
          children: [
            {
              label: "General",
              children: [
                { label: "Fluid chart (intake and output)" },
                { label: "Measurement of body weight and blood pressure" },
                {
                  label: "Home treatment (uncomplicated)",
                  children: [
                    { label: "Daily follow-up of blood pressure" },
                    { label: "Urea and creatinine every few days" }
                  ]
                },
                {
                  label: "Hospital admission (complicated)",
                  children: [
                    { label: "Severe hypertension" },
                    { label: "Renal failure & oliguria" },
                    { label: "Pulmonary edema" },
                    { label: "Encephalopathy" },
                    { label: "Until hematuria, HTN & edema disappear & proteinuria decreases" },
                    { label: "Strict bed rest in complicated cases (severe HTN, pulmonary edema)" }
                  ]
                },
                { label: "Salt restriction" },
                { label: "Fluid restriction in oliguric patients (0.5 L + volume of previous day urine)" },
                { label: "Protein restriction in renal failure (0.6-0.8 g/kg/day ≈ 40 g/day for adult)" }
              ]
            },
            {
              label: "Hypertension & edema",
              children: [
                { label: "Salt restriction" },
                { label: "Diuretics: loop diuretic" },
                { label: "Antihypertensives: β-blockers with caution — may precipitate pulmonary edema in impending HF" }
              ]
            },
            {
              label: "Hypertensive encephalopathy",
              children: [
                { label: "Maintain airway" },
                { label: "Control BP by parenteral agent: hydralazine 5-20 mg infusion" },
                { label: "Control fits: IV diazepam 10 mg" }
              ]
            },
            {
              label: "Pulmonary edema / HF",
              children: [
                { label: "Salt and water restriction" },
                { label: "Ultrafiltration (dialysis) to remove excess fluid in oliguric patient" },
                { label: "Acute RF → dialysis" }
              ]
            },
            {
              label: "Specific treatment",
              children: [
                {
                  label: "Primary GN",
                  children: [
                    { label: "Corticosteroid ± immunosuppressives depending on histopathological type" }
                  ]
                },
                {
                  label: "Secondary GN",
                  children: [
                    { label: "Treat the cause: PSGN, diabetic nephropathy, lupus nephritis" }
                  ]
                }
              ]
            }
          ]
        }
      ]
    },
    // ---------------- Topic 3 ----------------
    {
      label: "3. Nephrotic Syndrome",
      children: [
        {
          label: "Definition",
          children: [
            { label: "Heavy proteinuria ≥3.5 g/day/1.73 m2 or UPCR >3.5 in adults" },
            { label: "Hypoalbuminemia ≤2.5 g/dl" },
            { label: "Edema" },
            { label: "Hyperlipidemia (hypercholesterolemia)" }
          ]
        },
        {
          label: "Causes",
          children: [
            { label: "All causes of acute GN" },
            {
              label: "Primary",
              children: [
                { label: "MCD, MGN, MPGN, MCGN, FSGN" }
              ]
            },
            {
              label: "Secondary",
              children: [
                { label: "Infection, multisystem, malignancy, drugs, metabolic, familial" }
              ]
            }
          ]
        },
        {
          label: "Clinical features",
          children: [
            { label: "Proteinuria: frothy urine (protein decreases surface tension, like bile salts & detergents)" },
            { label: "Edema: generalized — limbs, face, genitalia & serous cavities (ascites, pleural & pericardial effusion); severity correlates with serum albumin & urinary protein losses; conditioned by HF" },
            {
              label: "Hypertension (variable)",
              children: [
                { label: "MCD → blood pressure always normal" },
                { label: "MCGN → hypertension always present" }
              ]
            }
          ]
        },
        {
          label: "Investigations",
          children: [
            { label: "24 h urine protein >3.5 g/day in adults" },
            {
              label: "Plasma proteins",
              children: [
                { label: "Serum albumin ≤2.5 g/dl" },
                { label: "Electrophoresis: ↓albumin, ↑alpha-2 & beta globulin, normal or slightly ↑gamma globulin, ↑fibrinogen" }
              ]
            },
            {
              label: "Plasma lipids",
              children: [
                { label: "↑cholesterol and LDL" },
                { label: "↑TG in 50%" },
                { label: "Normal or ↓HDL (urine loss)" }
              ]
            },
            { label: "Hypocalcemia: urinary loss of cholecalciferol-binding protein" },
            {
              label: "Renal function tests",
              children: [
                { label: "Urea, creatinine, eGFR usually normal" },
                { label: "Impaired in: severe hypovolemia → pre-renal AKI, MGN and MCGN" },
                { label: "NB: with impaired renal function, biochemical features of NS are uncommon (concomitant decreased GFR)" }
              ]
            },
            { label: "Urine exam: red cells & red cell casts → GN and exclude MCD" },
            { label: "PLA2R antibody → primary membranous nephropathy" },
            { label: "↓serum C3 → immune-complex mediated GN" },
            { label: "ASOT & throat swab → streptococcal infection" },
            { label: "ANA → SLE; ANCA → systemic vasculitis" },
            { label: "Hyperglycemia → diabetes mellitus" },
            {
              label: "Selective proteinuria (tested in children)",
              children: [
                { label: "Clearance of large MW protein (IgG) vs small MW protein (albumin, transferrin) measured simultaneously" },
                { label: "Low ratio → selective: MCD, DM, renal amyloidosis" },
                { label: "High ratio → unselective: crescentic GN" }
              ]
            },
            {
              label: "Renal biopsy",
              children: [
                {
                  label: "Indications",
                  children: [
                    { label: "Histological diagnosis and to plan therapy" },
                    {
                      label: "In children",
                      children: [
                        { label: "Steroid resistant, dependent and frequent relapse" },
                        { label: "Children with renal impairment" }
                      ]
                    },
                    { label: "In adults: most adults" }
                  ]
                },
                {
                  label: "Not indicated",
                  children: [
                    { label: "Young children with selective proteinuria, normotensive & benign urinary sediment → MCD" },
                    { label: "Long-standing DM (>10 years type 1, >5 years type 2) with retinopathy or neuropathy" },
                    { label: "Patient under drug therapy such as penicillamine" }
                  ]
                }
              ]
            }
          ]
        },
        {
          label: "Treatment",
          children: [
            {
              label: "Protein intake",
              children: [
                { label: "Daily physiological need (1 g/kg) + daily urinary protein losses" },
                { label: "Protein restriction 0.6-0.8 g/kg/day in renal impairment" },
                {
                  label: "High protein intake (1.5-2 g/kg/day) NOT advised",
                  children: [
                    { label: "Ineffective: increases protein loss" },
                    { label: "Difficult to manage with concomitant salt restriction" },
                    { label: "Could aggravate glomerular damage" }
                  ]
                }
              ]
            },
            {
              label: "Drug control of proteinuria",
              children: [
                { label: "ACEI & ARBs: ↓intraglomerular hydrostatic pressure → ↓filtered urinary protein losses" },
                { label: "Medical nephrectomy (mercurial drug or renal infarction) to abolish severe persistent proteinuria in ESRD" }
              ]
            },
            {
              label: "Control of edema",
              children: [
                { label: "Bed rest → induces diuresis" },
                { label: "Na+ restriction" },
                { label: "Diuretics in unresponsive patients" },
                {
                  label: "Human albumin infusion",
                  children: [
                    { label: "Indications: severe hypoalbuminemia; diuretic-resistant patient undergoing surgery/invasive procedure (biopsy)" },
                    { label: "Disadvantages: expensive; transient effect (24-48 hours)" }
                  ]
                }
              ]
            },
            {
              label: "Control of complications",
              children: [
                { label: "Subnutrition: proper diet, minerals, vitamins; severe proteinuria may justify renal ablation (medical or surgical)" },
                { label: "Sepsis: early detection and aggressive treatment" },
                { label: "Hyperlipidemia: statins" },
                { label: "Hypertension: salt restriction + antihypertensives" },
                {
                  label: "Thrombotic complications",
                  children: [
                    { label: "Long-term oral anticoagulant" },
                    { label: "Heparin ineffective: urinary loss of antithrombin III" },
                    { label: "Prophylaxis in membranous GN (thromboembolic complications common)" }
                  ]
                }
              ]
            },
            {
              label: "Specific treatment",
              children: [
                {
                  label: "Primary NS",
                  children: [
                    { label: "Depends on histopathological type: MCD, MGN, MCGN, FSGN" }
                  ]
                },
                {
                  label: "Secondary NS",
                  children: [
                    { label: "SLE → steroids + cyclophosphamide" },
                    { label: "DM → control of hyperglycemia" }
                  ]
                }
              ]
            }
          ]
        }
      ]
    },
    // ---------------- Topic 4 ----------------
    {
      label: "4. Anti-GBM Disease & Goodpasture Syndrome",
      children: [
        {
          label: "Definition",
          children: [
            {
              label: "Goodpasture Disease (Anti-GBM GN)",
              children: [
                { label: "Kidney-limited disease" },
                { label: "GN from glomerular deposition of anti-GBM antibodies" },
                { label: "Circulating anti-GBM antibodies" }
              ]
            },
            {
              label: "Goodpasture Syndrome",
              children: [
                { label: "Systemic disease with triad" },
                { label: "GN from glomerular deposition of anti-GBM antibodies" },
                { label: "Circulating anti-GBM antibodies" },
                { label: "Pulmonary hemorrhage" }
              ]
            }
          ]
        },
        {
          label: "Pathology / Histopathology",
          children: [
            { label: "Diffuse proliferative GN by LM" },
            { label: "Linear deposits of anti-GBM IgG antibody by IF" },
            { label: "G.P. Disease → GN only" },
            { label: "G.P. Syndrome → GN + pulmonary hemorrhage" }
          ]
        },
        {
          label: "Differential diagnosis (pulmonary-renal syndromes)",
          children: [
            { label: "Goodpasture syndrome" },
            { label: "Henoch-Schönlein purpura" },
            { label: "Systemic lupus erythematosus (SLE)" },
            { label: "Microscopic polyangiitis" },
            { label: "Cryoglobulinemia" },
            { label: "Advanced uremia with pulmonary edema and coagulopathies" },
            { label: "Thrombotic thrombocytopenic purpura (TTP)" },
            { label: "Pulmonary embolism with RV thrombosis" }
          ]
        },
        {
          label: "Investigations",
          children: [
            { label: "Urine: evidence of GN — hematuria with dysmorphic red cells, red cell casts, variable proteinuria" },
            { label: "Blood: positive circulating anti-GBM antibodies" },
            { label: "Other serology (complements, ASOT, ANA) normal" },
            { label: "Renal biopsy: diffuse proliferative GN" }
          ]
        },
        {
          label: "Treatment",
          children: [
            {
              label: "Corticosteroids",
              children: [
                { label: "IV methylprednisolone 7-15 mg/kg/day (max 1 g/day) for 3 days" },
                { label: "Then oral prednisone 1 mg/kg/day" },
                { label: "Reduce to 20 mg/day by 6 weeks" },
                { label: "Continue for 6 months" }
              ]
            },
            {
              label: "Cyclophosphamide (dose by age)",
              children: [
                { label: "<55 years: 3 mg/kg (down to 50 mg) for 3 months" },
                { label: ">55 years: 2 mg/kg (down to 50 mg) for 3 months" }
              ]
            },
            {
              label: "Plasma exchange (plasmapheresis)",
              children: [
                { label: "Daily 40-50 ml/kg plasma replaced with albumin" },
                { label: "For 2 weeks or until anti-GBM antibody disappears" },
                { label: "Not given in anuria and/or crescents >85% of glomeruli unless pulmonary hemorrhage" },
                { label: "Albumin is the recommended replacement (lower incidence of complications)" }
              ]
            },
            {
              label: "Summary",
              children: [
                { label: "3 days pulse methylprednisolone → 2 weeks daily plasmapheresis → 6 months oral corticosteroids + 3 months cyclophosphamide" }
              ]
            }
          ]
        }
      ]
    },
    // ---------------- Topic 5 ----------------
    {
      label: "5. Post-Streptococcal GN",
      children: [
        {
          label: "Organism",
          children: [
            { label: "Group A β-hemolytic streptococci (nephritogenic strains, types 1, 4, 12, 49)" },
            { label: "Type 49 is the most common isolated type" }
          ]
        },
        {
          label: "History of streptococcal infection",
          children: [
            { label: "Tonsillitis, pharyngitis, otitis media, or cellulitis: 1-2 weeks before onset of acute nephritis" },
            { label: "Skin infection → latent period may be prolonged to 4 weeks" },
            { label: "Latent period = time for immune-complex formation, deposition & glomerular injury" },
            { label: "Shorter latent period → exacerbation of underlying CKD (e.g. IgA nephropathy) rather than de novo acute GN" }
          ]
        },
        {
          label: "Presentations",
          children: [
            {
              label: "Acute GN",
              children: [
                { label: "Children: picture of acute GN" },
                { label: "Adults: strep history less commonly obtained; subacute/insidious onset with progressive slowly developing edema of lower limbs" },
                { label: "~10% of infected develop GN" },
                { label: "Infection may be mild and pass unnoticed" },
                { label: "No relationship between severity of infection & probability of developing acute nephritis" }
              ]
            },
            { label: "Nephrotic syndrome: uncommon (<20% of cases)" },
            { label: "RPGN: in 5% of cases" },
            { label: "Asymptomatic: discovered during routine urine examination" }
          ]
        },
        {
          label: "Investigations",
          children: [
            {
              label: "Evidence of streptococcal infection",
              children: [
                { label: "Antibodies to streptococcal exo-enzymes (SO, DNAase, BNDase, hyaluronidase)" },
                { label: "Decreased CH50 & C3 during acute phase, returns to normal within 8 weeks (transient hypocomplementemia)" }
              ]
            },
            {
              label: "Evidence of acute GN",
              children: [
                { label: "Urine: dysmorphic red cells, red cell casts, proteinuria <3 g/day" },
                { label: "Blood: transient ↑serum cholesterol (in NS), ↓serum albumin, renal impairment" },
                {
                  label: "Renal biopsy",
                  children: [
                    { label: "LM: diffuse endocapillary proliferative GN ± few crescents" },
                    { label: "EM: subepithelial electron-dense deposits (humps) ± variable mesangial deposits" },
                    { label: "IF: granular deposits of C3 & IgG" }
                  ]
                }
              ]
            }
          ]
        },
        {
          label: "Treatment",
          children: [
            {
              label: "General / supportive (see treatment of GN)",
              children: [
                { label: "Bed rest" },
                { label: "Diet: salt, fluid and protein restriction" },
                { label: "Drugs: diuretics; vasodilators for BP control" },
                { label: "Steroids, cytotoxic drugs & anticoagulants of no value, may be harmful — except in RPGN" },
                { label: "Dialysis for renal failure" }
              ]
            },
            {
              label: "Antibiotic (penicillin) therapy",
              children: [
                {
                  label: "For patients",
                  children: [
                    { label: "Decrease antigen load → decrease immune-complex formation → may stop disease progression" },
                    { label: "Halt spread of nephritogenic streptococci to close family contacts" },
                    { label: "Not very effective in aborting or ameliorating the disease course" }
                  ]
                },
                {
                  label: "For close contacts",
                  children: [
                    { label: "Short-term penicillin prophylaxis (phenoxy penicillin 500 mg/day) for high-risk individuals in closed community/family" }
                  ]
                }
              ]
            }
          ]
        },
        {
          label: "N.B.",
          children: [
            { label: "No effect of long-term penicillin prophylaxis after development of GN" },
            { label: "Removal of infected tonsil/septic foci delayed until convalescence advanced (operation may exacerbate disease)" },
            { label: "If needed: benzyl penicillin on day of operation and 3 days after" }
          ]
        }
      ]
    },
    // ---------------- Topic 6 ----------------
    {
      label: "6. Lupus Nephritis",
      children: [
        {
          label: "Definition",
          children: [
            { label: "Renal involvement in patients with SLE" },
            { label: "Exists with or without clinical manifestations of SLE" },
            { label: "Extremely diverse in presentation and pathology" }
          ]
        },
        {
          label: "Prevalence",
          children: [
            { label: "Kidney is the most common organ involvement in SLE" },
            { label: "Clinically ~50% of lupus patients have LN at diagnosis" }
          ]
        },
        {
          label: "Pathology",
          children: [
            {
              label: "Glomerular",
              children: [
                { label: "Haematoxylin bodies: rounded bluish inclusions in H&E; naked nuclei altered by binding to ANA; seen in only 2% of cases; pathognomonic of active LN" },
                { label: "Wire loop deposits: subendothelial immune deposits encircling entire glomerular tuft circumference; best seen in trichrome & silver stains" },
                { label: "Hyaline thrombi: massive subendothelial immune deposits protruding into or occluding tuft lumina (intraluminal immune deposits)" }
              ]
            },
            {
              label: "Tubulo-interstitial",
              children: [
                { label: "Seen in 50% of cases, especially proliferative LN" }
              ]
            }
          ]
        },
        {
          label: "Pathological classes (ISN/RPS)",
          children: [
            { label: "Class I — Minimal mesangial LN: normal glomeruli by LM; mesangial immune deposits by IF or EM" },
            { label: "Class II — Mesangial proliferative LN: mesangial hypercellularity and/or matrix expansion + mesangial immune deposits" },
            { label: "Class III — Focal proliferative LN: <50% of glomeruli involved" },
            { label: "Class IV — Diffuse proliferative LN: >50% of glomeruli involved" },
            { label: "Class V — Membranous LN: diffuse (global) capillary wall thickening + continuous subepithelial immune deposits" },
            { label: "Class VI — Advanced-stage LN: global glomerulosclerosis ≥90% of glomeruli, no active lesion" }
          ]
        },
        {
          label: "Clinical features",
          children: [
            { label: "Asymptomatic in many patients" },
            { label: "Hypertension — a clue of renal disease" },
            { label: "Symptoms & signs of: acute nephritis, nephrotic syndrome, rapidly progressive renal failure, and ESRD" }
          ]
        },
        {
          label: "Diagnosis",
          children: [
            { label: "Clinical: hypertension and/or renal edema" },
            { label: "Laboratory: urine exam (red cells, casts, proteinuria); elevated serum creatinine" },
            {
              label: "Renal biopsy",
              children: [
                { label: "Determine nature of renal pathology and pathological class" },
                { label: "Exclude other lesions complicating SLE: hypersensitivity interstitial nephritis (when patient develops ATN), pure antiphospholipid syndrome" },
                { label: "Assess activity index (0-24 score, acute & potentially treatable lesions) and chronicity index (0-12 score, irreversible lesions) → therapy & prognosis" }
              ]
            }
          ]
        },
        {
          label: "Management",
          children: [
            {
              label: "General (extra-renal manifestations affecting kidney)",
              children: [
                { label: "Hydroxychloroquine (or equivalent antimalarial) to all LN patients unless contraindicated" },
                { label: "Control of hypertension: target ≤120/80 mmHg" },
                { label: "Control of proteinuria: low-dose ACEIs or ARBs + protein restriction" },
                { label: "Control of hyperlipidemia: statins + low-fat diet" },
                { label: "Avoid nephrotoxic drugs e.g. NSAIDs; non-acetylated salicylates safe" },
                { label: "Avoid pregnancy in active LN (worsens renal disease; some medications teratogenic)" }
              ]
            },
            {
              label: "Specific (corticosteroids + immunosuppression)",
              children: [
                { label: "Divided into induction and maintenance phases" },
                { label: "Corticosteroids if clinically significant renal disease" },
                { label: "Immunosuppressives: cyclophosphamide, mycophenolate mofetil, azathioprine, or cyclosporine A" }
              ]
            }
          ]
        },
        {
          label: "Prognosis",
          children: [
            { label: "Classes I, II and V: generally good prognosis" },
            { label: "Classes III and IV: poor — tend to progress to ESRD, particularly class IV" },
            { label: "Class VI: hemodialysis or transplantation" }
          ]
        }
      ]
    },
    // ---------------- Topic 7 ----------------
    {
      label: "7. Diabetic Nephropathy",
      children: [
        {
          label: "Renal complications in diabetic patients",
          children: [
            { label: "Diabetic nephropathy (DN, diabetic glomerulosclerosis)" },
            { label: "Papillary necrosis" },
            { label: "UTI: asymptomatic bacteriuria, acute pyelonephritis, perinephric abscess" },
            { label: "Ischemic nephropathy due to renal artery atherosclerosis" },
            { label: "Hydronephrosis due to atonic bladder" },
            {
              label: "AKI secondary to",
              children: [
                { label: "Reaction to contrast (contrast nephropathy)" },
                { label: "UT obstruction secondary to papillary necrosis" }
              ]
            },
            { label: "NB: type 2 DM more common → most DN cases associated with type 2 DM" }
          ]
        },
        {
          label: "Definition",
          children: [
            { label: "Proteinuria with or without hypertension and renal impairment in DM of several years duration" }
          ]
        },
        {
          label: "Prevalence",
          children: [
            { label: "Type 1: ~30-50% develop DN (survive longer)" },
            { label: "Type 2: ~20% develop DN (usually die earlier)" }
          ]
        },
        {
          label: "Stages — Type 1 DM (5 stages)",
          children: [
            {
              label: "Stage I — Hyperfiltration / hypertrophy",
              children: [
                { label: "GFR ↑20-40% above age-matched controls" },
                { label: "Kidney hypertrophy on US" },
                { label: "Clinically may have polyuria" }
              ]
            },
            {
              label: "Stage II — Silent stage",
              children: [
                { label: "Normal GFR (most patients)" },
                { label: "Normal urinary albumin (<30 mg/day)" },
                { label: "Early structural renal damage" },
                { label: "~30-50% proceed to stage III" }
              ]
            },
            {
              label: "Stage III — Incipient nephropathy",
              children: [
                { label: "GFR starts to decline" },
                { label: "Microalbuminuria 30-300 mg/day (5-10 years after DM onset)" },
                { label: "Early hypertension or BP rise" }
              ]
            },
            {
              label: "Stage IV — Overt nephropathy",
              children: [
                { label: "Progressive GFR reduction" },
                { label: "Overt proteinuria >0.5 g/day" },
                { label: "Hypertension" }
              ]
            },
            {
              label: "Stage V — ESRD",
              children: [
                { label: "Requires RRT" },
                { label: "Other diabetic complications: retinopathy, neuropathy, CHF, cerebrovascular & peripheral vascular disease" }
              ]
            }
          ]
        },
        {
          label: "Stages — Type 2 DM",
          children: [
            { label: "Hyperfiltration stage rarely detected" },
            { label: "Microalbuminuria frequently present at diagnosis of DM" },
            { label: "Hypertension usually present at diagnosis of nephropathy" }
          ]
        },
        {
          label: "Pathology (3 major lesions)",
          children: [
            {
              label: "Glomerulosclerosis",
              children: [
                { label: "Diffuse: more common but non-specific" },
                { label: "Nodular: less common but pathognomonic" }
              ]
            },
            { label: "Chronic tubulo-interstitial nephritis" },
            { label: "Vasculitic lesions: arteriolosclerosis in afferent & efferent arterioles (pathognomonic for DM)" }
          ]
        },
        {
          label: "Pathogenesis (multifactorial)",
          children: [
            {
              label: "Hemodynamic",
              children: [
                { label: "Hyperglycemia → ↑GFR → ↑intraglomerular pressure → endothelial injury → glomerulosclerosis" }
              ]
            },
            {
              label: "Metabolic",
              children: [
                { label: "Hyperglycemia → glycosylation of mesangial & GBM proteins → trapping of circulating macromolecules → mesangial hyperplasia → altered GBM permeability" }
              ]
            },
            {
              label: "Genetic susceptibility",
              children: [
                { label: "Not all diabetic patients develop DN" }
              ]
            }
          ]
        },
        {
          label: "Risk factors for progression",
          children: [
            { label: "Proteinuria" },
            { label: "Hypertension" },
            { label: "Hyperglycemia" },
            { label: "Smoking" },
            { label: "High protein diet" },
            { label: "Genetic factors" }
          ]
        },
        {
          label: "Diagnosis",
          children: [
            {
              label: "Clinical",
              children: [
                { label: "DM ≥10 years duration with proteinuria ± HTN & renal insufficiency" },
                { label: "Presence of diabetic retinopathy strengthens diagnosis" }
              ]
            },
            {
              label: "Criteria of DN as cause of CKD",
              children: [
                { label: "Long-standing DM (≥10 years) before onset of CKD" },
                { label: "Normal-sized kidneys (by US)" },
                { label: "Presence of diabetic retinopathy" },
                { label: "Benign urinary sediment: no hematuria, no cellular casts" },
                { label: "Proteinuria still present when patient already started dialysis" }
              ]
            },
            {
              label: "Urine examination",
              children: [
                { label: "Proteinuria (micro- or macroalbuminuria)" }
              ]
            },
            {
              label: "Renal biopsy — needed if",
              children: [
                { label: "Duration of DM <10 years without retinopathy or neuropathy" },
                {
                  label: "Suspicion of alternative diagnosis",
                  children: [
                    { label: "Sudden onset of NS in early DM (<7 years type 1, <5 years type 2)" },
                    { label: "Renal insufficiency + active urinary sediment (red cells, cellular casts)" }
                  ]
                }
              ]
            }
          ]
        },
        {
          label: "Treatment",
          children: [
            {
              label: "Aim",
              children: [
                { label: "Slow progression by tight control of hyperglycemia, hypertension, UTI, and protein restriction" },
                { label: "RRT for ESRD diabetic patients" }
              ]
            },
            {
              label: "Control of hyperglycemia",
              children: [
                { label: "Insulin + proper diet" }
              ]
            },
            {
              label: "Control of hypertension (one of the most important factors)",
              children: [
                {
                  label: "Goals",
                  children: [
                    { label: "<130/80 mmHg in patients without proteinuria" },
                    { label: "<125/75 mmHg in patients with proteinuria" }
                  ]
                },
                {
                  label: "Drugs",
                  children: [
                    { label: "ACEI/ARBs" },
                    { label: "Diuretics in addition to ACEIs" },
                    { label: "CCB (non-dihydropyridine: verapamil & diltiazem)" },
                    { label: "β-blockers" },
                    { label: "Alpha-receptor antagonist e.g. prazosin" }
                  ]
                }
              ]
            },
            {
              label: "Control of UTI",
              children: [
                { label: "Proper antibiotic according to urine culture & sensitivity" }
              ]
            },
            {
              label: "Dietary protein restriction",
              children: [
                { label: "0.6-0.8 g/kg/day in patients with decreased GFR" }
              ]
            },
            {
              label: "RRT for ESRD patients",
              children: [
                { label: "Considered early at GFR <20 ml/min" }
              ]
            },
            {
              label: "N.B. — Insulin dosing",
              children: [
                { label: "Kidney metabolizes & excretes insulin → half-life prolonged with decreased GFR" },
                { label: "Decrease insulin dose in DN patients to avoid hypoglycemia" }
              ]
            }
          ]
        }
      ]
    }
  ]
};
