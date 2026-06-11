# Summarization of dataset info

import pandas as pd

incidents = pd.read_csv('incidents_master.csv')
finance = pd.read_csv('financial_impact.csv')
market = pd.read_csv('market_impact.csv')

print(incidents.info())
print()
print(finance.info())
print()
print(market.info())
