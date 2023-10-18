import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import numpy as np

from matrix_movement_builder import MatrixMovementBuilder
from polygon import Polygon


def matplotlib_ez(polygon: Polygon):
    fig, ax1 = plt.subplots()

    ax1.set_aspect('equal', adjustable='box')
    # bounding box zoom
    ax1.set_xlim(-10, 10)
    ax1.set_ylim(-10, 10)

    def update(frame):
        polygon.update()
        return ax1.fill(polygon.x, polygon.y, color="blue")

    # nombre d'itération
    frames = np.linspace(0, 1, 10000)

    # attente entre chaque itération
    interval = 0.01
    anni = FuncAnimation(fig, update, frames=frames, interval=interval, blit=True)

    plt.show()


builder = MatrixMovementBuilder()
# builder.translate(0.01, 0.01)
builder.rotate(0.01, 3, -4)
m = builder.get_matrix()

polygon = Polygon(
    np.array([1, 1, -1, -1]),
    np.array([1, -1, -1, 1]),
    m
)

matplotlib_ez(polygon)
