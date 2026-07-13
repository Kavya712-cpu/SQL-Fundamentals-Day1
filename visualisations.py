import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load sample dataset
df = sns.load_dataset("tips")

# Apply seaborn theme
sns.set_theme(style="whitegrid")

# -------------------------
# 1. Line Chart
# -------------------------
plt.figure(figsize=(6,4))
daily = df.groupby("day")["total_bill"].mean()
plt.plot(daily.index, daily.values, marker="o")
plt.title("Average Bill by Day")
plt.xlabel("Day")
plt.ylabel("Average Bill")
plt.savefig("line_chart.png")
plt.show()

# -------------------------
# 2. Bar Chart
# -------------------------
plt.figure(figsize=(6,4))
sns.barplot(data=df, x="day", y="total_bill")
plt.title("Total Bill by Day")
plt.savefig("bar_chart.png")
plt.show()

# -------------------------
# 3. Scatter Plot
# -------------------------
plt.figure(figsize=(6,4))
sns.scatterplot(data=df, x="total_bill", y="tip", hue="sex")
plt.title("Total Bill vs Tip")
plt.savefig("scatter_plot.png")
plt.show()

# -------------------------
# 4. Histogram
# -------------------------
plt.figure(figsize=(6,4))
plt.hist(df["total_bill"], bins=10)
plt.title("Distribution of Total Bill")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")
plt.savefig("histogram.png")
plt.show()

# -------------------------
# 5. Box Plot
# -------------------------
plt.figure(figsize=(6,4))
sns.boxplot(data=df, x="day", y="total_bill")
plt.title("Total Bill Distribution by Day")
plt.savefig("box_plot.png")
plt.show()

print("All charts created successfully!")