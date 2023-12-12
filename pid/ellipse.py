import numpy as np
from matplotlib import patches

from pid.transformation import Transformation

class Ellipse:
    """
    x: x coordinate for the center of the ellipse
    y: y coordinate for the center of the ellipse
    width: width of the ellipse
    height: height of the ellipse
    initial_transformation: currently used movement matrix (matrix that will make the polygon move)
    graph: list of Transformations
    counter: decreasing counter of frames that are need to be spent with the current Transformation
    """

    def __init__(self, x: float, y: float, width: float, height: float,
                 initial_transformation: Transformation,
                 matrixes_graph: dict[Transformation, Transformation],
                 color: str="blue"):
        self.ellipse = patches.Ellipse((x, y), width, height, color=color)
        self.x = x
        self.y = y
        self.current_transformation = initial_transformation
        self.graph = matrixes_graph
        if self.current_transformation != None:
            self.counter = self.current_transformation.n

    def next_transformation(self):
        if self.current_transformation in self.graph:
            self.current_transformation = self.graph[self.current_transformation]
            self.counter = self.current_transformation.n
        else:
            self.current_transformation = None

    def update(self):
        if self.current_transformation is None:
            return

        self.x, self.y, z = self.current_transformation.matrix @ np.array([self.x, self.y, 1])
        assert z == 1
        self.ellipse.set_center((self.x, self.y))

        # Special case: a "None" counter means we don't ever change matrix again.
        # Typicailly this is used for the last matrix in the list
        if self.counter != None:
            self.counter -= 1
            # If the end of the matrix is reached
            if self.counter == 0:
                self.next_transformation()
    
    def __repr__(self) -> str:
        return f"Ellipse(x={self.x}, y={self.y})"
