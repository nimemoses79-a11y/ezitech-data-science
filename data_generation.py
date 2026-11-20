
import pandas as pd
import random

# Make results reproducible
random.seed(42)

# Product categories
categories = [
    "Laptop",
    "Smartphone",
    "Headphones",
    "Monitor",
    "Keyboard"
]

# Generate 50 electronic products
products = []

for i in range(1, 51):
    products.append({
        "product_id": f"P{i:03d}",
        "category": categories[(i - 1) // 10],
        "price": round(random.uniform(500, 80000), 2)
    })

# Generate 365 days of sales data
dates = pd.date_range(
    end=pd.Timestamp("2026-11-20"),
    periods=365,
    freq="D"
)

sales_records = []

for date in dates:
    for product in products:
        sales_records.append({
            "product_id": product["product_id"],
            "category": product["category"],
            "price": product["price"],
            "units_sold": random.randint(0, 30),
            "date": date.strftime("%Y-%m-%d")
        })

# Create DataFrame
df = pd.DataFrame(sales_records)

# Save dataset as CSV
df.to_csv("sales_data.csv", index=False)

print("Sales dataset generated successfully!")
print("Total records:", len(df))
print("Total products:", df["product_id"].nunique())
print("Total days:", df["date"].nunique())
print("\nFirst five records:")
print(df.head())
