# Cyber Incident Impact Analytics and Anomaly Detection

Possible Objectives
- 
- Seeks to identify impacts of cyber incidents
- Financial loss prediction [/]
    - What are the mean of the financial loss
    - How widely the losses vary from each other 
- Market reaction analysis [/]
    - The correlating impact of cyberattacks in the market
- Risk modeling
- Industry vulnerability comparison [/]
- Time-series impact studies [/]
- Classification of high vs low severity incidents

Scope
- 
- Only the analyis of financial loss, correlation of cyberattack impacts on the market.
- Selective Analysis (???); a curated analytical dataset
- Involves descriptive statistics; no predictive modelling

Findings Before Data Analysis
- Number of Rows including header
    - incidents_master.csv : 851
    - market_impact.csv : 359
    - financial_impact.csv : 779
- Data is currently unsorted


Unique Tickers Audit
-
==================================================
INCIDENT MASTER
==================================================
Rows: 850
Unique Tickers: 359

Top 20 Tickers:
stock_ticker
SNV.SW     4
BZE.L      3
NAS1       3
RMM.MX     3
ORLA.JO    3
BITW       2
SFM        2
STUT.DE    2
MAR1.TO    2
VECT.AX    2
HARB.L     2
CMM.SA     2
SCHN.VI    2
SANT.HK    2
SCF.T      2
PHOE       2
PATH.KS    2
NHW.T      2
VTL.TO     2
CCL.CO     2
Name: count, dtype: int64


==================================================
MARKET IMPACT
==================================================
Rows: 358
Unique Tickers: 317

Top 20 Tickers:
stock_ticker
BZE.L      3
NAS1       3
SNV.SW     3
RMM.MX     3
ORLA.JO    3
BITW       2
SFM        2
STUT.DE    2
MAR1.TO    2
VECT.AX    2
HARB.L     2
CMM.SA     2
SCHN.VI    2
SCF.T      2
PHOE       2
PATH.KS    2
NHW.T      2
VTL.TO     2
OKON.L     2
TBL        2

