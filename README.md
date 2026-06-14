# Statistical Analysis of Cyber Incident Impacts using Operational, Financial, and Market Data

Overview
- 
This project investigates the impacts of cyber incidents to the businesses financial status and market reactions with a given dataset.

Objectives
-
- Establish a baseline understanding of the datasets
- Discover correlations and dependencies across different dimensions of risk
- Develop a predictive model to establish the impact of future risks
---------

Methodology
-
- **Exploratory Data Analysis** :
    - Multistage Analysis of Datasets
        - **Stage 1: Operational Incidents**
            - Common Attack Vectors
            - Impact of Attacks to the companies
            - Quality Scores
        - **Stage 2: Financial Impact**
            - Direct and Total Losses
            - Ransoms
            - Recovery Costs
            - Payouts
        - **Stage 3: Market Impact**
            - Prices before, during, and after disclosure
            - Volume Average
            - T-statistics and p-values
            - Market Cap
            - Pre to Post-incident volatility
            - Days to price recovery
- **Cross-Exploratory Analysis**
    - Data Merging
    - GroupBy Analysis
- **Predictive Model Development**
    - Feature Selection
    - Model Training
    - Evaluation
    - Tuning

Tools Used
-
- **Descriptive Statistics**
    - Mean
    - Median
    - Standard Deviation
    - Minima / Maxima
- **Python Programming**
    - Pandas (for data analysis)
    - Matplotlib (for data visualization)
- **AI Agents**
    - For brainstorming, code snippets, and automating redundant tasks


Current Findings
-
- **Incident Profile**
	- Attack Vectors (850 data points)
		- Ransomware, phishing, data breaches yields highest number of appearance in incidents
	- 412 out of 850 companies are public companies
	- Downtime (out of 402) 
		- Mean: 107
		- Median: 53
			- Q1 = 25.02
			- Q3 = 119.800
		- Standard Deviation: 184
        - Median
    -  **Attack Vectors + Downtime Correlation**
        - Ransomware, supply chain attacks, and APT-related incidents exhibits higher downtime values compared to other attack vectors
	    -  Backdoor, Data Breach, Phishing, and Trojan have no downtime observations recorded
    - **Data Compromised Records**
        - Right-skewed distribution
        - 
- **Financial Impact**
    - Direct Losses
        - Ranges from ~$90,000 to ~$2,302,300.00
        - Median is ~$8,525,071
    - Total Losses
        - Ranges from ~$173,793.10 to ~$3,451,548,000.00
    - Recovery Costs
    - Ransoms

- **Market Impact**
