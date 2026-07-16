import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load sample dataset
df = sns.load_dataset("tips")

# Dataset information
print("Shape:", df.shape)
print("\nData Types:")
print(df.dtypes)

print("\nNull Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

print("\nSummary Statistics:")
print(df.describe())

# Distribution plots
df.hist(figsize=(10,8))
plt.suptitle("Distribution of Numeric Columns")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(6,4))
numeric_df = df.select_dtypes(include="number")
sns.heatmap(numeric_df.corr(), annot=True, cmap="Blues")
plt.title("Correlation Heatmap")
plt.show()

# Business Insights
print("\nBusiness Insights:")
print("1. Higher total bills usually have higher tips.")
print("2. Dinner bills are generally higher than lunch bills.")
print("3. Most customers spend between $10 and $20.")
print("4. Weekends have higher restaurant bills.")
print("5. Male and female customers have similar spending patterns.")