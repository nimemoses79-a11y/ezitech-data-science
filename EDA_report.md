# VoltMart Sales Data – Exploratory Data Analysis Report

## 1. Overview
This analysis explores VoltMart's sales dataset to understand product pricing, monthly sales trends, and category demand.

The dataset contains **18,250 records** and five original columns: product ID, category, price, units sold, and date.

2. Data Quality and Cleaning

- The original data generation script does not intentionally generate missing (NaN) values.
- No missing-value removal or replacement operation is performed during dataset generation.
- Inspection of the saved CSV confirmed that no missing values were present.
- No duplicate records were detected.
- The date column was converted into datetime format during exploratory analysis.
- A revenue column was calculated using price multiplied by units sold.
- The cleaned dataset retains all 18,250 records.

## 3. Key Pricing Insights
- Average product price: **36,329.40**.
- Median product price: **37,359.26**.
- Minimum product price: **1,016.65**.
- Maximum product price: **77,862.70**.
- No price outliers were detected using the IQR method.

## 4. Category Performance
- Monitors generated the highest total revenue, approximately **2.999 billion**.
- Laptops recorded the highest total units sold, with **55,764 units**.
- Keyboards had the lowest average selling price, approximately **24,030.07**.

## 5. Visualizations
The following charts were generated and saved:

- `price_distribution.png` – Shows the distribution of product prices.
- `monthly_sales_trend.png` – Shows monthly changes in total sales revenue.
- `category_demand_heatmap.png` – Compares units sold across product categories and months.

## 6. Conclusion
The analysis shows that product categories differ in pricing, revenue, and demand. Monitors contribute the highest revenue, while laptops have the highest sales volume. No missing values, duplicate records, or price outliers were identified.

These findings can help VoltMart understand its sales performance and support future pricing decisions.