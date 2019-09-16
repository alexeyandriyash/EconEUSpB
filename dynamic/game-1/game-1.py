import numpy as np
import matplotlib.pyplot as plt

header = 'Game#1 by Andriyash, Babkina, Tokareva'
plotTitle = r'$\frac{dy}{dx} = y^2 - x^2$'
scale = 1.0
D = 10

#get x, y vector of points
oX = np.linspace(-scale, scale, D)
oY = np.linspace(-scale, scale, D)

#get grid of points
vX, vY = np.meshgrid(oX, oY)
deg = np.arctan(vY*vY-vX*vX)
dx = np.cos(deg)
dy = np.sin(deg)

plt.figure(header)
plt.title(plotTitle)
QP = plt.quiver(vX, vY, dx, dy)
#plt.scatter(vX, vY, color='r', s=5)
#plt.scatter(vX, vY, color='0.8', s=1)

plt.show()