import numpy as np
import matplotlib.pyplot as plt

header = 'Game#1 by Andriyash, Babkina, Tokareva'
plotTitle = r'$\frac{dy}{dx} = y^2 - x^2$'
scale = 1000.0
D = 30

#get x, y vector of points
oX = np.linspace(-scale, scale, D)
oY = np.linspace(-scale, scale, D)

#get grid of points
vX, vY = np.meshgrid(oX, oY)
deg = np.arctan(vX*vX - vY*vY)
dx = np.cos(deg)
dy = np.sin(deg)

plt.figure(header)
plt.title(plotTitle)
QP = plt.quiver(vX, vY, dx, dy, deg, units='x')
plt.scatter(vX, vY, color='r', s=5)
plt.scatter(vX, vY, color='0.8', s=1)

plt.show()