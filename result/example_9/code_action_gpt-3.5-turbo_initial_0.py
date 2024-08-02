import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load data from a CSV file
data = pd.read_csv('data.csv')

# Prepare the data
x = np.arange(0.0, 10.0, 0.02)
y = np.sin(3 * np.pi * x)
midpoint = (5, np.sin(3 * np.pi * 5))
peak = (x[np.argmax(y)], np.max(y))
data_point = (4, np.sin(12 * np.pi))

# Create the figure and plot the sine curve
fig, ax = plt.subplots(figsize=(4, 4))
ax.plot(x, y, label='Sine Curve')
ax.set_xlim(-2, 10)
ax.set_ylim(-6, 6)

# Annotate the midpoint and peak
ax.annotate('Midpoint', midpoint, xytext=(midpoint[0], midpoint[1] + 1),
            arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('Peak', peak, xytext=(peak[0], peak[1] + 1),
            arrowprops=dict(facecolor='black', shrink=0.05))

# Annotate the data point with an arrow
ax.annotate('Data point (4, sin(12pi))', data_point, xytext=(data_point[0], data_point[1] - 1),
            arrowprops=dict(facecolor='black', shrink=0.05))

# Add text annotations
ax.text(0, 1, 'Sine Curve', transform=ax.transAxes, fontsize=12, verticalalignment='top')
fig.text(0.95, 0.05, 'Created by PlotAgent', fontsize=8, color='gray', ha='right', va='bottom', alpha=0.5)

# Save the plot to a png file
plt.savefig('novice.png')

# Show the plot
plt.show()