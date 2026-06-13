import pandas as pd
import numpy as np
import os

def get_project_root():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def get_comprehensive_stats(df, ordered_cols):
    numeric_df = df.select_dtypes(include=[np.number])
    if numeric_df.empty:
        return pd.DataFrame()

    # Calculate basic stats
    full_summary = numeric_df.describe().T
    mode_series = numeric_df.mode().iloc[0] if not numeric_df.mode().empty else numeric_df.mean()
    full_summary['mode'] = mode_series

    # Final column set
    cols = ['mean', '50%', 'mode', 'min', '25%', '75%', 'max']
    full_summary = full_summary[cols].rename(columns={'50%': 'median'})

    # Reorder the rows (variables) based on the provided ordered_cols list
    existing_vars = [var for var in ordered_cols if var in full_summary.index]
    # Add any variables that weren't in our priority list to the end
    remaining_vars = [var for var in full_summary.index if var not in existing_vars]

    return full_summary.loc[existing_vars + remaining_vars]

def main():
    root = get_project_root()

    # 1. Define the Analytical Frame Order
    # Cause -> Scale -> Cost -> Reaction -> Truth
    frame_order = [
        # Cause
        'attack_vector_primary', 'downtime_hours', 'data_compromised_records',
        'data_type', 'systems_affected', 'attack_vector_secondary', 'attack_chain',
        # Scale
        'company_revenue_usd', 'employee_count', 'market_cap_at_disclosure', 'is_public_company',
        # Cost
        'total_loss_usd', 'direct_loss_usd', 'recovery_cost_usd',
        'legal_fees_usd', 'regulatory_fine_usd', 'insurance_payout_usd',
        # Reaction
        'abnormal_return_1d', 'abnormal_return_7d', 'abnormal_return_30d',
        'days_to_price_recovery', 'volume_ratio_disclosure', 'p_value_1d',
        # Truth
        'quality_score', 'quality_grade', 'confidence_tier'
    ]

    files = {
        'Incidents Master': os.path.join(root, 'datasets/incidents_master.csv'),
        'Financial Impact': os.path.join(root, 'datasets/financial_impact.csv'),
        'Market Impact': os.path.join(root, 'datasets/market_impact.csv')
    }

    dataframes = {}
    for name, path in files.items():
        dataframes[name] = pd.read_csv(path)

    # 2. Individual Summaries (Reordered by Frame)
    summaries = {}
    for name, df in dataframes.items():
        summaries[name] = get_comprehensive_stats(df, frame_order)

    # 3. Combined Sheet (Reordered by Frame)
    try:
        df_combined = dataframes['Incidents Master'].merge(
            dataframes['Financial Impact'], on='incident_id', how='inner'
        ).merge(
            dataframes['Market Impact'], on='incident_id', how='inner'
        )

        # Start with ID, then follow the frame order
        final_cols = ['incident_id'] + [col for col in frame_order if col in df_combined.columns]
        # Add any other columns that might be useful but weren't in the frame (e.g. company_name)
        others = [col for col in df_combined.columns if col not in final_cols]
        df_final_combined = df_combined[final_cols + others]

    except Exception as e:
        print(f"Error combining datasets: {e}")
        df_final_combined = pd.DataFrame()

    # 4. Write to XLSX
    output_file = os.path.join(root, 'dataset_summary.xlsx')
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        # Individual summaries
        for name in ['Incidents Master', 'Financial Impact', 'Market Impact']:
            summaries[name].to_excel(writer, sheet_name=name)

        # Combined sheet
        df_final_combined.to_excel(writer, sheet_name='Combined', index=False)

    print(f"\nSuccess! Results written and sorted by Analytical Frame in {output_file}")

if __name__ == "__main__":
    main()
