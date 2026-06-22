import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("=" * 50)
print("FUND MASTER ANALYSIS")
print("=" * 50)

print("\nTotal Schemes:")
print(df["scheme_name"].nunique())

print("\nFund Houses:")
print(df["fund_house"].unique())

print("\nCategories:")
print(df["category"].unique())

print("\nSub Categories:")
print(df["sub_category"].unique())

print("\nRisk Categories:")
print(df["risk_category"].value_counts())

print("\nMissing Values:")
print(df.isnull().sum())