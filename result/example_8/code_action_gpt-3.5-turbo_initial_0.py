import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import hsv_to_rgb

# Set a fixed random state for reproducibility
np.random.seed(0)

# Generate random radial distances and angles for 200 points
num_points = 200
radial_distances = np.random.rand(num_points)
angles = np.random.rand(num_points) * 2 * np.pi

# Calculate x and y coordinates from polar coordinates
x = radial_distances * np.cos(angles)
y = radial_distances * np.sin(angles)

# Calculate the area of each point proportional to the square of its radial distance
area = np.pi * (radial_distances ** 2)

# Calculate the color of each point based on its angle in the HSV color space
colors = np.stack([angles / (2 * np.pi), np.ones(num_points), np.ones(num_points)], axis=-1)
colors = hsv_to_rgb(colors)

# Create the scatter plot with polar projection
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
sc = ax.scatter(angles, radial_distances, s=area * 1000, c=colors)

plt.savefig('novice.png')
plt.show()