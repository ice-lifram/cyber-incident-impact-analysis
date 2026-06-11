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
