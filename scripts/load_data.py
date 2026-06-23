import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///../bluestock_mf.db")

# Load cleaned files
nav_df = pd.read_csv("../data/processed/clean_nav.csv")
txn_df = pd.read_csv("../data/processed/clean_transactions.csv")
perf_df = pd.read_csv("../data/processed/clean_performance.csv")
fund_df = pd.read_csv("../data/raw/01_fund_master.csv")

# Load into database
fund_df.to_sql("dim_fund", engine, if_exists="replace", index=False)
nav_df.to_sql("fact_nav", engine, if_exists="replace", index=False)
txn_df.to_sql("fact_transactions", engine, if_exists="replace", index=False)
perf_df.to_sql("fact_performance", engine, if_exists="replace", index=False)

print("All data loaded successfully")