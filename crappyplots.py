### don't use. trying to get both the indexes and legends removed as well as the bgcolor and draw colors fixed.

import matplotlib.pyplot as plt
import numpy as np

# Create the vectors X and Y
x = np.array(range(10))
ya = np.square(x)
yb = (np.square(x / 2) * 2 ) + 7
yc = np.square(x) - 2
yd = np.tan(x)


fig = plt.figure(frameon=False)
plt.plot(x, ya, 'w')
plt.plot(x, yb, 'w')
plt.plot(x, yc, 'w')
plt.plot(x, np.tan(yd), 'w')
ax = plt.Axes(fig, [0., 0., 1., 1.])
ax.set_axis_off()
fig.add_axes(ax)
ax.imshow(plt.show, aspect='auto')
#plt.show()
