# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# Load the dataset
df = pd.read_excel("superstore_sales.xlsx")

# Display first few rows
print(df.head())

# Data Cleaning
df['order_date'] = pd.to_datetime(df['order_date'])
df['ship_date'] = pd.to_datetime(df['ship_date'])

# Adding month_year column for time series analysis
df['month_year'] = df['order_date'].apply(lambda x: x.strftime('%Y-%m'))

# Exploratory Data Analysis (EDA)

# 1. Overall Sales Trend
sales_trend = df.groupby('month_year')['sales'].sum().reset_index()

plt.figure(figsize=(16, 5))
plt.plot(sales_trend['month_year'], sales_trend['sales'], color='#b80045')
plt.xticks(rotation='vertical', size=8)
plt.title('Overall Sales Trend')
plt.show()

# 2. Sales by Category
sales_by_category = df.groupby('category')['sales'].sum().reset_index()

fig = px.pie(sales_by_category, values='sales', names='category', title='Sales by Category', hole=0.5)
fig.show()

# 3. Sales by Sub-Category
sales_by_subcategory = df.groupby('sub_category')['sales'].sum().reset_index()

fig = px.bar(sales_by_subcategory, x='sub_category', y='sales', title='Sales by Sub-Category')
fig.show()

# 4. Monthly Profits
profit_by_month = df.groupby('month_year')['profit'].sum().reset_index()

fig = px.line(profit_by_month, x='month_year', y='profit', title='Monthly Profit Analysis')
fig.show()

# 5. Profit by Category
profit_by_category = df.groupby('category')['profit'].sum().reset_index()

fig = px.pie(profit_by_category, values='profit', names='category', title='Profit by Category', hole=0.5)
fig.show()

# 6. Profit by Sub-Category
profit_by_subcategory = df.groupby('sub_category')['profit'].sum().reset_index()

fig = px.bar(profit_by_subcategory, x='sub_category', y='profit', title='Profit by Sub-Category')
fig.show()

# 7. Sales and Profit by Customer Segments
sales_profit_by_segment = df.groupby('segment').agg({'sales': 'sum', 'profit': 'sum'}).reset_index()

fig = go.Figure()
fig.add_trace(go.Bar(x=sales_profit_by_segment['segment'], y=sales_profit_by_segment['sales'], name='Sales'))
fig.add_trace(go.Bar(x=sales_profit_by_segment['segment'], y=sales_profit_by_segment['profit'], name='Profit'))
fig.update_layout(title='Sales and Profit by Customer Segment', xaxis_title='Segment', yaxis_title='Amount')
fig.show()

# 8. Sales to Profit Ratio by Segment
sales_profit_by_segment['Sales_to_Profit_Ratio'] = sales_profit_by_segment['sales'] / sales_profit_by_segment['profit']
print(sales_profit_by_segment[['segment', 'Sales_to_Profit_Ratio']])

# 9. Top 10 Products by Sales
top_products_by_sales = df.groupby('product_name')['sales'].sum().sort_values(ascending=False).head(10)
print(top_products_by_sales)

# 10. Most Selling Products
most_selling_products = df.groupby('product_name')['quantity'].sum().sort_values(ascending=False).head(10)
print(most_selling_products)

# 11. Most Preferred Ship Mode
plt.figure(figsize=(10, 8))
sns.countplot(x='ship_mode', data=df)
plt.title('Most Preferred Ship Mode')
plt.show()

# 12. Most Profitable Category and Sub-Category
profit_by_cat_subcat = df.groupby(['category', 'sub_category'])['profit'].sum().sort_values(ascending=False)
print(profit_by_cat_subcat.head(10))
