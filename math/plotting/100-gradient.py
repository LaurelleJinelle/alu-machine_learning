#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

np.random.seed(5)

x = np.random.randn(2000) * 10
y = np.random.randn(2000) * 10
z = np.random.rand(2000) + 40 - np.sqrt(np.square(x) + np.square(y))

colors = ['blue', 'green', 'yellow']
cmap = LinearSegmentedColormap.from_list('custom_cmap', colors)

scatter = plt.scatter(x, y, c=z, cmap=cmap)

plt.xlabel('x coordinate (m)')
plt.ylabel('y coordinate (m)')
plt.title('Mountain Elevation')

cbar = plt.colorbar(scatter)
cbar.set_label('elevation (m)')

plt.show()
