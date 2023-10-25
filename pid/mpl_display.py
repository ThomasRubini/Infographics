from typing import List

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from polygon import Polygon

import numpy as np

def mpl_display(polygons: List[Polygon]):
    fig, ax1 = plt.subplots()

    ax1.set_aspect('equal', adjustable='box')
    # bounding box zoom
    ax1.set_xlim(-10, 10)
    ax1.set_ylim(-10, 10)

    def update(frame):
        figures = []
        for polygon in polygons:
            polygon.update()
            figures.append(*ax1.fill(polygon.x, polygon.y, color="blue"))
        return figures

    # nombre d'itération
    frames = np.linspace(0, 1, 10000)

    # attente entre chaque itération
    interval = 0.01
    anni = FuncAnimation(fig, update, frames=frames, interval=interval, blit=True)

    plt.show()