import pandas as pd

# ----------------------------
# Create two DataFrames
# ----------------------------
customers = pd.DataFrame({
    "CustomerID": [1, 2, 3, 4],
    "Name": ["Amit", "Priya", "Rahul", "Sneha"]
})

orders = pd.DataFrame({
    "CustomerID": [1, 2, 2, 5],
    "Product": ["Laptop", "Phone", "Tablet", "Camera"],
    "Amount": [50000, 20000, 30000, 25000]
})

# ----------------------------
# Merge Examples
# ----------------------------
print("Inner Join")
print(pd.merge(customers, orders, on="CustomerID", how="inner"))

print("\nLeft Join")
print(pd.merge(customers, orders, on="CustomerID", how="left"))

print("\nRight Join")
print(pd.merge(customers, orders, on="CustomerID", how="right"))

print("\nOuter Join")
print(pd.merge(customers, orders, on="CustomerID", how="outer"))

# ----------------------------
# Pivot Table
# ----------------------------
sales = pd.DataFrame({
    "Region": ["North", "North", "South", "South"],
    "Product": ["Laptop", "Phone", "Laptop", "Phone"],
    "Sales": [100, 150, 200, 180]
})

pivot = sales.pivot_table(
    values="Sales",
    index="Region",
    columns="Product",
    aggfunc="sum"
)

print("\nPivot Table")
print(pivot)

# ----------------------------
# Melt Example
# ----------------------------
wide = pd.DataFrame({
    "Student": ["A", "B"],
    "Math": [80, 90],
    "Science": [85, 95]
})

long = pd.melt(
    wide,
    id_vars="Student",
    var_name="Subject",
    value_name="Marks"
)

print("\nMelt Example")
print(long)

# ----------------------------
# Method Chaining
# ----------------------------
result = (
    sales
    .query("Sales > 120")
    .sort_values("Sales")
)

print("\nMethod Chaining")
print(result)