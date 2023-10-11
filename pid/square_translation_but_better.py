import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import numpy as np

x = np.array([0, 0  , 0.2, 0.2])
y = np.array([0, 0.2, 0.2, 0  ])
z = np.array([1, 1  , 1  , 1  ])
n = len(x)

Tx = -0.1
Ty = 0.3
Tm = np.array([[1, 0, Tx],
               [0, 1, Ty],
               [0, 0, 1 ]])

fig, ax1 = plt.subplots()

ax1.set_xlim(-10, 10)
ax1.set_ylim(-10, 10)

def update(frame):
    print("New frame", "="*80)
    for point_i in range(n):
        x[point_i], y[point_i], z[point_i] = Tm @ np.array([x[point_i], y[point_i], z[point_i]])
    print(x, y, z)
    return ax1.fill(x, y, color="blue")

ani = FuncAnimation(fig, update, frames=np.linspace(0, 2, 1000), interval=1000, blit=True)

plt.show()
