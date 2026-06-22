import pandas as pd

df = pd.read_csv("data/processed/nav_clean.csv")

df["Daily_Return_%"] = df["NAV"].pct_change() * 100

print(df)

df.to_csv("data/processed/nav_returns.csv", index=False)

print("\nNAV return calculation completed!")