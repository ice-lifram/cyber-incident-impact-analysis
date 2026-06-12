import csv
from collections import Counter
import os

def get_project_root():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def analyze_csv(filepath):
    with open(filepath, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    return data

def main():
    root = get_project_root()

    # Load datasets
    incidents_data = analyze_csv(os.path.join(root, 'datasets/incidents_master.csv'))
    financial_data = analyze_csv(os.path.join(root, 'datasets/financial_impact.csv'))
    market_data = analyze_csv(os.path.join(root, 'datasets/market_impact.csv'))

    print("--- Dataset Summaries ---")
    print(f"Incidents: {len(incidents_data)} rows")
    print(f"Financial: {len(financial_data)} rows")
    print(f"Market: {len(market_data)} rows")

    # Analysis: Attack Vectors (Incidents)
    vectors = Counter([row['attack_vector_primary'] for row in incidents_data if row['attack_vector_primary']])
    print("\n--- Primary Attack Vector Distribution ---")
    for vec, count in vectors.most_common():
        print(f"{vec}: {count}")

    # Analysis: Attributed Groups (Incidents)
    groups = Counter([row['attributed_group'] for row in incidents_data if row['attributed_group']])
    print("\n--- Top Attributed Groups ---")
    for group, count in groups.most_common(10):
        print(f"{group}: {count}")

    # Analysis: Financial Impact
    total_losses = []
    for row in financial_data:
        try:
            val = float(row['total_loss_usd'])
            total_losses.append(val)
        except (ValueError, TypeError):
            continue

    if total_losses:
        sum_loss = sum(total_losses)
        avg_loss = sum_loss / len(total_losses)
        print("\n--- Financial Impact Stats ---")
        print(f"Total Loss Sum: ${sum_loss:,.2f}")
        print(f"Average Loss per Incident: ${avg_loss:,.2f}")
        print(f"Max Loss: ${max(total_losses):,.2f}")
        print(f"Min Loss: ${min(total_losses):,.2f}")

    # Analysis: Market Impact (Abnormal Returns)
    abnormal_returns = []
    for row in market_data:
        try:
            val = float(row['abnormal_return_1d'])
            abnormal_returns.append(val)
        except (ValueError, TypeError):
            continue

    if abnormal_returns:
        avg_return = sum(abnormal_returns) / len(abnormal_returns)
        print("\n--- Market Impact Stats ---")
        print(f"Avg 1d Abnormal Return: {avg_return:.4%}")

if __name__ == "__main__":
    main()
