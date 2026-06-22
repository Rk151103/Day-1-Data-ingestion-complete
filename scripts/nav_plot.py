import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/nav_clean.csv")

plt.plot(df["Date"], df["NAV"], marker="o")

plt.title("NAV Trend")
plt.xlabel("Date")
plt.ylabel("NAV")
plt.grid(True)

plt.show()