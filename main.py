import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# Read CSV Data
df = pd.read_csv("sales.csv")

# display missing data's number
missing = df.isnull().sum()
print("=== Missing Data ===")
print(missing[missing > 0])

# Delete rows with missing values
df_clean = df.dropna()

# Display avarage sales by item categories
avg_sales = df_clean.groupby("category")["sales"].mean()
print("\n=== Avarage Sales in each category ===")
print(avg_sales)

#seaborn as the graph style
sns.set(style="whitegrid", palette="pastel")

# make a graph
avg_sales.plot(kind="bar", color= "skyblue", edgecolor = "black")
plt.title("Avarage Sales by Product Category")
plt.xlabel("Category")
plt.ylabel("Avarge Sales")
plt.tight_layout()

#save shown graphes
plt.savefig("avg_avg_sales_by_category.png")
plt.show()

#calculate the daily sales' sum
daily_sales = df_clean.groupby("date")["sales"].sum()
print("\n=== daily sum of sales ===")
print(daily_sales)

#display Line chart
plt.figure()
daily_sales.plot(kind="line", marker="o", linestyle="-", color="green")
plt.title("Total Sales by Date")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.xticks(rotation = 45)
plt.tight_layout()
plt.savefig("daily_sales_line_chart.png")
plt.show()
