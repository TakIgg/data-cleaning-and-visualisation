import pandas as pd

# Read CSV Data
df = pd.read_csv("sales.csv")

# display missing data's number
print("=== Missing Data ===")
print(df.isnull().sum())

# Delete rows with missing values
df_clean = df.dropna()

# Display avarage sales by item categories商品カテゴリごとの売上平均を計算して表示
print("\n=== Avarage Sales in each category ===")
print(df_clean.groupby("category")["sales"].mean())
