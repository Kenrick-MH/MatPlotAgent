import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the CSV file
file_path = 'Sales Invoice ERP Mei.csv'
data = pd.read_csv(file_path)

# Step 2: Process the data
# Convert the 'Date' column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Group by date and sum the 'Grand Total'
daily_totals = data.groupby('Date')['Grand Total'].sum().reset_index()

# Step 3: Create the scatter plot
plt.figure(figsize=(12, 6))
plt.scatter(daily_totals['Date'], daily_totals['Grand Total'], color='green')
plt.plot(daily_totals['Date'], daily_totals['Grand Total'], color='green')

# Step 4: Adjust the y-axis scale to the order of hundreds
plt.ylim(0, (daily_totals['Grand Total'].max() // 100 + 1) * 100)  # Adjusting y-axis scale to the order of hundreds

# Step 5: Add labels and title
plt.xlabel('Date')
plt.ylabel('Total Amount')
plt.title('Money Gained Each Day')

# Step 6: Save the plot
plt.savefig('novice_final.png')

# Show the plot
plt.show()