import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = pd.read_csv('Sales Invoice ERP Mei.csv')

# Convert the 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Group the data by 'Date' and sum the 'Grand Total' for each day
daily_sales = data.groupby('Date')['Grand Total'].sum().reset_index()

# Create a scatter plot to visualize the fluctuating trend
plt.figure(figsize=(12, 6))
plt.scatter(daily_sales['Date'], daily_sales['Grand Total'], color='blue', marker='o')
plt.title('Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Grand Total')
plt.yscale('log')  # Adjust the scale for the grand total to be in the order of hundreds
plt.savefig('novice.png')
plt.show()

# Create a line plot to visualize the money gained each day by summing the entries in 'Grand Total' for each day
plt.figure(figsize=(12, 6))
plt.plot(daily_sales['Date'], daily_sales['Grand Total'], color='green', marker='o', linestyle='-')
plt.title('Money Gained Each Day')
plt.xlabel('Date')
plt.ylabel('Total Amount')
plt.yscale('log')  # Adjust the scale for the grand total to be in the order of hundreds
plt.savefig('novice.png')
plt.show()