# Incident Profile Analysis

import pandas as pd

df = pd.read_csv('incidents_master.csv')

print(df.info())

incident_id = df['incident_id']
revenue = df['company_revenue_usd']
attack_vector = df['attack_vector_primary']
downtime_hours = df['downtime_hours']


print(df.describe())
print("------------------------------------")
pd.set_option('display.max_rows', None)

print()

# Number of Attack Vectors
attack_vectors_numbers = attack_vector.value_counts()
print(attack_vectors_numbers)

print()

# Public/Private Companies
company_type = df['is_public_company'].value_counts()
print(company_type)

print()

# Average Downtime Hours
print(downtime_hours.describe())

print()

# Data Compromised Records
data_com_rec = df['data_compromised_records'].describe()
print(data_com_rec)

print()
# Quality and Confidence Tier
confidence_tier = df['confidence_tier'].value_counts()
quality_grade = df['quality_grade'].value_counts()

print(confidence_tier)
print('---------------------')
print(quality_grade)

print()

# Attack Revenue + Downtime Analysis
attack_downtime = df.groupby("attack_vector_primary")["downtime_hours"].count()

print(attack_downtime)
