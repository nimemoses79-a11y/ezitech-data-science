import matplotlib.pyplot as plt
import pandas as pd

# Load the sales dataset
df = pd.read_csv("sales_data.csv")

# Calculate total revenue
df["revenue"] = df["price"] * df["units_sold"]

# Display basic information
print("===== SALES DATA ANALYSIS =====")

print("\nTotal Records:", len(df))
print("Total Units Sold:", df["units_sold"].sum())
print("Total Revenue:", round(df["revenue"].sum(), 2))
print("Average Price:", round(df["price"].mean(), 2))

# Sales by category
category_sales = df.groupby("category")["revenue"].sum()

print("\n===== REVENUE BY CATEGORY =====")
print(category_sales.sort_values(ascending=False))

# Best-selling categories by quantity
best_selling = df.groupby("category")["units_sold"].sum()

print("\n===== UNITS SOLD BY CATEGORY =====")
print(best_selling.sort_values(ascending=False))

print("\n===== BEST-SELLING CATEGORY =====")
print(best_selling.idxmax())

print("\n===== LOWEST-SELLING CATEGORY =====")
print(best_selling.idxmin())

# ===== REVENUE CHART =====
plt.figure(figsize=(10, 6))

category_sales.sort_values(ascending=False).plot(kind="bar")

plt.title("Revenue by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("revenue_chart.png")
plt.show()