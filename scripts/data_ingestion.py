import pandas as pd
import os

raw_data_path = "data/raw"

files = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

print("=" * 60)
print("DATA INGESTION STARTED")
print("=" * 60)

for file in files:
    file_path = os.path.join(raw_data_path, file)

    print(f"\nLoading: {file}")

    df = pd.read_csv(file_path)

    print("Shape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("-" * 60)

print("\nDATA INGESTION COMPLETED")