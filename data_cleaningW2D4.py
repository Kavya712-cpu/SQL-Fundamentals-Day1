import pandas as pd
import numpy as np

# Sample dataset
data = {
    "Name": ["Amit", "Priya", "Rahul", "Priya", "Sneha"],
    "Age": [25, np.nan, 30, 28, 150],
    "City": [" Bangalore", "mumbai", "Delhi ", "Mumbai", "bangalore"]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing values with mean
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Remove duplicates
df = df.drop_duplicates()

# Standardize text
df["City"] = df["City"].str.strip().str.title()

# IQR Outlier Detection
Q1 = df["Age"].quantile(0.25)
Q3 = df["Age"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df = df[(df["Age"] >= lower) & (df["Age"] <= upper)]

print("\nCleaned Data:")
print(df)

# Save cleaned dataset
df.to_csv("cleaned_dataset.csv", index=False)

print("\nDataset cleaned successfully.")