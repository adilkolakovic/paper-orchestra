# Experimental Log: Causal ML Evaluation of Child Allowance (Serbia)

## 1. Study Metadata & Institutional Setup

* **Project:** Expression of Interest — Serbia: Causal Machine Learning (Policy AI Optimization Center for Children)
* **Evaluated Policy:** Child Allowance (*Dečiji dodatak*), regulated by the Law on Financial Support to Families with Children
* **Consortium:** Statistical Office of the Republic of Serbia (SORS), Republic Institute for Social Protection, and UNICEF
* **Unit of Observation:** Individual single parent and linked child(ren) observed longitudinally across administrative registries, aggregated to socio-demographic cluster and municipal levels
* **Temporal Scope:**
  * **Historical Baseline Window:** 2015–2026 (11-year vital statistics history for pre-treatment profiling)
  * **Treatment & Outcome Panel Window:** 2022–2026 (benefit transactions, employment trajectories, and educational outcomes)

---

## 2. Dataset Architecture & Cohort Construction (Completed)

### 2.1 Linked Administrative Data Sources

| Registry / Source | Custodian | Coverage | Key Variables & Role in Pipeline |
| :--- | :--- | :--- | :--- |
| **Vital Statistics (`DEM-01`, `DEM-02`, `RB-1`)** | SORS | 2015–2026 | Births, deaths, and divorces; used to deterministically identify single-parent households and construct pre-treatment family history. |
| **Child Allowance Registry (`ExportDD`)** | MoLEVSA | 2022–2026 | Binary and longitudinal treatment indicator ($T \in \{0, 1\}$), benefit duration, and payment episodes. |
| **Social Card & Benefit Registries (`ExportNSP`, `ExportRD`)** | MoLEVSA | 2022–2026 | Financial Social Assistance (`FSA` / `NSP`) receipt, Birth Grant (`RD`) receipt (3rd/4th child income-test interaction), and household poverty indicators. |
| **Mandatory Social Insurance (`CROSO`) & Municipal Stats** | CROSO / SORS | 2022–2026 | Formal employment status, monthly contribution continuity, industry (`NACE`) codes, and municipal average wages. |
| **Education Information System (`EIS-JISP`)** | Ministry of Education | 2022–2026 | Student enrollment, attendance compliance, grade progression/retention, primary/secondary completion, and early dropout records. |

### 2.2 Analytical Sample & Treatment Assignment Summary

Deterministic record linkage across SORS Vital Statistics and MoLEVSA benefit registries yielded the following analytical cohort:

* **Total Identified Single-Parent Cohort ($N$):** $75,342$ households
* **Treated Group ($N_1$, Confirmed CA Beneficiaries, 2022–2026):** $15,193$ ($20.17\%$)
* **Control Pool ($N_0$, Non-Recipient Single Parents):** $60,149$ ($79.83\%$)
* **Control-to-Treated Ratio:** $3.96:1$ ($\approx 4:1$), providing dense covariate coverage and strong common support across regional and socio-demographic strata.

---

## 3. Outcome Operationalization

1. **Primary Outcome Domain A — Labor Market Dynamics (`CROSO`):**
   * $Y^{(1a)}$: Binary transition probability from economic inactivity/unemployment at baseline ($t_0$) to formal employment within $t_0 + 24$ months.
   * $Y^{(1b)}$: Cumulative months of continuous mandatory social security contributions over a 24-month follow-up panel.
2. **Primary Outcome Domain B — Poverty Mitigation & Non-Dependency (`MoLEVSA`):**
   * $Y^{(2a)}$: Probability of household entry into extreme poverty requiring Financial Social Assistance (`FSA` / `NSP`).
   * $Y^{(2b)}$: Reduction in the estimated household poverty gap relative to statutory thresholds.
3. **Secondary Outcome Domain C — Child Educational Attainment (`EIS-JISP`):**
   * $Y^{(3a)}$: Primary and secondary school on-time completion rates.
   * $Y^{(3b)}$: Annual grade retention / repetition rates.
   * $Y^{(3c)}$: Early school dropout incidence among school-aged children in beneficiary vs. non-beneficiary households.

---

## 4. Experimental Pipeline & Model Configurations

### Stage 1: Unsupervised Socio-Demographic Stratification (`EXP-01`)
* **Objective:** Partition single-parent households into structurally homogeneous clusters prior to causal estimation to eliminate functional-form misspecification across categorical covariates.
* **Distance Metric:** Gower dissimilarity coefficient $d_G(i, j) \in [0, 1]$ handling mixed numeric and categorical administrative attributes.
* **Clustering Algorithm:** K-Prototypes clustering.
* **Baseline Covariate Set ($X_{\text{pre}}$):** Parental age, gender, highest educational attainment code, pre-treatment employment history, number and age distribution of children, single-parenthood pathway (divorce `RB-1`, widowhood `DEM-02`, unmarried birth `DEM-01`), municipal code, and local average wage tier.
* **Hyperparameter Grid & Selection Criteria:**
  * Candidate cluster counts: $k \in \{3, 4, 5, 6, 7, 8, 9, 10\}$
  * Categorical weight balancing parameter: $\gamma \in \{0.5, 1.0, 1.5, 2.0\}$
  * Selection metrics: Average Silhouette width, cluster stability via bootstrap resampling, and minimum cluster size constraint ($n_c \ge 1,000$ with at least $15\%$ treated share per cluster).

### Stage 2: Within-Cluster Double-Robust Causal Estimation (`EXP-02` & `EXP-03`)
* **Objective:** Estimate within-cluster $\text{ATE}_c$, overall population-weighted $\text{ATE}$, and conditional heterogeneous treatment effects $\text{CATE}(x) = \mathbb{E}[Y(1) - Y(0) \mid X = x]$.
* **Estimator A — Causal Forests (Generalized Random Forests / `GRF`):**
  * Splitting criterion: Maximize treatment effect heterogeneity ($\tau$-heterogeneity) with honesty splitting (separate subsamples for tree structure and leaf estimation).
  * Configuration: `num.trees = 2000`, `min.node.size = 50`, `sample.fraction = 0.5`, honest fraction $= 0.5$, tuning enabled for `mtry` and `alpha`.
* **Estimator B — Double Machine Learning (`DML`):**
  * Formulation: Interactive Regression Model (IRM) for binary treatment $T \in \{0, 1\}$ with Neyman-orthogonal score functions.
  * Nuisance Learners: Gradient Boosted Decision Trees (`LightGBM` / `XGBoost`) and Random Forests for outcome regressions $\hat{\mu}_0(X), \hat{\mu}_1(X)$ and propensity score $\hat{e}(X) = \mathbb{P}(T = 1 \mid X)$.
  * Sample Splitting: $K$-fold cross-fitting ($K = 5$) stratified by cluster and treatment status.

### Stage 3: Policy Targeting & Subgroup Heterogeneity Analysis (`EXP-04`)
* **Heterogeneity Dimensions:**
  * Parental education level and baseline attachment to formal labor (`CROSO`).
  * Household size and birth-order eligibility interactions (specifically assessing the 3rd- and 4th-child birth grant income inclusion rule).
  * Regional development tier and municipal unemployment/wage context.
* **Policy Simulation:** Compare observed targeting efficiency against counterfactual eligibility rules (e.g., excluding birth grants from the means test or adjusting per-capita income thresholds).

---

## 5. Validation, Identification Checks & Sensitivity Protocol (`EXP-05`)

* **Overlap / Positivity Diagnostic:** Verify propensity score support within every cluster $c$, trimming extreme observations outside $\hat{e}(x) \in [0.05, 0.95]$ if necessary and comparing trimmed vs. untrimmed estimates.
* **Covariate Balance Check:** Require Standardized Mean Differences $\text{SMD} < 0.10$ across all baseline covariates after inverse probability / forest weighting within each cluster.
* **Placebo / Falsification Tests:** Estimate pseudo-treatment effects on pre-treatment employment and social assistance trajectories (2019–2021) prior to 2022–2026 CA enrollment; expect $\hat{\tau}_{\text{placebo}} \approx 0$.
* **Unobserved Confounding Sensitivity:** Compute Rosenbaum sensitivity bounds and omitted variable bias benchmarks (Calibrated against strong observed predictors such as municipal wage tier and baseline education).

---

## 6. Experiment Execution Log

| Run ID | Experiment Stage | Scope & Method | Status | Recorded Outputs & Notes |
| :--- | :--- | :--- | :--- | :--- |
| **`EXP-00`** | Cohort Extraction & Multi-Registry Linkage | SORS (`DEM-01`, `DEM-02`, `RB-1`) + MoLEVSA (`ExportDD`, `ExportNSP`, `ExportRD`) + CROSO + EIS-JISP | **Completed** | Linked $N = 75,342$ single parents ($N_1 = 15,193$ treated; $N_0 = 60,149$ control; ratio $3.96:1$). Full panel structured for 2015–2026 baseline and 2022–2026 outcomes. |
| **`EXP-01`** | Unsupervised Socio-Demographic Stratification | Gower Distance + K-Prototypes ($k \in \{3,\dots,10\}$) on pre-treatment baseline $X_{\text{pre}}$ | **Configured / Pending** | Optimal $k^*$ and cluster profiles to be logged upon execution on SORS secure environment. |
| **`EXP-02`** | Within-Cluster Causal Forest Estimation | Honest GRF (`2000` trees) per cluster across primary (`CROSO`, `FSA`) and secondary (`EIS-JISP`) outcomes | **Configured / Pending** | Will output cluster-specific $\text{ATE}_c$, $\text{CATE}(x)$ distributions, and variable importance for treatment heterogeneity. |
| **`EXP-03`** | Double Machine Learning (`DML`) Benchmark | 5-fold cross-fitted IRM (`LightGBM` / `RF` nuisance learners) per cluster | **Configured / Pending** | Cross-estimator consistency check against Causal Forest $\text{ATE}$ / $\text{CATE}$ estimates. |
| **`EXP-04`** | Subgroup Heterogeneity & Policy Counterfactuals | HTE decomposition by education, region, and birth-grant income inclusion | **Configured / Pending** | Policy simulations for MoLEVSA and UNICEF targeting and adequacy recommendations. |
| **`EXP-05`** | Diagnostics, Placebo & Sensitivity Suite | Overlap ($\hat{e}(x)$), $\text{SMD} < 0.10$, 2019–2021 pre-trend placebo, Rosenbaum bounds | **Configured / Pending** | Mandatory robustness verification prior to policy brief publication. |