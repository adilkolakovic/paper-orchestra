# Project Idea and Contributions: Causal Machine Learning Evaluation of Serbia's Child Allowance Programme

## 1. Core Idea & Policy Motivation

### Background & Empirical Puzzle
Serbia's **Child Allowance (CA)** is a non-contributory, means-tested cash transfer governed by the *Law on Financial Support to Families with Children* (Official Gazette of RS Nos. 113/2017, 50/2018, and 46/2021). Administered locally by municipal and city child protection services and funded by the central budget, its core objective is to alleviate poverty among low-income families with children.

Since 2014—and particularly following the 2017/2018 legislative amendments—the number of Child Allowance beneficiaries has experienced a steep, sustained decline. Potential drivers include:
* **Regulatory tightening:** Exclusion of foster families from eligibility and inclusion of third- and fourth-child birth grants in the household income assessment.
* **Administrative enforcement:** Enhanced automated cross-checks against property cadaster registries (enforcing the 2-hectare land per member and housing size ceilings) alongside school attendance and vaccination conditionalities.
* **Macro-demographic shifts:** Rising nominal/real wages relative to indexed income thresholds and overall child population decline.

Despite major structural shifts in programme coverage, **no rigorous causal impact evaluation** has been conducted to measure how Child Allowance affects household welfare, labor supply, or child development, nor how these effects vary across vulnerable subgroups.

### Proposed Identification & Modeling Idea
To overcome confounding and functional form misspecification in observational administrative data, this project proposes a **two-step non-parametric Causal Machine Learning (Causal ML) framework** tailored to high-dimensional, predominantly categorical registry data:

1. **Target Population Isolation (Single-Parent Design):** The study restricts the analytical cohort to **single-parent households** ($N = 75,342$). Focusing on single mothers and fathers removes unobserved intra-household income and labor-supply noise from a second cohabiting parent, creating a clean, well-identified quasi-experimental setting.
2. **Step 1 — Unsupervised Socio-Demographic Stratification:** Rather than imposing linear or parametric specifications on high-dimensional categorical variables (municipalities, education levels, industry codes, family structure), households are first partitioned into homogeneous socio-demographic profiles using mixed-data clustering (**Gower dissimilarity** and **K-Prototypes**).
3. **Step 2 — Within-Cluster Double-Robust Causal Estimation:** Within each stratified cluster, double-robust Causal ML estimators (**Causal Forests** and **Double Machine Learning**) compare Child Allowance recipients ($N_1 = 15,193$) against non-recipient single parents ($N_0 = 60,149$) with near-identical pre-treatment covariates to estimate both Average Treatment Effects ($\text{ATE}$) and Conditional Average Treatment Effects ($\text{CATE}$).

---

## 2. Key Contributions

1. **Methodological Contribution (Non-Parametric Causal ML for Categorical Administrative Data):**
   * Demonstrates how coupling unsupervised mixed-data clustering (Gower distance / K-Prototypes) with double-robust estimators (Causal Forests and DML) eliminates parametric functional-form bias and guarantees local common support across complex administrative registries.
2. **Data Infrastructure Contribution (Multi-Registry Longitudinal Linkage):**
   * Establishes a unified longitudinal analytical dataset linking an 11-year vital statistics baseline (2015–2026) with social protection, mandatory social insurance, and national education registries (2022–2026), achieving a gold-standard $\approx 4:1$ control-to-treated ratio ($60,149$ controls vs. $15,193$ treated).
3. **Policy & Equity Contribution (Actionable Targeting & Adequacy Evidence):**
   * Quantifies potential work-disincentive versus labor-enabling effects in formal employment, assesses prevention of extreme poverty (entry into Financial Social Assistance), and measures intergenerational returns via children's school retention and completion—directly informing legislative reforms on eligibility thresholds, adequacy, and child-sensitive social protection for the Government of Serbia and UNICEF.

---

## 3. Research Questions & Outcome Dimensions

* **Primary Policy Question:** What are the average ($\text{ATE}$) and heterogeneous ($\text{CATE}$) causal effects of Child Allowance on vulnerable single-parent households in Serbia regarding parental formal employment, social assistance dependency, and child educational attainment?
* **Heterogeneity Sub-Questions:**
  1. *Household Profiles:* How do treatment effects vary by parental education, baseline employment status, household size, and family composition?
  2. *Spatial & Labor Market Context:* How do municipal wage levels and local labor market conditions moderate programme effectiveness?
  3. *Human Capital Investment:* Does Child Allowance receipt improve primary/secondary school completion and reduce grade repetition and early dropout?
  4. *Equity & Targeting Efficiency:* Are the most socio-economically vulnerable children reached equally, and where do exclusion errors or benefit adequacy gaps occur?