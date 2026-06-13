# Industrial Risk Analysis Project Log

## Project Overview

### Initial Project Directions

The project initially explored multiple potential themes:

1. Industrial Risk Assessment Analytics
2. Security Control Effectiveness Dashboard
3. Cyber-Physical Incident Analysis Repository

After investigating the available datasets, the project evolved into:

> Statistical Analysis and Anomaly Detection of Cyber Incident Impacts using Operational, Financial, and Market Data.

---

# Dataset Investigation Phase

## Available Datasets

Three primary datasets were identified.

### Incident Master Dataset

**Records:** 850

**Contains:**
- Company information
- Industry classification
- Attack vectors
- Downtime information
- Data compromise information
- Attribution information
- Quality indicators

**Purpose:**
Operational Impact Analysis

---

### Financial Impact Dataset

**Records:** 778

**Contains:**
- Direct losses
- Recovery costs
- Legal fees
- Regulatory fines
- Insurance payouts
- Total losses

**Purpose:**
Financial Impact Analysis

---

### Market Impact Dataset

**Records:** 358

**Contains:**
- Abnormal returns
- CAR metrics
- Trading volume metrics
- Volatility metrics
- Recovery periods

**Purpose:**
Market Impact Analysis

---

# Initial Challenges

## Severity Measurement Problem

### Question

How can severity be quantified?

### Initial Idea

Use financial loss as a severity metric.

### Issue

Financial loss information had not yet been validated.

### Resolution

The Financial Impact Dataset was later discovered and validated.

Severity can now be quantified using:

- Total Loss (`total_loss_usd`)
- Direct Loss (`direct_loss_usd`)
- Recovery Cost (`recovery_cost_usd`)
- Legal Fees (`legal_fees_usd`)
- Regulatory Fines (`regulatory_fine_usd`)

---

# Statistical Methodology Discussions

## Mean vs Median

### Question

Can the mean be used as a threshold for extreme losses?

### Conclusion

Not by itself.

### Reason

Cyber incident losses are highly skewed due to a small number of catastrophic events.

---

## Median + IQR

### Recommendation

Use:

- Median
- Quartiles
- Interquartile Range (IQR)

### Purpose

Severity Classification

### Justification

More robust against extreme outliers.

---

## Mean + Standard Deviation

### Recommendation

Use alongside Median + IQR.

### Purpose

Anomaly Detection

Formula:

\[
z = \frac{x-\mu}{\sigma}
\]

### Interpretation

- \|z\| > 2 → Unusual Incident
- \|z\| > 3 → Highly Anomalous Incident

---

# Dataset Validation Phase

## Initial Concern

Some Incident IDs may exist in Financial or Market datasets but not in the Incident Master dataset.

### Validation Method

Python Set Operations:

```python
incident_ids = set(incident_df["incident_id"])
financial_ids = set(financial_df["incident_id"])
market_ids = set(market_df["incident_id"])
```

---

## Validation Results

### Financial Dataset

```text
Unique in Financial: 0
```

**Conclusion:**

All Financial records exist in the Incident Master dataset.

---

### Market Dataset

```text
Unique in Market: 0
```

**Conclusion:**

All Market records exist in the Incident Master dataset.

---

### Common Records

```text
Common Across All Three Datasets: 329
```

**Conclusion:**

329 incidents contain:

- Operational Data
- Financial Data
- Market Data

simultaneously.

---

# Dataset Relationship Mapping

Final hierarchy:

```text
Incident Master (850)
│
├── Financial Impact (778)
│
└── Market Impact (358)
```

Intersection:

```text
Incident ∩ Financial ∩ Market = 329
```

---

# Major Methodological Decision

## Rejected Approach

### Single Unified Dataset Only

Reason:

Would discard large amounts of valid information.

---

## Accepted Approach

### Phase 1 — Individual Dataset Analyses

#### Analysis A — Incident Master Dataset

**Sample Size:** 850

**Focus:**
- Industry Analysis
- Attack Vector Analysis
- Downtime Analysis
- Data Compromise Analysis
- Incident Trend Analysis

**Goal:**

Understand operational characteristics of cyber incidents.

---

#### Analysis B — Financial Impact Dataset

**Sample Size:** 778

**Focus:**
- Direct Losses
- Recovery Costs
- Legal Fees
- Regulatory Fines
- Total Losses

**Goal:**

Understand financial consequences of cyber incidents.

---

#### Analysis C — Market Impact Dataset

**Sample Size:** 358

**Focus:**
- Abnormal Returns
- CAR Metrics
- Recovery Periods
- Trading Volume Reactions

**Goal:**

Understand investor and market reactions.

---

### Phase 2 — Comparative Analysis

**Sample Size:** 329

**Focus:**

Relationships between:

```text
Operational Impact
        ↓
Financial Impact
        ↓
Market Impact
```

Potential Questions:

- Do larger breaches generate larger losses?
- Do larger losses generate stronger market reactions?
- Does downtime affect stock-price recovery?
- Which incidents are anomalous across multiple dimensions?

---

# Exploratory Statistical Findings

## Incident + Financial Merge

### Merge Result

```text
778 rows
50 columns
```

### Interpretation

The merge was successful and retained all Financial Impact records.

---

## Distribution Analysis

### Total Loss (USD)

| Statistic | Value |
|------------|------------:|
| Mean | 70.99M |
| Median | 16.56M |
| Maximum | 3.45B |

**Finding:**

Strong positive skew.

---

### Data Compromised Records

| Statistic | Value |
|------------|------------:|
| Mean | 2.87M |
| Median | 56K |
| Maximum | 549.7M |

**Finding:**

Extremely positively skewed.

---

### Downtime Hours

| Statistic | Value |
|------------|------------:|
| Mean | 110.4 |
| Median | 54.4 |
| Maximum | 1951.6 |

**Finding:**

Strong positive skew.

---

# Methodological Implications

## Conclusion

Median + IQR is justified.

### Evidence

Across all major impact variables:

- Mean >> Median
- Extreme maximum values exist
- Strong right-skew is present

---

# Draft Severity Framework

## Financial Severity

**Variable:**

```text
total_loss_usd
```

| Severity | Rule |
|-----------|-----------|
| Low | ≤ Median |
| Moderate | Median–Q3 |
| High | > Q3 |
| Extreme | > Q3 + 1.5×IQR |

---

## Operational Severity

**Variable:**

```text
downtime_hours
```

Same classification framework.

---

## Data Breach Severity

**Variable:**

```text
data_compromised_records
```

Same classification framework.

---

# Python vs Excel Discussion

## Python

Use for:

- Descriptive Statistics
- Correlation Analysis
- Filtering
- Grouping
- Severity Classification
- Anomaly Detection
- Reproducible Analysis

Expected Usage:

```text
90%
```

---

## Excel

Use for:

- Spot Checking
- Data Validation
- Outlier Investigation
- Reviewing Notes
- Contextual Analysis

Expected Usage:

```text
10%
```

---

# Attack Vector Analysis Strategy

## Recommended Workflow

### Python First

Examples:

```python
value_counts()
groupby()
describe()
```

### Metrics

- Frequency Distributions
- Average Downtime by Attack Vector
- Median Downtime by Attack Vector
- Severity by Attack Vector

---

### Excel Second

Use for:

- Inspecting unusual incidents
- Reading notes
- Investigating extreme downtime events
- Validating suspicious records

---

# Project Structure Recommendation

```text
project/
│
├── datasets/
│
├── analysis/
│   ├── incident_analysis.py
│   ├── financial_analysis.py
│   ├── market_analysis.py
│   └── comparative_analysis.py
│
├── utils/
│   └── loader.py
│
└── main.py
```

---

# Current Working Objectives

## Objective 1

Analyze the operational characteristics and severity of cyber incidents using the Incident Master dataset.

---

## Objective 2

Analyze the financial impacts of cyber incidents using the Financial Impact dataset.

---

## Objective 3

Analyze market reactions to cyber incident disclosures using the Market Impact dataset.

---

## Objective 4

Conduct a comparative analysis on the 329 common incidents to investigate relationships among:

- Operational Severity
- Financial Losses
- Market Responses

---

# Current Project Status

## Completed

- Dataset Inspection
- Variable Identification
- Data Validation
- Dataset Relationship Mapping
- Common ID Verification
- Initial Descriptive Statistics
- Distribution Assessment
- Skewness Assessment
- Methodology Selection
- Scope Refinement

---

## Next Steps

### Incident Analysis

- Attack Vector Frequencies
- Industry Analysis
- Downtime Analysis
- Data Compromise Analysis

### Financial Analysis

- Financial Severity Classification
- Cost Distribution Analysis
- Outlier Detection

### Market Analysis

- Abnormal Return Analysis
- Recovery Analysis
- Volatility Analysis

### Comparative Analysis

Investigate:

- Breach Size ↔ Financial Loss
- Financial Loss ↔ Market Reaction
- Downtime ↔ Recovery Time

### Advanced Analysis

- Correlation Analysis
- Anomaly Detection
- Severity Framework Validation

---

# Current Project Maturity

**Status:** Transitioning from Data Investigation Phase into Formal Statistical Analysis Phase.

-------
# Cyber Incident Impact Analysis Project Log
## Project Evolution and Decision History

---

# Initial Project Concept

The project began as a portfolio-oriented cybersecurity and data analytics project using three related datasets:

1. Incident Master Dataset
2. Financial Impact Dataset
3. Market Impact Dataset

Initial intention:

- Statistical anomaly detection
- Cyber incident analysis
- Financial impact assessment
- Portfolio project demonstrating data analytics skills

At this stage, objectives were broad and focused primarily on describing datasets.

---

# Early Project Direction

Several project directions were considered:

## Option 1
Industrial Risk Assessment Analytics

## Option 2
Security Control Effectiveness Dashboard

## Option 3
Cyber-Physical Incident Analysis Repository

After discussion, the project gradually shifted toward:

> Cyber Incident Impact Analysis

because the available datasets contained rich financial and market variables.

---

# Initial Roadmap

Initial plan:

1. Dataset exploration
2. Variable discovery
3. Exploratory Data Analysis (EDA)
4. Descriptive statistics
5. Visualizations
6. Potential anomaly detection

---

# Dataset Investigation Phase

Three datasets were examined.

## Incident Master Dataset

850 incidents

Contains:

- Company metadata
- Industry classifications
- Country information
- Attack vectors
- Downtime data
- Records compromised
- Quality indicators

Observation:

Mostly categorical variables with only a few quantitative measures.

---

## Financial Impact Dataset

778 incidents

Contains:

- Direct losses
- Recovery costs
- Legal fees
- Regulatory fines
- Insurance payouts
- Total losses
- Inflation-adjusted losses

Observation:

Primary source of financial severity information.

---

## Market Impact Dataset

358 incidents

Contains:

- Stock prices
- Abnormal returns
- CAR metrics
- Volatility measures
- Recovery periods

Observation:

Suitable for market reaction studies.

---

# Initial Objective Discussion

Original objectives:

1. Analyze operational characteristics.
2. Analyze financial impacts.
3. Analyze market reactions.

Problem identified:

These objectives were broad enough that they could be completed using only basic descriptive statistics.

---

# Data Quality Investigation

A significant issue was discovered:

Datasets did not contain the same number of observations.

## Counts

Incident Dataset

850 incidents

Financial Dataset

778 incidents

Market Dataset

358 incidents

Concern:

How can datasets be compared if they contain different numbers of observations?

---

# Common Incident ID Investigation

A set-based comparison was performed.

Using Python:

```python
set()
```

Common incident IDs were identified.

Results:

```text
Common IDs across all datasets: 329

Financial-only IDs: 0

Market-only IDs: 0
```

Interpretation:

Market dataset is essentially a subset of Financial dataset.

Financial dataset is essentially a subset of Incident dataset.

The three datasets can therefore be merged using the 329 common incidents.

---

# First Major Methodological Decision

Two competing approaches were considered.

## Approach A

Analyze all datasets separately.

Advantages:

- Maximum sample size
- Simpler analysis
- No loss of observations

---

## Approach B

Analyze only common IDs.

Advantages:

- Enables direct comparisons
- Supports correlation and predictive modeling

Disadvantages:

- Significant reduction in sample size

---

# Selected Approach

Balanced approach chosen.

Plan:

### Primary Analysis

Analyze each dataset separately using its full sample size.

### Secondary Analysis

Perform integrated analysis using the 329 common incidents.

This preserves data while enabling cross-dataset insights.

---

# Exploratory Data Analysis (EDA)

EDA was performed on the Incident Master Dataset.

---

## Attack Vector Analysis

Most common attack vectors:

```text
Ransomware
Phishing
Data Breach
APT
Malware
DDoS
Supply Chain
Trojan
Backdoor
```

Finding:

Ransomware was the dominant attack vector.

---

## Public vs Private Companies

Distribution found to be nearly balanced.

---

## Downtime Analysis

Key observation:

Downtime distribution was highly skewed.

Median was preferred over mean.

Reason:

Extreme incidents heavily inflated average downtime.

---

## Data Compromised Analysis

Similar skewness observed.

Median became preferred measure of central tendency.

---

# Statistical Methodology Discussion

Question raised:

Why use Median + IQR instead of Mean + Standard Deviation?

Conclusion:

Cyber incident data are heavily right-skewed.

Therefore:

Preferred:

- Median
- IQR

Supplementary:

- Mean
- Standard Deviation

Both can be reported.

---

# Revenue Variable Discussion

Question:

Should company revenue be used?

Conclusion:

Revenue is more descriptive of companies than incidents.

Revenue does not directly measure cyber impact.

Decision:

Revenue removed from primary analyses.

May be used later in predictive modeling.

---

# Employee Count Discussion

Question:

Should employee count be analyzed?

Conclusion:

Not directly related to incident severity.

Decision:

Removed from primary scope.

---

# Industry Variable Investigation

Discovery:

industry_primary contains NAICS codes.

Examples:

```text
62
52
51
44-45
31-33
```

Interpretation:

Industry classification rather than numerical values.

Decision:

Treat as categorical variable.

---

# Missing Data Investigation

Missing value analysis added.

Purpose:

- Identify unreliable variables
- Assess completeness
- Improve dataset understanding

This became a standard component of all analyses.

---

# Downtime Missingness Discovery

Several attack vectors showed:

```text
Count = 0
```

for downtime.

Affected vectors:

- Phishing
- Data Breach
- Trojan
- Backdoor

Important conclusion:

Cannot conclude:

> These incidents caused no downtime.

Correct conclusion:

> Downtime information is missing for these incidents.

---

# Portfolio vs Academic Research Discussion

Clarification:

This project is a portfolio project.

Not:

- Thesis
- Journal article
- Formal academic research

Implication:

Practical insights are prioritized over methodological perfection.

---

# Interactive CLI Discussion

Idea proposed:

Create a CLI allowing users to request specific analyses.

Decision:

Not prioritized.

Reason:

Portfolio value comes primarily from:

- Analysis
- Visualizations
- Documentation

CLI can be added later as a bonus feature.

---

# Jupyter Notebook Decision

Decision:

Adopt Jupyter Notebooks after analysis scripts stabilize.

Reason:

Notebooks are better suited for:

- Documentation
- Narrative analysis
- Portfolio presentation

---

# Kaggle Dataset Review

Dataset creator description reviewed.

Key intended use cases:

- Financial loss prediction
- Market reaction analysis
- Risk modeling
- Industry vulnerability comparison
- Time-series studies
- Severity classification

This prompted reevaluation of project objectives.

---

# Confidence Tier Investigation

Issue:

Dataset documentation does not define whether:

```text
1 = Highest Confidence
```

or

```text
1 = Lowest Confidence
```

Decision:

Remove confidence tier from primary analyses.

Reason:

Interpretation cannot be validated.

---

# Objective Redefinition

Original objectives considered too broad.

New structure created.

---

## Objective 1

Operational Analysis

Focus:

- Attack vectors
- Industries
- Downtime
- Data exposure

---

## Objective 2

Financial Impact Analysis

Focus:

- Direct losses
- Recovery costs
- Legal fees
- Regulatory fines
- Insurance payouts
- Total losses

---

## Objective 3

Market Reaction Analysis

Focus:

- Abnormal returns
- CAR metrics
- Trading volume
- Volatility
- Recovery periods

---

## Objective 4

Integrated Impact Analysis

Using:

329 Common Incident IDs

Focus:

- Operational vs Financial
- Financial vs Market
- Attack Vector Impact

---

# Predictive Modeling Added

Following consultation with an analyst, predictive modeling was added.

Reason:

Existing objectives could largely be satisfied with descriptive statistics alone.

New objective:

Predict incident severity and financial impact.

Potential target:

```text
total_loss_usd
```

Potential features:

- Attack Vector
- Industry
- Downtime
- Records Compromised
- Public/Private Status

---

# Time-Based Financial Analysis Discussion

Idea proposed:

Analyze losses with respect to incident dates.

Conclusion:

Possible using:

```text
Median Loss by Year
```

Prefer:

```text
inflation_adjusted_usd
```

over:

```text
total_loss_usd
```

to avoid inflation bias.

---

# Calculus Discussion

Question:

Can derivatives be used?

Conclusion:

Yes.

Example:

Median Loss = f(Year)

Derivative interpretation:

Rate of change in incident losses over time.

However:

This is supplementary analysis rather than a primary project objective.

---

# Current Project Structure

Phase 1

Operational Analysis

Phase 2

Financial Impact Analysis

Phase 3

Market Reaction Analysis

Phase 4

Integrated Impact Analysis

Phase 5

Predictive Modeling

---

# Current Status

Completed:

- Dataset investigation
- Variable investigation
- Dataset integration assessment
- Common ID analysis
- Initial Incident Dataset EDA
- Missing value assessment
- Objective redesign
- Methodology refinement

In Progress:

- Incident Dataset Analysis

Upcoming:

- Financial Impact Analysis
- Market Impact Analysis
- Integrated Impact Analysis
- Predictive Modeling
- Jupyter Notebook Documentation

---

# Current Working Philosophy

Analyze each dataset independently first.

Extract findings using full sample sizes.

Then:

Use the 329 common incidents for integrated analysis and predictive modeling.

This maximizes available information while maintaining analytical rigor appropriate for a portfolio project.
