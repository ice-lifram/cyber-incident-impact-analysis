# Cross-exploratory dataset analysis 

import pandas as pd

df = pd.read_csv('data_sum_modified.csv')

# print(df.describe())

# ---------------------- #

# Attack Vectors + Total Loss
print("Attack Vectors + Total Loss")
att_loss = df.groupby('attack_vector_primary')['total_loss_usd'].describe().sort_values('count', ascending=False)
print(att_loss)

# Analysis of Total Losses with respect to Incident Dates
print("\nTotal Losses with respect to Incident Dates")
total_loss_change = df['total_loss_usd'].describe()
print(total_loss_change)

# What's next: graph total loss change with respect to time (incident dates)
