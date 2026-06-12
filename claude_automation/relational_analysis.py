import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

def get_project_root():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def main():
    root = get_project_root()

    # Load datasets
    incidents = pd.read_csv(os.path.join(root, 'datasets/incidents_master.csv'))
    financial = pd.read_csv(os.path.join(root, 'datasets/financial_impact.csv'))
    market = pd.read_csv(os.path.join(root, 'datasets/market_impact.csv'))

    # Merge datasets
    df = incidents.merge(financial, on='incident_id', how='inner').merge(market, on='incident_id', how='inner')

    insights = ["# 📊 Comparative Insights\n\n"]

    # 1. Correlation Analysis
    insights.append("## 1. Correlation Analysis\n")
    numeric_cols = ['total_loss_usd', 'company_revenue_usd', 'abnormal_return_1d', 'days_to_price_recovery', 'downtime_hours', 'data_compromised_records']
    available_numeric = [col for col in numeric_cols if col in df.columns]
    corr_matrix = df[available_numeric].corr()

    insights.append("Correlation matrix of key metrics:\n")
    insights.append(corr_matrix.to_markdown() + "\n\n")

    # 2. Impact by Attack Vector
    insights.append("## 2. Impact by Attack Vector\n")
    vector_impact = df.groupby('attack_vector_primary')['total_loss_usd'].agg(['mean', 'median', 'std', 'count']).sort_values(by='mean', ascending=False)
    insights.append("Financial loss aggregated by attack vector:\n")
    insights.append(vector_impact.to_markdown() + "\n\n")

    # 3. Impact by Industry
    insights.append("## 3. Impact by Industry\n")
    industry_impact = df.groupby('industry_primary')['total_loss_usd'].agg(['mean', 'median', 'std', 'count']).sort_values(by='mean', ascending=False)
    insights.append("Financial loss aggregated by industry:\n")
    insights.append(industry_impact.to_markdown() + "\n\n")

    # 4. Market vs Financial Severity
    insights.append("## 4. Market vs Financial Severity\n")
    df['severity_bin'] = pd.qcut(df['total_loss_usd'], 3, labels=['Low', 'Medium', 'High'])
    market_severity = df.groupby('severity_bin')['abnormal_return_1d'].mean()
    insights.append("Average abnormal return based on financial loss severity quintiles:\n")
    insights.append(market_severity.to_markdown() + "\n\n")

    # Write to file
    output_path = os.path.join(root, 'documentations/comparative_insights.md')
    with open(output_path, 'w') as f:
        f.write("\n".join(insights))

    print(f"Relational analysis complete. Insights written to {output_path}")

if __name__ == "__main__":
    main()
