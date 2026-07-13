import pandas as pd

# Load CSV
df = pd.read_csv("sales.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Information
print("\nDataset Info:")
df.info()

# Summary Statistics
print("\nSummary Statistics:")
print(df.describe())

# Value Counts
print("\nCustomers by City:")
print(df["City"].value_counts())

# Filter rows
print("\nCustomers with Amount > 5000:")
print(df[df["Amount"] > 5000])

# Select columns
print("\nCustomer Name and Amount:")
print(df[["Customer_name", "Amount"]])

# Group By
print("\nTotal Amount by City:")
print(df.groupby("City")["Amount"].sum())

# Handle missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Export cleaned data
df.to_csv("cleaned_sales.csv", index=False)

print("\nAnalysis completed successfully.")