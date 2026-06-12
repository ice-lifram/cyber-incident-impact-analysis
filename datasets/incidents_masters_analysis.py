# Incident Metadata Analysis

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
# Quality Score
quality_grade = df['quality_grade'].value_counts()

print(quality_grade)

# Attack Vectors + Downtime Analysis
print("\nAttack Vector + Downtime Hours Analysis")
attack_downtime = df.groupby("attack_vector_primary")["downtime_hours"].agg([
    "count",
    "median",
    "mean",
    ])

print(attack_downtime)

# Attack Vector + Data Compromised Records Analysis
print("\nAttack Vector + Data Compromised Analysis")
record_compromised = df.groupby("attack_vector_primary")["data_compromised_records"].agg([
    "count",
    "mean",
    "median",
])
print(record_compromised)

print()

# Industries affected
industries = df['industry_primary'].value_counts()
print(industries)
industries_downtime = df.groupby('industry_primary')['downtime_hours'].agg([
    "count",
    "mean",
    "median"
])
print(industries_downtime)

print()

industries_records = df.groupby("industry_primary")['data_compromised_records'].agg([
    "count",
    "mean",
    "median"
])
print(industries_records)


# Define all missing values
print("\nMissing Values")
print("--------------------")

missing = df.isnull().sum()
missing_pct = (missing / len(df) * 100).round(2)

missing_df = pd.DataFrame({
    "Missing Count": missing,
    "Missing %": missing_pct
})

print(missing_df.sort_values("Missing %", ascending=False))
