import matplotlib.pyplot as plt
import numpy as np

# Import the necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Prepare the data for plotting
x = np.arange(0.0, 3.02, 0.02)
y1 = x**2
y2 = np.cos(3*np.pi*x)
y3 = y1 * y2
y4 = np.sqrt(1 + x)

# Create the plot with the specified lines and markers
plt.figure()

plt.plot(x, y1, label='Square', color='blue')
plt.plot(x, y2, label='Oscillatory', linestyle='--', marker='o', color='orange')
plt.plot(x, y3, label='Damped', linestyle='-.', color='green')  # Corrected linestyle
plt.plot(x, y4, label='Square Root', marker='.', color='red')

plt.legend(loc='upper left', shadow=True)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Damped oscillation')

plt.savefig('novice.png')
plt.show()