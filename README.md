# Statistical Analysis of Cyber Incident Impacts using Operational, Financial, and Market Data

Overview
- 
This project investigates the impacts of cyber incidents to the businesses financial status and market reactions with a given dataset.

Objectives
-
- Identify the operational characteristics and severity of cyber incidents occurred
- Analyze the financial losses and recovery costs of the cyber incidents
- Investigate the market's reaction to cyber incident occurence
---------

Methodology
-
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

Tools Used
-
- **Descriptive Statistics**
    - Mean
    - Median
    - Standard Deviation
    - Interquartile Range
    - Z-score
- **Python Programming**
    - Pandas (for data analysis)
    - Matplotlib (for data visualization)

Current Findings
-
- **Incident Profile**
	- Attack Vectors (850 data points)
		- Ransomware, phishing, data breaches are common causes
	- 412 out of 850 companies are public companies
	- Downtime (out of 402) 
		- Mean: 107
		- Median: 53
			- Q1 = 25.02
			- Q3 = 119.800
		- Standard Deviation: 184
    -  **Attack Vectors + Downtime Correlation**
        - APT, DDoS, Malware, Ransomware, and Supply Chain have recorded downtime hours information
	    -  Backdoor, Data Breach, Phishing, and Trojan have no downtime observations recorded
- **Financial Impact**
- **Market Impact**


