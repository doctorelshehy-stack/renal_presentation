// ============================================================
// Folder 04 — Electrolytes & Acid-Base
// Separate cards per common title (Definition / Causes /
// Classification / Clinical / Investigations / Treatment)
// ============================================================
const folderElectrolytes = {
  label: "04 · Electrolytes & Acid-Base",
  children: [
    // ---------------- Topic 14 ----------------
    {
      label: "14. Acid-Base Balance",
      children: [
        {
          label: "Overview of acid-base disturbances",
          children: [
            { label: "Metabolic acidosis: primary ↓HCO3 → ↓pH → ↑ventilation → ↓CO2 (respiratory compensation)" },
            { label: "Metabolic alkalosis: primary ↑HCO3 → ↑pH → ↓ventilation → ↑CO2 (respiratory compensation)" },
            { label: "Respiratory acidosis: primary CO2 retention → ↓pH → renal HCO3 retention (renal compensation)" },
            { label: "Respiratory alkalosis: primary CO2 loss → ↑pH → renal HCO3 excretion (renal compensation)" },
            {
              label: "Compensation summary",
              children: [
                { label: "Metabolic acidosis: pH↓, HCO3↓, CO2↓" },
                { label: "Metabolic alkalosis: pH↑, HCO3↑, CO2↑" },
                { label: "Respiratory acidosis: pH↓, HCO3↑, CO2↑" },
                { label: "Respiratory alkalosis: pH↑, HCO3↓, CO2↓" }
              ]
            }
          ]
        },
        {
          label: "Metabolic acidosis",
          children: [
            {
              label: "Definition",
              children: [
                { label: "Primary decrease in serum bicarbonate leading to low pH" }
              ]
            },
            {
              label: "Anion gap",
              children: [
                { label: "Principle of electro-neutrality: total cations = total anions" },
                { label: "AG = Na − (HCO3 + Cl)" },
                { label: "Increased AG: ↓unmeasured cations (hypokalemia) or ↑unmeasured anions (hyperphosphatemia)" },
                { label: "High AG acidosis: ↓HCO3 balanced by ↑unmeasured anions (AG ↑)" },
                { label: "Normal AG (hyperchloremic) acidosis: ↓HCO3 balanced by ↑Cl (AG normal)" }
              ]
            },
            {
              label: "Causes",
              children: [
                {
                  label: "Normal AG (hyperchloremic)",
                  children: [
                    { label: "GI HCO3 loss: diarrhea, pancreatic fistula, ureteral diversion" },
                    { label: "Renal HCO3 loss: proximal RTA (type II)" },
                    { label: "Failure of H+ secretion: distal RTA (type I)" },
                    { label: "Acid infusion: NH4Cl, hyperalimentation" }
                  ]
                },
                {
                  label: "High AG",
                  children: [
                    { label: "Ketoacidosis (diabetic, alcoholic, starvation)" },
                    { label: "Renal failure (uremic acidosis)" },
                    { label: "Lactic acidosis" },
                    { label: "Massive rhabdomyolysis" },
                    {
                      label: "Exogenous toxins",
                      children: [
                        { label: "Salicylate" },
                        { label: "Methanol" },
                        { label: "Ethylene glycol" },
                        { label: "Metformin" }
                      ]
                    }
                  ]
                }
              ]
            },
            {
              label: "Clinical features",
              children: [
                { label: "Symptoms: dyspnea; plus symptoms of underlying cause (DKA, CKD, drugs, stones)" },
                { label: "Signs: Kussmaul respiration; hypotension, arrhythmia, coma in severe cases" }
              ]
            },
            {
              label: "Investigations",
              children: [
                {
                  label: "General",
                  children: [
                    { label: "ABG: pH, HCO3, PCO2" },
                    { label: "Serum electrolytes: Na+, K+, Cl−" }
                  ]
                },
                {
                  label: "Specific (for cause)",
                  children: [
                    { label: "Renal functions" },
                    { label: "Blood glucose" },
                    { label: "Ketones" },
                    { label: "Lactate" },
                    { label: "Toxicology screen" }
                  ]
                }
              ]
            },
            {
              label: "Treatment",
              children: [
                { label: "Treat the underlying condition" },
                { label: "Alkali therapy when pH >7.20 needed: low HCO3 + PCO2 near physiological limit (~15); impending respiratory failure" },
                { label: "IV NaHCO3 for acute; deficit = (Desired HCO3 − Measured HCO3) × 0.5 × weight (kg)" },
                { label: "Oral NaHCO3 for chronic (e.g. RTA)" },
                { label: "Monitoring: HCO3/pH, Na+, volume status, PCO2" }
              ]
            }
          ]
        },
        {
          label: "Metabolic alkalosis",
          children: [
            {
              label: "Definition",
              children: [
                { label: "Primary increase in serum bicarbonate leading to high pH" }
              ]
            },
            {
              label: "Classification",
              children: [
                { label: "Chloride-responsive (urine Cl <20 mmol/L)" },
                { label: "Chloride-resistant (urine Cl >20 mmol/L)" },
                { label: "Other (alkali-loading)" }
              ]
            },
            {
              label: "Causes",
              children: [
                {
                  label: "Chloride-responsive",
                  children: [
                    { label: "Gastric loss: vomiting, nasogastric suction" },
                    { label: "Colonic loss: congenital chloridorrhea, villous adenoma" },
                    { label: "Volume depletion (contraction alkalosis)" },
                    { label: "Thiazides & loop diuretics (after discontinuation, secondary to volume depletion)" },
                    { label: "Cystic fibrosis" }
                  ]
                },
                {
                  label: "Chloride-resistant with hypertension",
                  children: [
                    { label: "Primary hyperaldosteronism" },
                    { label: "Cushing's syndrome" },
                    { label: "Exogenous steroid therapy" },
                    { label: "Liddle's syndrome" },
                    { label: "Renovascular hypertension" }
                  ]
                },
                {
                  label: "Chloride-resistant without hypertension",
                  children: [
                    { label: "Bartter's syndrome" },
                    { label: "Gitelman's syndrome" },
                    { label: "Severe K+ depletion" },
                    { label: "Current diuretic therapy (diuretics still active)" },
                    { label: "Hypomagnesemia" }
                  ]
                },
                {
                  label: "Other (alkali-loading)",
                  children: [
                    { label: "Exogenous alkali: antacids, bicarbonate infusion" },
                    { label: "Recovery of acidosis (renal overcorrection)" },
                    { label: "Milk-alkali syndrome" },
                    { label: "Hypercalcemia" },
                    { label: "Hypoalbuminemia" }
                  ]
                }
              ]
            },
            {
              label: "Clinical features",
              children: [
                { label: "History: GI loss, surgery, drugs, renal insufficiency" },
                { label: "Symptoms: hypoventilation, hypokalemia, hypocalcemia" },
                { label: "Signs: volume status assessment, tetany (Chvostek's & Trousseau's), mental changes, seizures" }
              ]
            },
            {
              label: "Investigations",
              children: [
                {
                  label: "General",
                  children: [
                    { label: "ABG: pH, HCO3, PCO2" },
                    { label: "Serum electrolytes: Na+, K+, Cl−, Ca2+, Mg2+" },
                    { label: "Urinary chloride" }
                  ]
                },
                {
                  label: "Specific (for chloride-resistant)",
                  children: [
                    { label: "Aldosterone, cortisol, renin" },
                    { label: "Renovascular imaging" }
                  ]
                }
              ]
            },
            {
              label: "Treatment",
              children: [
                {
                  label: "Chloride-responsive with volume depletion",
                  children: [
                    { label: "Isotonic NaCl + KCl replacement" }
                  ]
                },
                {
                  label: "Chloride-responsive with volume overload",
                  children: [
                    { label: "KCl + carbonic anhydrase inhibitors / K-sparing diuretics" }
                  ]
                },
                {
                  label: "Chloride-resistant",
                  children: [
                    { label: "Treat specific underlying cause" }
                  ]
                }
              ]
            }
          ]
        }
      ]
    },
    // ---------------- Topic 15 ----------------
    {
      label: "15. Hyponatremia",
      children: [
        {
          label: "Definition",
          children: [
            { label: "Serum Na+ <135 mmol/L" },
            { label: "Dilutional hyponatremia: water retention (most common)" },
            { label: "Pseudohyponatremia: spurious low Na+ due to ↑lipids/proteins" }
          ]
        },
        {
          label: "Pathological effects",
          children: [
            { label: "Water shifts from ECF to ICF" },
            { label: "Cell swelling" },
            { label: "Brain edema & neurologic manifestations" }
          ]
        },
        {
          label: "Clinical manifestations",
          children: [
            { label: "Manifestations of underlying cause" },
            {
              label: "Neurologic (from brain edema)",
              children: [
                { label: "Personality change, lethargy, confusion" },
                { label: "Stupor, hyperexcitability, hyperreflexia, seizures" },
                { label: "Coma, death" }
              ]
            }
          ]
        },
        {
          label: "Classification (true hyponatremia = hypotonic)",
          children: [
            { label: "Hypertonic (pseudohyponatremia): hyperglycemia, mannitol" },
            { label: "Isotonic (pseudohyponatremia): hyperlipidemia, hyperproteinemia" },
            {
              label: "Hypotonic (true hyponatremia)",
              children: [
                { label: "Hypervolemic" },
                { label: "Euvolemic" },
                { label: "Hypovolemic" }
              ]
            }
          ]
        },
        {
          label: "Causes",
          children: [
            {
              label: "Hypervolemic (total body Na+ ↑, water ↑↑)",
              children: [
                { label: "Heart failure" },
                { label: "Liver failure" },
                { label: "Oliguric AKI" },
                { label: "CKD" },
                { label: "Nephrotic syndrome" },
                { label: "Hypoalbuminemia" }
              ]
            },
            {
              label: "Euvolemic (total body Na+ normal, water ↑)",
              children: [
                { label: "SIADH" },
                { label: "Nephrogenic SIAD (drugs, malignancy, CNS disease)" },
                { label: "Primary polydipsia" },
                { label: "Thiazide diuretics" },
                { label: "Hypothyroidism" }
              ]
            },
            {
              label: "Hypovolemic (total body Na+ ↓, water ↓ less)",
              children: [
                {
                  label: "Extra-renal losses",
                  children: [
                    { label: "Vomiting, diarrhea, hemorrhage" },
                    { label: "Pancreatitis, burns" },
                    { label: "Third-space losses" }
                  ]
                },
                {
                  label: "Renal losses",
                  children: [
                    { label: "Diuretics (especially thiazides)" },
                    { label: "Adrenal insufficiency" },
                    { label: "Tubulointerstitial nephritis" },
                    { label: "AKI recovery phase (polyuric)" }
                  ]
                }
              ]
            }
          ]
        },
        {
          label: "Diagnostic algorithm",
          children: [
            {
              label: "Step 1: Plasma osmolality low → assess extracellular volume status",
              children: [
                {
                  label: "Increased EVS (hypervolemic)",
                  children: [
                    { label: "HF, cirrhosis, nephrosis" }
                  ]
                },
                {
                  label: "Normal EVS (euvolemic)",
                  children: [
                    { label: "Urine osmolality <100 → primary polydipsia" },
                    { label: "Urine osmolality >100 → SIADH, hypothyroidism, hypocortisolism" }
                  ]
                },
                {
                  label: "Decreased EVS (hypovolemic)",
                  children: [
                    { label: "GI losses, Addison's disease" },
                    { label: "Salt-losing nephritis, cerebral salt wasting" }
                  ]
                }
              ]
            },
            {
              label: "Step 2: Normal or high plasma osmolality",
              children: [
                { label: "Hyperglycemia (true hyponatremia with high osmolality)" },
                { label: "Pseudohyponatremia (spurious)" }
              ]
            }
          ]
        },
        {
          label: "Treatment",
          children: [
            { label: "Control symptoms then correct Na+" },
            { label: "Acute vs chronic; rate of correction (avoid osmotic demyelination / CPM)" },
            { label: "Fluid therapy per volume status" },
            { label: "Isotonic 0.9% NaCl (hypo/euvolemic)" },
            { label: "Hypertonic 3% NaCl + loop diuretics (hyper/euvolemic)" },
            {
              label: "Vasopressin antagonists",
              children: [
                { label: "Conivaptan" },
                { label: "Tolvaptan" }
              ]
            }
          ]
        }
      ]
    },
    // ---------------- Topic 16 ----------------
    {
      label: "16. Hypernatremia",
      children: [
        {
          label: "Definition",
          children: [
            { label: "Serum Na+ >145 mmol/L" },
            { label: "Always hypertonic → water shifts from ICF to ECF" },
            { label: "Cell shrinkage (brain shrinkage → vascular rupture, seizures, coma)" }
          ]
        },
        {
          label: "Causes",
          children: [
            {
              label: "Water loss (most common)",
              children: [
                {
                  label: "Extra-renal",
                  children: [
                    { label: "Insensible losses: fever, hyperventilation, burns" },
                    { label: "Inadequate intake: impaired thirst, unconscious, no access" }
                  ]
                },
                {
                  label: "Renal",
                  children: [
                    { label: "Diabetes insipidus: central (ADH deficiency) / nephrogenic (ADH resistance)" },
                    { label: "Osmotic diuresis: hyperglycemia, mannitol" },
                    { label: "Diuretic therapy" }
                  ]
                }
              ]
            },
            {
              label: "Sodium gain",
              children: [
                { label: "Hypertonic saline infusion" },
                { label: "Sodium bicarbonate infusion" },
                { label: "Salt poisoning" },
                { label: "Mineralocorticoid excess (hyperaldosteronism, Cushing's)" }
              ]
            }
          ]
        },
        {
          label: "Clinical features",
          children: [
            { label: "Thirst (early)" },
            { label: "Neurologic: irritability, weakness, lethargy, confusion, seizures, coma" },
            { label: "Signs of volume status (depending on cause)" }
          ]
        },
        {
          label: "Investigations",
          children: [
            { label: "Serum Na+, osmolality" },
            { label: "Urine osmolality, urine Na+" },
            { label: "Volume status assessment" },
            { label: "Water deprivation test (for DI)" }
          ]
        },
        {
          label: "Treatment",
          children: [
            { label: "Correct free water deficit slowly (avoid cerebral edema)" },
            { label: "Formula: water deficit = 0.6 × weight × (1 − 140/Na+)" },
            { label: "Hypovolemic: isotonic saline first → then free water" },
            { label: "Euvolemic: free water (oral/D5W)" },
            { label: "Hypervolemic: loop diuretics + free water" },
            { label: "Diabetes insipidus: desmopressin (central); thiazides + low solute diet (nephrogenic)" }
          ]
        }
      ]
    },
    // ---------------- Topic 17 ----------------
    {
      label: "17. Hyperkalemia",
      children: [
        {
          label: "Definition",
          children: [
            { label: "Serum K+ >5.0 mmol/L" },
            { label: "Pseudohyperkalemia: hemolysis, thrombocytosis, leukocytosis, fist clenching" }
          ]
        },
        {
          label: "Causes",
          children: [
            {
              label: "Increased release from cells",
              children: [
                { label: "Tissue breakdown: rhabdomyolysis, tumor lysis, hemolysis, burns, trauma" },
                { label: "Acidemia (↑H+ enters cells → K+ exits)" },
                { label: "Hyperosmolality (hyperglycemia)" },
                { label: "Insulin deficiency" },
                { label: "β-blockers" },
                { label: "Digitalis toxicity" },
                { label: "Succinylcholine (in denervation, burns, neuromuscular disease)" }
              ]
            },
            {
              label: "Reduced excretion",
              children: [
                { label: "CKD (most common)" },
                { label: "AKI" },
                { label: "Hypoaldosteronism: primary (Addison's), secondary (hyporeninemic), pseudohypoaldosteronism" },
                { label: "Drugs: ACEI/ARB, K-sparing diuretics, NSAIDs, cyclosporine, tacrolimus, heparin, trimethoprim, pentamidine" },
                { label: "Type 4 RTA" }
              ]
            }
          ]
        },
        {
          label: "Clinical features",
          children: [
            { label: "Muscle weakness, flaccid paralysis" },
            { label: "Cardiac: peaked T waves, prolonged PR, widened QRS, sine wave, VF/asystole" },
            { label: "Paresthesias" }
          ]
        },
        {
          label: "Investigations",
          children: [
            { label: "ECG (essential)" },
            { label: "Serum K+, creatinine, pH, glucose" },
            { label: "Urine K+, osmolality, pH" },
            { label: "Drug review" }
          ]
        },
        {
          label: "Treatment",
          children: [
            {
              label: "Emergency (ECG changes / K+ >6.5)",
              children: [
                { label: "IV Ca gluconate 10% 10 ml → membrane stabilization (cardiac)" },
                { label: "IV insulin 10 units + 50 ml 50% dextrose → shift K+ into cells" },
                { label: "Nebulized salbutamol 10-20 mg → shift K+ into cells" },
                { label: "NaHCO3 (if acidemia) → shift K+ into cells" }
              ]
            },
            {
              label: "Potassium removal",
              children: [
                { label: "Loop diuretics (if urine output)" },
                { label: "Cation exchange resins (sodium polystyrene sulfonate, patiromer, SZC)" },
                { label: "Dialysis (definitive; if severe, refractory, or renal failure)" }
              ]
            },
            {
              label: "General measures",
              children: [
                { label: "Stop K+-retaining drugs" },
                { label: "Low K+ diet" },
                { label: "Treat underlying cause" }
              ]
            }
          ]
        }
      ]
    },
    // ---------------- Topic 18 ----------------
    {
      label: "18. Hypokalemia",
      children: [
        {
          label: "Definition",
          children: [
            { label: "Serum K+ <3.5 mmol/L" },
            { label: "Pseudohypokalemia: leukocytosis (cells consume K+ in vitro)" }
          ]
        },
        {
          label: "Causes",
          children: [
            {
              label: "Reduced intake",
              children: [
                { label: "Starvation, anorexia" }
              ]
            },
            {
              label: "Increased cellular uptake",
              children: [
                { label: "Alkalemia" },
                { label: "Insulin" },
                { label: "β-agonists" },
                { label: "Barium poisoning" },
                { label: "Familial hypokalemic periodic paralysis" }
              ]
            },
            {
              label: "Increased losses (most common)",
              children: [
                {
                  label: "Renal losses",
                  children: [
                    { label: "Diuretics: thiazides, loops (most common cause)" },
                    { label: "Mineralocorticoid excess: primary / secondary hyperaldosteronism, Cushing's, exogenous steroids, licorice" },
                    { label: "Renal tubular acidosis: type 1 (distal), type 2 (proximal)" },
                    { label: "Magnesium deficiency (impairs K+ conservation)" },
                    { label: "Osmotic diuresis: hyperglycemia, mannitol" },
                    { label: "Penicillin (high dose, carbenicillin)" },
                    { label: "Bartter's, Gitelman's, Liddle's syndromes" }
                  ]
                },
                {
                  label: "Extra-renal losses",
                  children: [
                    { label: "GI: vomiting, diarrhea, laxative abuse, villous adenoma" },
                    { label: "Sweating (prolonged, hot climate)" },
                    { label: "Dialysis (especially PD)" }
                  ]
                }
              ]
            }
          ]
        },
        {
          label: "Clinical features",
          children: [
            { label: "Muscle weakness, fatigue, cramps, paralysis (ascending)" },
            { label: "Ileus, constipation" },
            { label: "Polyuria (nephrogenic DI), polydipsia" },
            { label: "Cardiac: flattened T, ST depression, U waves, arrhythmias (esp. with digitalis)" },
            { label: "Rhabdomyolysis (severe <2.5)" }
          ]
        },
        {
          label: "Investigations",
          children: [
            { label: "ECG" },
            { label: "Serum K+, Mg2+, creatinine, pH" },
            { label: "Urine K+ (spot or 24h): <20 → extra-renal; >20 → renal" },
            { label: "Acid-base status" },
            { label: "Drug review" }
          ]
        },
        {
          label: "Treatment",
          children: [
            { label: "Treat underlying cause" },
            { label: "Stop offending drugs" },
            { label: "Mg2+ repletion (essential; hypokalemia refractory if Mg2+ low)" },
            {
              label: "Potassium replacement",
              children: [
                { label: "Oral KCl (preferred): 20-40 mmol per dose, max 100 mmol/day" },
                { label: "IV KCl: max 10 mmol/h (peripheral), 20-40 mmol/h (central, cardiac monitoring)" },
                { label: "K-sparing diuretics (spironolactone, amiloride, triamterene)" },
                { label: "KCl in IV fluids: max 40 mmol/L" }
              ]
            },
            { label: "Monitor ECG & serum K+ frequently" }
          ]
        }
      ]
    }
  ]
};