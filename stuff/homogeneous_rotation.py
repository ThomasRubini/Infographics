import math
import numpy as np

#     Rotation process:
#     1 - Convert point to a 3x1 vector
#     2 - Translate point to origin (0, 0)
#     3 - Rotate point according to origin point
#     4 - Translate in the other way point to new position

#     point_vector = np.array([x, y, 1])

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import numpy as np


x = np.array([-0.1,   -0.1, 0.1, 0.1]).astype(float)
y = np.array([-0.1, 0.1, 0.1,   -0.1]).astype(float)
z = np.array([1,   1,   1,   1]).astype(float)
n = len(x)

Theta = math.pi/64
Tm = np.array([[math.cos(Theta), -math.sin(Theta), 0],
               [math.sin(Theta),  math.cos(Theta), 0],
               [              0,                0, 1]])

fig, ax1 = plt.subplots()

ax1.set_aspect('equal', adjustable='box')
# bounding box zoom
ax1.set_xlim(-1, 1)
ax1.set_ylim(-1, 1)

def update(frame):
    # print("New frame", "="*80)
    for point_i in range(n):
        x[point_i], y[point_i], z[point_i] = Tm @ np.array([x[point_i], y[point_i], z[point_i]])
    # print(x, y, z)
    return ax1.fill(x, y, color="blue")

# nombre d'itération
frames = np.linspace(0, 1, 10000)

# attente entre chaque itération
interval = 0.01
ani = FuncAnimation(fig, update, frames=frames, interval=interval, blit=True)

plt.show()
