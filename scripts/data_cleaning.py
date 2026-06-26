import pandas as pd
import os

input_folder = "data/raw"
output_folder = "data/processed"

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    if file.endswith(".csv"):
        path = os.path.join(input_folder, file)

        df = pd.read_csv(path)

        if "date" in df.columns:
            df["date"] = pd.to_datetime(df["date"], errors="coerce", dayfirst=True)
            df = df.sort_values("date")

        if "nav" in df.columns:
            df = df[df["nav"] > 0]
            df["nav"] = df["nav"].ffill()

        df = df.drop_duplicates()

        output_path = os.path.join(output_folder, file)
        df.to_csv(output_path, index=False)

        print(f"{file} cleaned successfully!")

print("All CSV files cleaned successfully.")