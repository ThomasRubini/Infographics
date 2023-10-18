import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import matplotlib.pyplot as plt

x = [0, 0, 0.1, 0.1]
y = [0, 0.1, 0.1, 0]

fig, ax1 = plt.subplots()

ax1.set_aspect('equal', adjustable='box')
ax1.fill(x, y)

ax1.set_xlim(0, 2)
ax1.set_ylim(0, 2)

plt.show()
