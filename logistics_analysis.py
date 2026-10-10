"""
Week 3: Advanced Data Analysis and Visualization in Logistics
Uses a hypothetical dataset. Run from this folder with:
    pip install -r requirements.txt
    python logistics_analysis.py
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "logistics_shipments.csv"
OUT = ROOT / "visualizations"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA)
print("Shape:", df.shape)
print("\nMissing values:\n", df.isna().sum())
print("\nDescriptive statistics:\n", df.select_dtypes("number").describe().round(2))
print("\nMode summary:\n", df.groupby("Transport_Mode").agg(
    shipments=("Shipment_ID", "count"),
    avg_delivery_days=("Delivery_Time_Days", "mean"),
    avg_cost_inr=("Transportation_Cost_INR", "mean"),
    avg_cost_per_unit=("Cost_per_Unit_INR", "mean")
).round(2))
print("\nRegion summary:\n", df.groupby("Region").agg(
    shipments=("Shipment_ID", "count"),
    avg_delivery_days=("Delivery_Time_Days", "mean"),
    avg_cost_inr=("Transportation_Cost_INR", "mean")
).round(2))
print("\nCorrelation matrix:\n", df.select_dtypes("number").corr().round(2))

plt.figure(figsize=(8, 5))
plt.hist(df["Delivery_Time_Days"], bins=18, edgecolor="black")
plt.title("Distribution of Delivery Times")
plt.xlabel("Delivery time (days)")
plt.ylabel("Number of shipments")
plt.tight_layout()
plt.savefig(OUT / "delivery_time_distribution.png", dpi=160)
plt.close()

mode_cost = df.groupby("Transport_Mode")["Transportation_Cost_INR"].mean().sort_values()
mode_cost.plot(kind="bar", edgecolor="black", figsize=(8, 5))
plt.title("Average Transportation Cost by Mode")
plt.xlabel("Transport mode")
plt.ylabel("Average cost (INR)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(OUT / "average_cost_by_mode.png", dpi=160)
plt.close()

plt.figure(figsize=(8, 5))
plt.scatter(df["Distance_km"], df["Transportation_Cost_INR"], alpha=0.7)
plt.title("Distance vs Transportation Cost")
plt.xlabel("Distance (km)")
plt.ylabel("Transportation cost (INR)")
plt.tight_layout()
plt.savefig(OUT / "distance_vs_cost.png", dpi=160)
plt.close()

plt.figure(figsize=(8, 5))
plt.scatter(df["Shipment_Volume_Units"], df["Transportation_Cost_INR"], alpha=0.7)
plt.title("Shipment Volume vs Transportation Cost")
plt.xlabel("Shipment volume (units)")
plt.ylabel("Transportation cost (INR)")
plt.tight_layout()
plt.savefig(OUT / "volume_vs_cost.png", dpi=160)
plt.close()

numeric = df.select_dtypes("number")
corr = numeric.corr()
plt.figure(figsize=(8, 6))
plt.imshow(corr, aspect="auto", vmin=-1, vmax=1)
plt.xticks(range(len(corr.columns)), corr.columns, rotation=45, ha="right")
plt.yticks(range(len(corr.index)), corr.index)
plt.colorbar(label="Correlation coefficient")
plt.title("Correlation Matrix of Numeric Variables")
plt.tight_layout()
plt.savefig(OUT / "correlation_matrix.png", dpi=160)
plt.close()

region_time = df.groupby("Region")["Delivery_Time_Days"].mean().sort_values()
region_time.plot(kind="bar", edgecolor="black", figsize=(8, 5))
plt.title("Average Delivery Time by Region")
plt.xlabel("Region")
plt.ylabel("Average delivery time (days)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(OUT / "delivery_time_by_region.png", dpi=160)
plt.close()

print(f"\nCharts saved in: {OUT}")
