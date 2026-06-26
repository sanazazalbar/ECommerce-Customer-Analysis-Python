import numpy as np

# Load CSV
data = np.genfromtxt(
    "ecommerce_customer_data.csv",
    delimiter=",",
    names=True,
    dtype=None,
    encoding="utf-8"
)

print("Data Loaded Successfully\n")

# Extract columns
customer_id = data['Customer_ID']
price = data['Product_Price'].astype(float)
quantity = data['Quantity'].astype(float)
total_amount = data['Total_Purchase_Amount'].astype(float)
returns = data['Returns'].astype(float)
age = data['Age'].astype(float)
churn = data['Churn'].astype(float)

print("\nData Extracted Successfully")


# Sales Analysis 

print("\n--- Sales Analysis ---")
print("Total Revenue:", np.sum(total_amount))
print("Average Order Value:", np.mean(total_amount))
print("Maximum Purchase:", np.max(total_amount))
print("Minimum Purchase:", np.min(total_amount))


# Customer Behavior

print("\n--- Customer Behavior ---")
print("Average Age:", np.mean(age))
print("Average Quantity:", np.mean(quantity))

# High-value customers
avg_spend = np.mean(total_amount)
high_spenders = customer_id[total_amount > avg_spend]
print("High Value Customers:", np.unique(high_spenders))


# Churn Analysis

print("\n--- Churn Analysis ---")

# Get unique churned customer IDs
churn_customers = np.unique(customer_id[churn == 1])

# Count churned customers
churn_count = len(churn_customers)

# Total unique customers
total_customers = len(np.unique(customer_id))

# Calculate churn rate
churn_rate = (churn_count / total_customers) * 100

# Show complete array 
np.set_printoptions(threshold=np.inf)

# Print results
print("Churn Rate (%):", churn_rate)

print("Churn Count:", churn_count)

print("Churned Customers:")
print(churn_customers)


#Customer Spending 

print("\n--- Customer Spending ---")

unique_customers, indices = np.unique(customer_id, return_inverse=True)

customer_spending = np.bincount(indices, weights=total_amount)

print("Average Customer Spending:", np.mean(customer_spending))
print("Top Customer Spending:", np.max(customer_spending))


# Correlation

print("\n--- Correlation Analysis ---")
correlation = np.corrcoef(quantity, total_amount)
print("Quantity vs Total Amount Correlation:\n", correlation)


# Distribution

print("\n--- Spending Distribution ---")
hist, bins = np.histogram(total_amount, bins=5)

for i in range(len(hist)):
    print(f"Range {int(bins[i])} - {int(bins[i+1])} : {hist[i]} customers")


# Outlier Detection 

mean = np.mean(total_amount)
std = np.std(total_amount)

outliers = total_amount[np.abs(total_amount - mean) > 2 * std]
print("\nOutliers:", outliers)


#  Performance Report 

print("\n--- Customer Performance ---")

status = np.where(total_amount > avg_spend, "High", "Low")

for i in range(min(10, len(customer_id))):
    print(f"Customer {customer_id[i]}: {total_amount[i]} -> {status[i]}")





