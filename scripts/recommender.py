import pandas as pd

funds = {
    "Low": [
        "SBI_Bluechip",
        "HDFC_Top_100_Direct",
        "ICICI_Bluechip"
    ],
    "Moderate": [
        "Kotak_Bluechip",
        "Axis_Bluechip",
        "Nippon_India_Large_Cap"
    ],
    "High": [
        "Axis_Bluechip",
        "Kotak_Bluechip",
        "ICICI_Bluechip"
    ]
}

risk = input("Enter Risk Appetite (Low/Moderate/High): ").strip()

if risk in funds:
    print("\nTop 3 Recommended Funds")
    print(pd.DataFrame({"Fund": funds[risk]}))
else:
    print("Invalid Risk Level")