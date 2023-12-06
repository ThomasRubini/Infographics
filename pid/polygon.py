import numpy as np

from pid.transformation import Transformation

class Polygon:
    """
    n: number of points in the polygon
    x: x coordinates of each point of the polygon
    y: y coordinates of each point of the polygon
    initial_transformation: currently used movement matrix (matrix that will make the polygon move)
    graph: list of Transformations
    counter: decreasing counter of frames that are need to be spent with the current Transformation
    """

    def __init__(self, x: np.ndarray, y: np.ndarray,
                 initial_transformation: Transformation,
                 matrixes_graph: dict[Transformation, Transformation],
                 color: str="blue"):
        self.n = len(x)
        assert len(y) == self.n
        self.x = x.astype(float)
        self.y = y.astype(float)
        self.current_transformation = initial_transformation
        self.graph = matrixes_graph
        self.color = color
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
        
        for point_i in range(self.n):
            self.x[point_i], self.y[point_i], z = self.current_transformation.matrix @ np.array([self.x[point_i], self.y[point_i], 1])
            assert z == 1

        # Special case: a "None" counter means we don't ever change matrix again.
        # Typicailly this is used for the last matrix in the list
        if self.counter != None:
            self.counter -= 1
            # If the end of the matrix is reached
            if self.counter == 0:
                self.next_transformation()
    
    def __repr__(self) -> str:
        return f"Polygon(size={self.n}, points=[{', '.join(map(str, zip(self.x, self.y)))}])"
