import pandas as pd
import os

print("Data Ingestion Started")

raw_folder = "data/raw"
processed_folder = "data/processed"

os.makedirs(processed_folder, exist_ok=True)

for file in os.listdir(raw_folder):
    if file.endswith(".csv"):

        file_path = os.path.join(raw_folder, file)

        try:
            df = pd.read_csv(file_path)

            print(f"\nProcessing: {file}")
            print("Shape:", df.shape)

            print("\nData Types:")
            print(df.dtypes)

            print("\nFirst 5 Rows:")
            print(df.head())

            output_file = os.path.join(
                processed_folder,
                f"processed_{file}"
            )

            df.to_csv(output_file, index=False)

            print(f"\nSaved: {output_file}")

        except Exception as e:
            print(f"Error processing {file}: {e}")

print("\nAll datasets processed successfully!")