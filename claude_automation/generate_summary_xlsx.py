import pandas as pd
import numpy as np
import os

def get_project_root():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def get_comprehensive_stats(df):
    numeric_df = df.select_dtypes(include=[np.number])
    if numeric_df.empty:
        return pd.DataFrame()

    full_summary = numeric_df.describe().T
    mode = numeric_df.mode().iloc[0] if not numeric_df.mode().empty else numeric_df.mean()
    full_summary['mode'] = mode

    cols = ['mean', '50%', 'mode', 'min', '25%', '75%', 'max']
    full_summary = full_summary[cols].rename(columns={'50%': 'median'})

    return full_summary

def main():
    root = get_project_root()
    files = {
        'Incidents Master': os.path.join(root, 'datasets/incidents_master.csv'),
        'Financial Impact': os.path.join(root, 'datasets/financial_impact.csv'),
        'Market Impact': os.path.join(root, 'datasets/market_impact.csv')
    }

    dataframes = {}
    for name, path in files.items():
        dataframes[name] = pd.read_csv(path)

    summaries = {}
    for name, df in dataframes.items():
        summaries[name] = get_comprehensive_stats(df)

    non_negotiables = [
        'incident_id', 'company_name', 'stock_ticker', 'company_revenue_usd',
        'incident_date', 'attack_vector_primary', 'total_loss_usd',
        'total_loss_lower_bound', 'total_loss_upper_bound', 'recovery_cost_usd'
    ]
    considering = [
        'abnormal_return_1d', 'days_to_price_recovery'
    ]
    all_necessary_cols = non_negotiables + considering

    try:
        df_combined = dataframes['Incidents Master'].merge(
            dataframes['Financial Impact'], on='incident_id', how='inner'
        ).merge(
            dataframes['Market Impact'], on='incident_id', how='inner'
        )
        existing_cols = [col for col in all_necessary_cols if col in df_combined.columns]
        df_final_combined = df_combined[existing_cols]
    except Exception as e:
        print(f"Error combining datasets: {e}")
        df_final_combined = pd.DataFrame()

    output_file = os.path.join(root, 'dataset_summary.xlsx')
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        for name in ['Incidents Master', 'Financial Impact', 'Market Impact']:
            summaries[name].to_excel(writer, sheet_name=name)
        df_final_combined.to_excel(writer, sheet_name='Combined', index=False)

    print(f"\nSuccess! Results written to {output_file}")

if __name__ == "__main__":
    main()
