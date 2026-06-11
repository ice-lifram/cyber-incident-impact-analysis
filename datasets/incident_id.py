# Incident IDs Analysis

import pandas as pd

incidents = pd.read_csv('incidents_master.csv')
finance = pd.read_csv('financial_impact.csv')
market = pd.read_csv('market_impact.csv')

id_masters = incidents['incident_id']
id_finance = finance['incident_id']
id_market = market['incident_id']

common_ids = (
    set(incidents["incident_id"])
    & set(finance["incident_id"])
    & set(market["incident_id"])
)

print("Total common IDs, ", len(common_ids))


incident_ids = set(incidents["incident_id"])
financial_ids = set(finance["incident_id"])
market_ids = set(market["incident_id"])

print("Unique in Financial:")
print(len(financial_ids - incident_ids))

print("Unique in Market:")
print(len(market_ids - incident_ids))

print("Similar to all three:")
print(len(incident_ids & financial_ids & market_ids))

print("Data Points of Market")
print("Length: ", len(market["incident_id"]))

