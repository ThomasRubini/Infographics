import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import numpy as np

x = np.array([0, 0, 0.2, 0.2])
y = np.array([0, 0.2, 0.2, 0])

fig, ax1 = plt.subplots()

ax1.set_xlim(0, 2)
ax1.set_ylim(0, 2)

def update(frame):
    return ax1.fill(x + frame, y + frame, color="blue")

ani = FuncAnimation(fig, update, frames=np.linspace(0, 2, 1000), interval=10, blit=True)

plt.show()
