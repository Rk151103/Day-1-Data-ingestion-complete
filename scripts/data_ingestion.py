import pandas as pd

print("Data Ingestion Started")

try:
    df = pd.read_csv("data/raw/sample_nav.csv")

    print("\nData Loaded Successfully!")
    print(df)

    df.to_csv("data/processed/nav_clean.csv", index=False)

    print("\nProcessed file saved!")

except Exception as e:
    print("Error:", e)