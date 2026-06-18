# Financial Impact Analysis

import pandas as pd

df = pd.read_csv('financial_impact.csv')

# print(df)

print("------------------")
print(df.describe())


incident_id = df['incident_id']
direct_losses = df['direct_loss_usd']
direct_loss_method = df['direct_loss_method']
recovery_cost = df['recovery_cost_usd']
total_loss = df['total_loss_usd']
inflation_adjusted = df['inflation_adjusted_usd']
insurance_payout = df['insurance_payout_usd']
regulatory_fine = df['regulatory_fine_usd']
total_loss_method = df['total_loss_method']
ransom_demanded = df['ransom_demanded_usd']
ransom_paid = df['ransom_paid_usd']
ransom_source = df['ransom_source']

# Total Loss and adjusted costs by inflation
print(total_loss.agg(["count", "median", "min", "max", "mean"]))
print("---------")
print(inflation_adjusted.agg(["count", "median", "min", "max", "mean"]))
"""
print()
# Direct Losses
print(direct_losses.describe())

print()
# Recovery Costs
print(recovery_cost.describe())

print()
# Total Loss
print(total_loss.describe())

print()
# Insurance Payout
print(insurance_payout.describe())

print()
# Ransom Demanded
print(ransom_demanded.describe())

# Ransom Paid
print(ransom_paid.describe())

print()
# Ransom Source
print(ransom_source.value_counts())

print()

# Calculations
# 1. Direct, Ransoms, Recovery, and Insurance costs
"""
