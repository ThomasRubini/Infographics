import matplotlib.pyplot as plt
import matplotlib.animation as animation

from pid.polygon import Polygon

def mpl_display(scenes: list[list[Polygon, int]], interval = 5):
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
        if len(scenes) == 0: return []
        figures = []
        for polygon in scenes[0][0]:
            polygon.update()
            if isinstance(polygon, Polygon):
                figures.append(*ax1.fill(polygon.x, polygon.y, color=polygon.color))
            else:
                figures.append(polygon.ellipse)
                ax1.add_artist(polygon.ellipse)
        scenes[0][1] -= 1
        if scenes[0][1] == 0:
            scenes.pop(0)
        return figures
    
    # We need that variable to stay in scope while displaying,
    # otherwise FuncAnimation will be collected by the garbage collector
    anni = animation.FuncAnimation(fig, update_figs, frames=sum(map(lambda scene: scene[1], scenes)), interval=interval, blit=True, cache_frame_data=False)
    plt.axis('off')
    
    # Uncomment this 2 lines to save the animation as mp4 format
    # writer = animation.FFMpegWriter(fps=30)
    # anni.save('output.mp4', writer=writer)
    
    plt.show()