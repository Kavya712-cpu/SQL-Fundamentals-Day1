import pandas as pd

# Sample dataset
df = pd.DataFrame({
    "CustomerID": [1, 2, 3, 4],
    "Name": ["Amit", "Priya", "Rahul", "Sneha"],
    "Age": [25, 30, 22, 28],
    "Email": [
        "amit@gmail.com",
        "priya@gmail.com",
        "rahul@gmail.com",
        "sneha@gmail.com"
    ]
})

print("Shape:", df.shape)
print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

print("\nData Types:")
print(df.dtypes)