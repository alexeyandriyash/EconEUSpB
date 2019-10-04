import numpy as np
import matplotlib.pylab as plt
from scipy.integrate import odeint

header = 'Game#2 by Andriyash, Babkina, Tokareva'

color = ['red', 'green', 'blue', 'yellow',
         'magenta', 'olive', 'purple', 'pink',
         'red', 'green', 'blue', 'yellow',
         'magenta', 'olive', 'purple', 'pink',
         'red', 'green', 'blue', 'yellow',
         'magenta', 'olive', 'purple', 'pink',
         'red', 'green', 'blue', 'yellow',
         'magenta', 'olive', 'purple', 'pink',
         'red', 'green', 'blue', 'yellow',
         'magenta', 'olive', 'purple', 'pink',
         'red', 'green', 'blue', 'yellow',
         'magenta', 'olive', 'purple', 'pink',
         'red', 'green', 'blue', 'yellow',
         'magenta', 'olive', 'purple', 'pink',
         'red', 'green', 'blue', 'yellow',
         'magenta', 'olive', 'purple', 'pink',
         'red', 'green', 'blue', 'yellow',
         'magenta', 'olive', 'purple', 'pink',
         'red', 'green', 'blue', 'yellow',
         'magenta', 'olive', 'purple', 'pink'
         ]

samples = []
power = 3


def system(vect, time):
    x, y = vect
    return [y - 3 * x, 2 * y + x]


for i in range(20):
    samples.append((0.001 * i ** power, 0.001 * i ** power))
    samples.append((-0.001 * i ** power, -0.001 * i ** power))
    samples.append((-0.001 * i ** power, 0.001 * i ** power))
    samples.append((0.001 * i ** power, -0.001 * i ** power))

t = np.linspace(0, 1, 200)
plot = plt.figure(header)
plt.axes()
plt.grid(plot)

for i, v in enumerate(samples):
    sol = odeint(system, v, t)
    plt.quiver(sol[:-1, 0], sol[:-1, 1],
               sol[1:, 0] - sol[:-1, 0],
               sol[1:, 1] - sol[:-1, 1],
               scale_units='xy', angles='xy', scale=1, color=color[i])

plt.show(plot)
