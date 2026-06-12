import pandas as pd
import os

def get_project_root():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Load datasets
def main():
    root = get_project_root()
    incidents = pd.read_csv(os.path.join(root, 'datasets/incidents_master.csv'))
    financial = pd.read_csv(os.path.join(root, 'datasets/financial_impact.csv'))
    market = pd.read_csv(os.path.join(root, 'datasets/market_impact.csv'))

    print("--- Dataset Summaries ---")
    print(f"Incidents: {incidents.shape[0]} rows, {incidents.shape[1]} cols")
    print(f"Financial: {financial.shape[0]} rows, {financial.shape[1]} cols")
    print(f"Market: {market.shape[0]} rows, {market.shape[1]} cols")

    # Merge datasets for holistic analysis
    df = incidents.merge(financial, on='incident_id', how='inner').merge(market, on='incident_id', how='outer')

    print("\n--- High Level Stats ---")
    print(f"Total Incidents Analyzed: {len(incidents)}")
    print(f"Total Financial Loss (sum of total_loss_usd): ${df['total_loss_usd'].sum():,.2f}")
    print(f"Average Total Loss per Incident: ${df['total_loss_usd'].mean():,.2f}")
    print(f"Median Total Loss per Incident: ${df['total_loss_usd'].median():,.2f}")

    print("\n--- Attack Vector Distribution ---")
    print(incidents['attack_vector_primary'].value_counts())

    print("\n--- Top Attributed Groups ---")
    print(incidents['attributed_group'].value_counts().head(10))

    print("\n--- Industry Distribution ---")
    print(incidents['industry_primary'].value_counts().head(10))

    print("\n--- Public vs Private Financial Impact ---")
    public_loss = df[df['is_public_company'] == True]['total_loss_usd'].mean()
    private_loss = df[df['is_public_company'] == False]['total_loss_usd'].mean()
    print(f"Avg Loss (Public): ${public_loss:,.2f}")
    print(f"Avg Loss (Private): ${private_loss:,.2f}")

    print("\n--- Market Reaction (Avg 1d Abnormal Return) ---")
    print(f"Avg 1d Abnormal Return: {market['abnormal_return_1d'].mean():.4%}")

if __name__ == "__main__":
    main()
