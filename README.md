# Statistical Analysis of Cyber Incident Impacts using Operational, Financial, and Market Data

## Overview
This project investigates the impacts of cyber incidents on businesses through operational incident metadata, financial losses, and market reactions using publicly available datasets. The project aims to characterize cyber incidents, identify relationships across multiple dimensions of risk, and develop a predictive model for estimating future impacts.

---

# Objectives

- Establish a baseline understanding of the datasets
- Discover correlations and dependencies across different dimensions of risk
- Develop a predictive model to estimate the impacts of future cyber incidents

---

# Methodology

## Exploratory Data Analysis

### Multistage Analysis of Datasets

#### Stage 1: Operational Incidents

- Common Attack Vectors
- Impact of Attacks to Companies
- Industry Analysis
- Quality Scores
- Downtime Analysis
- Data Compromised Records

#### Stage 2: Financial Impact

- Direct and Total Losses
- Recovery Costs
- Ransom Demands and Payments
- Insurance Payouts
- Loss Estimation Methods

#### Stage 3: Market Impact

- Stock Prices Before, During, and After Disclosure
- Trading Volume Analysis
- Abnormal Returns
- Cumulative Abnormal Returns (CAR)
- Market Capitalization
- Pre- vs. Post-Incident Volatility
- Days to Price Recovery

---

## Cross-Exploratory Analysis

- Data Merging
- GroupBy Analysis
- Correlation Analysis

---

## Predictive Model Development

- Feature Selection
- Model Training
- Model Evaluation
- Hyperparameter Tuning

---

# Tools Used

## Descriptive Statistics

- Mean
- Median
- Standard Deviation
- Minimum / Maximum

## Python Programming

- Pandas (Data Analysis)
- Matplotlib (Visualization)

## AI Agents

Used for:

- Brainstorming
- Code snippets
- Automating repetitive analysis
- Documentation assistance

---

# Current Findings

## Stage 1 – Incident Metadata

### Incident Profile

**Attack Vectors (850 incidents)**

- Ransomware, phishing, and data breaches were the three most frequently reported attack vectors.
- Approximately 48.5% (412/850) of affected organizations were publicly traded companies.

### Downtime Hours

- Available observations: 420
- Mean: 107.21 hours
- Median: 53.60 hours
- Standard Deviation: 184.65 hours
- Q1: 25.82 hours
- Q3: 119.80 hours
- Distribution is highly right-skewed, indicating a small number of incidents caused exceptionally long operational disruptions.

### Attack Vector vs. Downtime

- Ransomware exhibited the highest number of recorded downtime observations.
- Supply chain attacks and Advanced Persistent Threat (APT) incidents generally experienced higher median downtime.
- Backdoor, phishing, data breach, and trojan incidents contained no reported downtime observations within the dataset.

### Data Compromised Records

- Available observations: 602
- Distribution is heavily right-skewed.
- Large-scale breaches substantially increase the overall mean.
- Industries with the largest compromised records were not necessarily the same industries exhibiting the longest operational downtime.

### Industry Analysis

- Healthcare (62), Finance (52), and Information (51) contained the greatest number of documented incidents.
- Industry-level downtime and compromised records varied considerably.
- Findings from industries with small sample sizes were interpreted cautiously.

---

## Stage 2 – Financial Impact

### Direct Financial Losses

- Reported direct losses ranged from approximately **USD 90,000** to **USD 2.30 billion**.
- The distribution was strongly right-skewed, indicating a relatively small number of extremely costly incidents.

### Total Financial Losses

- Total estimated losses ranged from approximately **USD 174 thousand** to **USD 3.45 billion**.
- Large-scale incidents substantially increased average losses.

### Recovery Costs

- Recovery costs also exhibited a right-skewed distribution.
- Most organizations incurred relatively moderate recovery costs, while a small number experienced exceptionally high expenditures.

### Ransom Analysis

- Both ransom demands and ransom payments demonstrated substantial variability.
- Many incidents contained missing ransom information, suggesting either undisclosed or non-applicable ransom events.

### Insurance Payouts

- Insurance payouts varied considerably across incidents.
- A substantial proportion of observations contained missing values, indicating incomplete disclosure.

---

## Stage 3 – Market Impact

### Stock Price Performance

- Average abnormal returns were negative across the 1-day, 7-day, and 30-day event windows, indicating an overall negative market response following cyber incident disclosures.

### Cumulative Abnormal Returns (CAR)

- Mean CAR values remained negative across all analyzed event windows, suggesting persistent adverse market reactions after disclosure.

### Trading Activity

- Disclosure-day trading volume was substantially higher than baseline trading volume.
- Median disclosure-day trading volume was approximately **2.75×** the normal trading activity.

### Market Volatility

- Average post-incident volatility exceeded pre-incident volatility, indicating increased market uncertainty following cyber incidents.

### Price Recovery

- Median recovery time was approximately **57 days**.
- Recovery times exhibited a right-skewed distribution, with several firms requiring substantially longer periods to recover.

---

# Current Progress

- ✅ Incident Metadata Analysis
- ✅ Financial Impact Analysis
- ✅ Market Impact Analysis
- ⏳ Cross-Dataset Exploratory Analysis
- ⏳ Predictive Modeling
- ⏳ Final Documentation
