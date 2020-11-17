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



""" all sorts of silly equations:
y = x3 − 5x
six(y) = sin(x^2/y)
(xy^2)/2 = y/x
(sin (y+1))/3 =cos(x)
(sin (y+1))/3 =cos(3x+1)


index -2/2, -2/2
    (xy^3)/2 +1 = y/x
    y^3/x + x^3/y^2 = y +1
    sin(x)+cos(y)=0.5
    x/(x^2 +y^2) = 4y/3
    11x+ 1/(x^2 +y^2) = 4y/3
    (x+3) * (x−2)^2 * (x+1)^3
    y = (x+2) * (x−1)^2 * (x+1)^3
    y = (x - 2) * (x + 1) * (x-1)^3
    y^2 = (2x+2)^3/6
    tan(x) = cos(y)
    tan(2x) = cos(3(y+1)/2)
    tan(3(x-1)) = cos(3(y+5)/2)


index 0-10, 0-100
    y = x^2
    y = (((x/2)^2)+7)
    y = x^2 - 2

"""
