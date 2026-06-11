# 🛒 E-Commerce Customer Data Analysis using NumPy

## 📌 Project Overview

The **E-Commerce Customer Data Analysis System** is a Python-based data analytics project that leverages **NumPy** to process and analyze customer purchase data from a CSV dataset.

The system generates actionable business insights related to customer behavior, sales performance, churn analysis, spending trends, and outlier detection. The project demonstrates how powerful business analytics can be performed using core Python and NumPy without relying on advanced data science frameworks such as Pandas.

This project is ideal for showcasing skills in:

* Data Analysis
* Numerical Computing
* Business Intelligence
* Customer Analytics
* Python Programming
* NumPy Operations

---

# 🎯 Objectives

The primary objectives of this project are:

* Analyze customer purchasing behavior.
* Calculate key sales performance metrics.
* Identify high-value customers.
* Measure customer churn rate.
* Detect unusual spending patterns.
* Generate meaningful business insights.
* Practice real-world data analysis using NumPy.

---

# 🛠️ Technologies Used

| Technology  | Purpose                   |
| ----------- | ------------------------- |
| Python 3.x  | Core Programming Language |
| NumPy       | Numerical Data Analysis   |
| CSV Dataset | Data Source               |

---

# 📂 Dataset Structure

The dataset contains customer transaction and behavioral information.

| Column Name           | Description                       |
| --------------------- | --------------------------------- |
| Customer_ID           | Unique customer identifier        |
| Product_Price         | Price of purchased product        |
| Quantity              | Quantity purchased                |
| Total_Purchase_Amount | Total amount spent in transaction |
| Returns               | Product return indicator          |
| Age                   | Customer age                      |
| Churn                 | Customer churn status             |

---

# 🚀 Features

## 1️⃣ Data Loading & Processing

* Reads customer data from a CSV file.
* Extracts required columns using NumPy.
* Cleans and prepares data for analysis.

---

## 2️⃣ Sales Performance Analysis

The system calculates:

* Total Revenue Generated
* Average Order Value (AOV)
* Maximum Purchase Amount
* Minimum Purchase Amount

### Metrics Generated

```text
Total Revenue
Average Order Value
Highest Purchase
Lowest Purchase
```

---

## 3️⃣ Customer Behavior Analysis

Provides insights into customer purchasing habits.

### Analysis Includes

* Average Customer Age
* Average Quantity Purchased
* High-Value Customer Identification

### Business Benefit

Helps companies understand:

* Customer demographics
* Buying patterns
* Premium customer segments

---

## 4️⃣ Churn Analysis

Evaluates customer retention and customer loss.

### Metrics

* Total Churned Customers
* Churn Rate Percentage
* Churned Customer List

### Formula

```text
Churn Rate = (Churned Customers / Total Customers) × 100
```

---

## 5️⃣ Customer Spending Analysis

Analyzes spending behavior across customers.

### Insights Generated

* Average Spending
* Above-Average Spenders
* Top Spending Customers

This helps businesses identify:

* VIP customers
* Loyalty targets
* Upselling opportunities

---

## 6️⃣ Correlation Analysis

Measures the relationship between:

* Quantity Purchased
* Total Purchase Amount

### Method Used

```python
np.corrcoef()
```

### Interpretation

| Correlation Value | Meaning                      |
| ----------------- | ---------------------------- |
| +1                | Strong Positive Relationship |
| 0                 | No Relationship              |
| -1                | Strong Negative Relationship |

---

## 7️⃣ Spending Distribution Analysis

Uses histograms to group customers into spending ranges.

### NumPy Function

```python
np.histogram()
```

### Example Output

```text
0 - 500
500 - 1000
1000 - 1500
1500 - 2000
```

This provides a visual understanding of customer spending behavior.

---

## 8️⃣ Outlier Detection

Detects unusual transactions that significantly differ from average spending.

### Statistical Method

```text
Outlier = Mean ± (2 × Standard Deviation)
```

### Purpose

Identify:

* Extremely high purchases
* Fraudulent transactions
* Unusual customer behavior

---

## 9️⃣ Customer Performance Classification

Customers are categorized based on spending patterns.

### Categories

#### High Spending Customers

Customers whose spending exceeds average spending.

#### Low Spending Customers

Customers whose spending falls below average spending.

This segmentation can be used for:

* Personalized marketing
* Customer retention campaigns
* Loyalty programs

---

# 📊 NumPy Functions Used

| Function        | Purpose                |
| --------------- | ---------------------- |
| np.genfromtxt() | Load CSV data          |
| np.sum()        | Calculate totals       |
| np.mean()       | Calculate averages     |
| np.max()        | Find maximum value     |
| np.min()        | Find minimum value     |
| np.unique()     | Identify unique values |
| np.bincount()   | Count occurrences      |
| np.corrcoef()   | Correlation analysis   |
| np.histogram()  | Distribution analysis  |
| np.where()      | Conditional filtering  |
| np.std()        | Standard deviation     |

---

# 📈 Sample Outputs

### Sales Metrics

```text
Total Revenue Generated
Average Order Value
Maximum Purchase Amount
Minimum Purchase Amount
```

### Customer Insights

```text
Average Customer Age
Average Quantity Purchased
High-Value Customers
```

### Churn Report

```text
Total Churned Customers
Churn Rate Percentage
```

### Correlation Analysis

```text
Quantity vs Purchase Amount Correlation
```

### Outlier Report

```text
Unusual Transactions Detected
```

### Spending Distribution

```text
Customer Spending Ranges
```

---

# 💡 Business Insights Generated

The project helps answer important business questions:

* Who are the highest-value customers?
* What is the average customer spending?
* How much revenue is being generated?
* What percentage of customers are churning?
* Are there unusual spending behaviors?
* Does purchasing quantity influence spending amount?

---

# 🎓 Learning Outcomes

By building this project, you will gain hands-on experience with:

* NumPy Arrays
* Statistical Analysis
* Customer Analytics
* Data Processing
* Business Intelligence Concepts
* Correlation Analysis
* Outlier Detection Techniques
* Real-World Data Analytics Workflows

---

# 🔮 Future Enhancements

Potential improvements include:

* Data Visualization using Matplotlib
* Interactive Dashboard
* Customer Segmentation Models
* Predictive Churn Analysis
* Machine Learning Integration
* Export Reports to Excel/PDF
* Real-Time Analytics

---

# 📜 Conclusion

This project demonstrates how NumPy can be used to perform comprehensive customer and sales analytics in an e-commerce environment. It showcases practical applications of numerical computing, statistical analysis, and business intelligence while strengthening core Python programming skills.

⭐ If you found this project useful, consider giving it a star on GitHub!
