import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('sales_data_analysis.csv')

print(data.head())

total_revenue = data.groupby('Product_Category')['Revenue'].sum().reset_index()

plt.figure(figsize=(10, 6))
plt.bar(total_revenue['Product_Category'], total_revenue['Revenue'], color='skyblue')
plt.title('Total Revenue by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.grid(axis='y')

plt.tight_layout()
plt.show()

total_units_sold = data.groupby('Product_Category')['Units_Sold'].sum().reset_index()

plt.figure(figsize=(8, 8))
plt.pie(total_units_sold['Units_Sold'], labels=total_units_sold['Product_Category'], autopct='%1.1f%%', startangle=140)
plt.title('Proportion of Total Units Sold by Product Category')

plt.axis('equal')
plt.show()
