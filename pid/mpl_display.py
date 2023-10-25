from typing import List

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from pid.polygon import Polygon

def mpl_display(polygons: List[Polygon], interval = 5):
    """
    This function uses matplotlib to display the given list of polygon.

    **Warning**: This function will enter in an infinite loop to display the items, and will never return

    :param polygons: list of polygons that will be drawns
    :param interval: delay between each frame
    """

    fig, ax1 = plt.subplots()

    ax1.set_aspect('equal', adjustable='box')
    # bounding box zoom
    ax1.set_xlim(-10, 10)
    ax1.set_ylim(-10, 10)

    def update_figs(_):
        figures = []
        for polygon in polygons:
            polygon.update()
            figures.append(*ax1.fill(polygon.x, polygon.y, color="blue"))
        return figures
    
    # We need that variable to stay in scope while displaying,
    # otherwise FuncAnimation will be collected by the garbage collector
    anni = FuncAnimation(fig, update_figs, frames=None, interval=interval, blit=True, cache_frame_data=False)

    plt.show()