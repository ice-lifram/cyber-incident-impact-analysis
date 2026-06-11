# Incident Masters Analysis

import pandas as pd

df = pd.read_csv('incidents_master.csv')

print(df.info())

incident_id = df['incident_id']
revenue = df['company_revenue_usd']
employee_count = df['employee_count']
attack_vector = df['attack_vector_primary']
downtime_hours = df['downtime_hours']



print(df.describe())
print("------------------------------------")
pd.set_option('display.max_rows', None)

# Number of Attack Vectors
attack_vectors_numbers = attack_vector.value_counts()

# Descriptive Statistics of Revenue
revenue_stat = revenue.describe()
print(revenue_stat)

# Descriptive Statistics of Revenue by Attack Vector 
count = df.groupby("attack_vector_primary")["company_revenue_usd"].agg([
    "count",
    "mean",
    "median",
    "min",
    "max"
]).sort_values("median", ascending=False)

print(count)
