# Financial Impact Analysis

import pandas as pd

df = pd.read_csv('financial_impact.csv')

print(df.info())

print("------------------")
print(df.describe())
