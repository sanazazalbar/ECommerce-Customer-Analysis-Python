# 🛒 E-Commerce Customer Analysis using Python & NumPy

## 📌 Project Overview
Analyzed an e-commerce customer dataset using **Python and 
NumPy** — without Pandas — to perform sales analysis, churn 
detection, outlier detection, and customer segmentation 
across 7 key data dimensions.

## 🛠 Tools Used
- Python 3.x
- NumPy
- CSV (data loading)
- Jupyter / Python Script

## 📂 Dataset Columns Analyzed
Customer_ID, Product_Price, Quantity, Total_Purchase_Amount,
Returns, Age, Churn

## 🔍 Analysis Performed (9 modules)

| # | Analysis | Method Used |
|---|---|---|
| 1 | Sales Performance | np.sum(), np.mean(), np.max(), np.min() |
| 2 | Customer Behavior | Age & quantity averages |
| 3 | High-Value Customers | Filtered above avg spend |
| 4 | Churn Rate | (Churned / Total) × 100 |
| 5 | Customer Spending | np.bincount() with weights |
| 6 | Correlation Analysis | np.corrcoef(quantity, total_amount) |
| 7 | Spending Distribution | np.histogram() with 5 bins |
| 8 | Outlier Detection | Mean ± 2×Standard Deviation |
| 9 | Performance Classification | np.where() → High/Low labels |

## 📊 Key Metrics Generated
- Total Revenue, Average Order Value (AOV)
- Churn Rate % across unique customers
- Quantity vs Purchase Amount correlation
- Spending ranges across 5 distribution buckets
- Outlier transactions beyond 2 standard deviations

## ⚙️ How to Run
python projectnumpy.py

Ensure ecommerce_customer_data.csv is in the same folder.

## 💡 Key Highlights
- Pure NumPy analysis — no Pandas dependency
- End-to-end pipeline: load → clean → analyze → report
- 11 NumPy functions used across 9 analysis modules
- Churn rate calculated on unique customer level

## 🚀 Conclusion
Demonstrates end-to-end customer analytics using core 
NumPy operations — proving strong numerical computing 
and data analysis skills without high-level frameworks.
