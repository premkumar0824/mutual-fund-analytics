import pandas as pd

fund_df = pd.read_csv("data/raw/01_fund_master.csv")
nav_df = pd.read_csv("data/raw/02_nav_history.csv")

fund_codes = set(fund_df["amfi_code"])
nav_codes = set(nav_df["amfi_code"])

missing_codes = fund_codes - nav_codes

print("=" * 50)
print("AMFI CODE VALIDATION")
print("=" * 50)

print("Fund Master Codes:", len(fund_codes))
print("NAV History Codes:", len(nav_codes))

if len(missing_codes) == 0:
    print("\nSUCCESS: All AMFI codes exist in NAV history")
else:
    print("\nMissing Codes:")
    print(missing_codes)