import numpy as np
import matplotlib.pyplot as plt

# Generate the sequences
t = np.arange(0.0, 3.0, 0.02)
t2 = np.arange(0.0, 3.0, 0.2)

# Compute the required values
y1 = t**2
y2 = np.cos(3 * np.pi * t)
y3 = t**2 * np.cos(3 * np.pi * t)
y4 = np.sqrt(1 + t2)

# Create the plot
plt.figure()

# Plot the three lines with the specified styles
plt.plot(t, y1, 'b-', label='Square')
plt.plot(t, y2, 'y--o', label='Oscillatory')
plt.plot(t, y3, 'g-.s', label='Damped')

# Plot the additional sequence with dot markers
plt.plot(t2, y4, 'r.', label='Square Root')

# Add the legend with the specified labels and shadow
plt.legend(loc='upper left', shadow=True)

# Label the axes and add the title
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Damped oscillation')

# Save the plot to a PNG file
plt.savefig('novice_final.png')

# Show the plot
plt.show()