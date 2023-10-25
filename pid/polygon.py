import numpy as np

class Polygon:
    """
    n: number of points in the polygon
    x: x coordinates of each point of the polygon
    y: y coordinates of each point of the polygon
    current_matrix: currently used movement matrix (matrix that will make the polygon move)
    matrixes: list of tuples of movement matrixes with their number of frames
        Note: "None" can be used as a number of frames, to specify that we should never stop using that matrix (infinite frames)
    counter: decreasing counter of frames that are need to be spent with the current matrix
    """

    def __init__(self, x: np.ndarray, y: np.ndarray, matrixes: list[tuple[np.ndarray, int]]):
        self.n = len(x)
        assert len(y) == self.n
        self.x = x.astype(float)
        self.y = y.astype(float)
        self.matrixes = matrixes

        self.__pop_matrix()
    
    def __pop_matrix(self):
        """
        Pops a new current matrix from self.matrixes, if possible
        if no matrixes are present in the list, the function will raise an error
        """
        if len(self.matrixes) == 0:
            raise Exception(f"asking to change current matrix when matrix list is empty for polygon {self}")
        self.current_matrix = self.matrixes[0][0]
        self.counter = self.matrixes[0][1]
        self.matrixes = self.matrixes[1:]

    def update(self):
        for point_i in range(self.n):
            self.x[point_i], self.y[point_i], z = self.current_matrix @ np.array([self.x[point_i], self.y[point_i], 1])
            assert z == 1

        # Special case: a "None" counter means we don't ever change matrix ever.
        # Typicailly this is used for the last matrix in the list
        if self.counter != None:
            self.counter -= 1
            if self.counter == 0:
                self.__pop_matrix()
    
    def __repr__(self) -> str:
        return f"Polygon(size={self.n}, points=[{', '.join(map(str, zip(self.x, self.y)))}])"
    
if __name__ == "__main__":
    polygon = Polygon(
        np.array([-0.1, -0.1, 0.1,  0.1]),
        np.array([-0.1,  0.1, 0.1, -0.1]),
        np.array([[1, 0, 1], [0, 1, 1], [0, 0, 1]])
    )
    print(polygon)