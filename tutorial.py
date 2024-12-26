#1 hosptial patiend data managment
import pandas as pd
import numpy as np
random_numbers = np.random.randint(1, 51, size=20)
series = pd.Series(random_numbers)
print(series)

#2

S1 = pd.Series([ 10, 20, 30, 40], index=['A', 'B', 'C', 'D'])
S2 = pd.Series([5, 4, 6, 8], index=['A', 'B', 'C', 'D'])
print("S1:")
print(S1)
print("\nS2:")
print(S2)
product = S1 * S2
print("\nProduct of S1 and S2:")
print(product)

#3
data = [75, 78, 82, 86]
index = ['ENGLISH', 'HINDI', 'MATHS', 'SCIENCE']
series = pd.Series(data, index=index)
print(series)

#4
data = {
    'TCS': 350,'Reliance': 800,'L & T': 300,'Wipro': 150,'Capgemini': 400,'Accenture': 200,'DNV': 250,'KPMG': 150 }
profit_series = pd.Series(data)
print("Company Profits:")
print(profit_series)
companies_with_high_profit = profit_series[profit_series > 200]
print("\nCompanies with Profit Greater Than 200 Crores:")
print(companies_with_high_profit)

#5
data = {'Organization 1': 28800,'Organization 2': 38700,'Organization 3': 17800,'Organization 4': 46500, 'Organization 5': 37500 }
donation_series = pd.Series(data, dtype=float)
print("Original Donation Amounts:")
print(donation_series)
updated_donations = donation_series * 2
print("\nUpdated Donation Amounts (Doubled):")
print(updated_donations)

#6 a)
df = pd.read_csv('sales_data.csv')
print("DataFrame Loaded from CSV:")
print(df.head())

#b
df['Revenue'] = df['Units Sold'] * df['Unit Price']
print("\nDataFrame with Revenue Column:")
print(df.head())

#c
average_revenue_per_region = df.groupby('Region')['Revenue'].mean()
print("\nAverage Revenue Per Region:")
print(average_revenue_per_region)

#d
total_revenue_per_salesperson = df.groupby('Salesperson')['Revenue'].sum()
top_salesperson = total_revenue_per_salesperson.idxmax()
top_revenue = total_revenue_per_salesperson.max()
print("\nSalesperson with the Highest Total Revenue:")
print(f"Salesperson: {top_salesperson}")
print(f"Total Revenue: {top_revenue}")

#7 a)
df = pd.read_excel('Data_pool.xlsx')
print("DataFrame Loaded from Excel:")
print(df.head())

#b)
df['Average Assignment Score'] = df[['Assignment 1', 'Assignment 2']].mean(axis=1)
print("\nDataFrame with Average Assignment Score:")
print(df.head())
