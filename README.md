# PD Model Validation Tool: The Jeffrey’s Test Framework

This repository provides a professional Python implementation of the **Jeffrey’s Test**, a Bayesian calibration tool specifically designed for the backtesting of **Probability of Default (PD)** models. 

This framework is built to align with the **ECB (European Central Bank)** and **EBA (European Banking Authority)** requirements for Internal Rating-Based (IRB) systems.

---

## Regulatory Context & Compliance

### 1. ECB Validation Reporting (Chapter 2.5.3)
In accordance with the **ECB Instructions on Validation Reporting (Section 2.5.3 - Predictive Ability)**, banks are required to demonstrate that their PD estimates are accurate predictors of realized default rates. For **Low-Default Portfolios (LDP)**, where traditional frequentist tests (like the Binomial Test) lack statistical power, the ECB allows for alternative robust methodologies. This tool bridges that gap by providing a Bayesian significance test.

### 2. Supervisory Guide 2025 & EBA/GL/2017/16
The **ECB Supervisory Guide 2025** and **EBA Guidelines** emphasize the principle of **Prudence**. Where data is scarce, models must incorporate a **Margin of Conservatism (MoC)**. The Jeffrey’s Test is a standard-of-practice for:
* **Quantifying Underestimation:** Measuring the probability that the realized default rate exceeds the PD estimate.
* **Rating Grade Analysis:** Validating calibration at a granular "Rating Bucket" level, as expected during On-Site Inspections (OSI).

---

## Statistical Rationale: Why Jeffrey’s Test?

The Jeffrey’s Test utilizes a **Non-informative Prior** based on the $Beta(0.5, 0.5)$ distribution. This approach has critical implications for PD validation:

* **Handling Zero Defaults:** In portfolios with zero realized defaults, frequentist models often fail to provide a meaningful p-value. Jeffrey’s Prior effectively assumes a "0.5 default" baseline, preventing the collapse of the statistical inference.
* **Posterior PDF:** By updating the Prior with observed data ($D$ defaults, $N$ non-defaults), we obtain a **Posterior Beta Distribution**:
  $$P(\text{PD} | \text{Data}) \sim Beta(D + 0.5, N - D + 0.5)$$
* **One-Tailed Significance:** The test focuses on the "right tail" of the distribution to identify if the model is systematically underestimating risk—the primary concern for financial regulators.



---

## Features & Methodology

### Traffic Light System (TLS)
The tool categorizes validation results into a three-zone system based on the p-value:
* **🟢 Green (p > 0.05):** The model is well-calibrated or conservative.
* **🟡 Yellow (0.01 < p ≤ 0.05):** Monitoring is required; potential calibration drift.
* **🔴 Red (p ≤ 0.01):** Significant underestimation. Immediate recalibration or MoC adjustment required.

### Technical Implementation
* **Language:** Python 3.x
* **Key Libraries:** `scipy.stats` (Beta distribution), `matplotlib` (HD visualization), `pandas` (Reporting).
* **Environment:** Optimized for Google Colab with interactive forms.

---

## Visualizing Results
The tool generates a high-definition PDF/PNG report showing the **Posterior Density Function**. This visual aid helps validators understand the "safety margin" between the model's PD and the critical rejection threshold.

![Validation Plot](validazione_Portafoglio_Mutui_Retail.png)

---

## Usage
1. Clone the repository.
2. Run the `jeffreys_test.py` script.
3. Input your Portfolio Segment, Defaults, Non-defaults, and Model PD.
4. Export the HD report for your Validation Document.

---
**Author:** Vittorio Pasculli 
**Domain:** Risk Management | Credit Model Validation | Quantitative Finance
