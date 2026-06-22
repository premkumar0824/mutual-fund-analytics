import requests
import pandas as pd

schemes = {
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_largecap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

for name, code in schemes.items():

    print(f"\nFetching {name}...")

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    print("Status Code:", response.status_code)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        file_name = f"data/raw/{name}_nav.csv"

        nav_df.to_csv(file_name, index=False)

        print("Saved:", file_name)
        print("Rows:", len(nav_df))

    else:
        print("Failed to fetch data")

print("\nAll NAV files downloaded successfully.")