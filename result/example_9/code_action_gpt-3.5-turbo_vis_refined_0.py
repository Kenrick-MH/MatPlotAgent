import matplotlib.pyplot as plt
import numpy as np

# Generate data
x = np.arange(0.0, 10.0, 0.02)
y = np.sin(3 * np.pi * x)

# Create figure
fig, ax = plt.subplots(figsize=(4, 4))

# Plot data
ax.plot(x, y)

# Annotate midpoint
mid_x = 5
mid_y = np.sin(3 * np.pi * mid_x)
ax.annotate('Midpoint', xy=(mid_x, mid_y), xytext=(mid_x + 1, mid_y + 1),
            arrowprops=dict(facecolor='black', shrink=0.05))

# Find peak
peak_x = x[np.argmax(y)]
peak_y = np.max(y)
ax.annotate('Peak', xy=(peak_x, peak_y), xytext=(peak_x + 1, peak_y + 1),
            arrowprops=dict(facecolor='black', shrink=0.05))

# Annotate specific data point
specific_x = 4
specific_y = np.sin(12 * np.pi)
ax.annotate('data point (4, sin(12pi))', xy=(specific_x, specific_y), xytext=(specific_x + 1, specific_y - 1),
            arrowprops=dict(facecolor='black', shrink=0.05))

# Add text annotations
ax.text(0, 1, 'Sine Curve', transform=ax.transAxes, fontsize=12, verticalalignment='top')
fig.text(1, 0, 'Created by PlotAgent', fontsize=8, verticalalignment='bottom', horizontalalignment='right')

# Set axis limits
ax.set_xlim(-2, 10)
ax.set_ylim(-6, 6)

# Save the plot
plt.savefig('novice_final.png')

# Show plot
plt.show()