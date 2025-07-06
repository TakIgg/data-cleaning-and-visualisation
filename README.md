
# 📊 Data Cleaning Project

  My second project to clean and analyze sales data using Python and pandas.

## 📊 Visualization Added

This version includes a bar chart and a line chart showing average sales per product category.

- Bar chart of average sales per product category (`avg_sales_by_category.png`)
- Line chart of total sales per day (`daily_sales_line_chart.png`)
- Charts are automatically saved as image files

### 📈 Graph example:
plt.savefig(data_graph.pnger)
```python
import matplotlib.pyplot as plt

avg_sales.plot(kind="bar")
plt.title("Average Sales by Product Category")
plt.show()

## 🔧 What this project does

  - Load sales data from a CSV file (`sales.csv`)
  - Check for missing values and clean the data
  - Group by product category and calculate average sales

## 📁 Files

  - `sales.csv`: Sample sales data
  - `main.py`: Python script to clean and analyze the data

## ▶️ How to run

1. Install pandas:
   ```bash
   pip install pandas

## Run the script
  python main.py
  
## Output Example
  === Missing Data ===
  date        0
  item        1
  category    0
  sales       1
  quantity    0
  dtype: int64
  
  === Avarage Sales in each category ===
  category
  A    516.666667
  B    100.000000
  Name: sales, dtype: float64

## 📚 Skills used
  Python
  pandas
  CSV data handling