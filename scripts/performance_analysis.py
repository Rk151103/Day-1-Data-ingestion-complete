import pandas as pd

df = pd.read_csv("data/processed/nav_returns.csv")

avg_return = df["Daily_Return_%"].mean()
max_return = df["Daily_Return_%"].max()
min_return = df["Daily_Return_%"].min()

print("Performance Analysis")
print("-------------------")
print("Average Return:", avg_return)
print("Maximum Return:", max_return)
print("Minimum Return:", min_return)