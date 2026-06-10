# hand coded na kasi napagod sa prompts lmao
# a draft code for data scraping and analysis

import pandas as pd

incident = pd.read_csv('incidents_master.csv')
finance = pd.read_csv('financial_impact.csv')
market = pd.read_csv('market_impact.csv')


print(incident.info())
print()
print(finance.info())
print()
print(market.info())

id_masters = incident['incident_id']
id_finance = finance['incident_id']
id_market = market['incident_id']

merged = incident.merge(
    finance,
    on="incident_id",
    how="inner"
)

print(merged.shape)

full = merged.merge(
    market,
    on="incident_id",
    how="left"
)

print(full)

cols = [
    "total_loss_usd",
    "direct_loss_usd",
    "recovery_cost_usd",
    "legal_fees_usd",
    "regulatory_fine_usd",
    "data_compromised_records",
    "downtime_hours",
    "company_revenue_usd",
    "employee_count"
]

print(merged[cols].describe())
