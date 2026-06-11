E-Commerce Customer Data Analysis using NumPy
📌 Project Overview

This project is an E-Commerce Customer Data Analysis System developed using Python and NumPy. The application processes customer purchase data from a CSV file and generates valuable business insights related to sales performance, customer behavior, spending patterns, churn analysis, and outlier detection.

The project demonstrates the practical use of NumPy for data analysis without relying on advanced data science libraries, making it an excellent example of numerical computing and business analytics using core Python tools.

🎯 Objectives
Analyze e-commerce customer purchasing behavior.
Calculate key sales performance metrics.
Identify high-value customers.
Measure customer churn rate.
Detect unusual spending patterns and outliers.
Generate business insights for decision-making.
🛠️ Technologies Used
Python 3.x
NumPy
CSV Dataset
📂 Dataset Attributes

The dataset contains the following fields:

Column Name	Description
Customer_ID	Unique customer identifier
Product_Price	Price of purchased product
Quantity	Quantity purchased
Total_Purchase_Amount	Total transaction amount
Returns	Product return indicator
Age	Customer age
Churn	Customer churn status
🚀 Features
1. Data Loading and Processing
Loads customer data from a CSV file using NumPy.
Extracts relevant columns for analysis.
2. Sales Analysis
Total Revenue
Average Order Value
Maximum Purchase Amount
Minimum Purchase Amount
3. Customer Behavior Analysis
Average Customer Age
Average Quantity Purchased
High-Value Customer Identification
4. Churn Analysis
Calculates Churn Rate
Identifies Churned Customers
Counts Total Churned Customers
5. Customer Spending Analysis
Calculates average customer spending.
Identifies top-spending customers.
6. Correlation Analysis
Measures correlation between:
Quantity Purchased
Total Purchase Amount
7. Spending Distribution
Generates spending ranges using histograms.
Shows customer distribution across spending categories.
8. Outlier Detection
Detects unusual purchase amounts using statistical methods.
Identifies transactions significantly different from average spending.
9. Customer Performance Report
Classifies customers as:
High Spending
Low Spending
📊 NumPy Functions Used
np.genfromtxt()
np.sum()
np.mean()
np.max()
np.min()
np.unique()
np.bincount()
np.corrcoef()
np.histogram()
np.where()
np.std()
📈 Sample Analysis Outputs
Total Revenue Generated
Average Order Value
High-Value Customers List
Churn Rate Percentage
Customer Spending Statistics
Quantity vs Spending Correlation
Spending Distribution Report
Outlier Transactions
Customer Performance Classification
