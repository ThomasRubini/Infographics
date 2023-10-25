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

    def __init__(self, x: np.ndarray, y: np.ndarray,
                 matrixes: list[tuple[np.ndarray, int]],
                 color: str="blue", repeat: bool=False):
        self.n = len(x)
        assert len(y) == self.n
        self.x = x.astype(float)
        self.y = y.astype(float)
        self.matrixes = matrixes
        self.color = color
        self.repeat = repeat

        self.__pop_matrix()
    
    def __reuse_matrix(self):
        """
        Append the current matrix at the end of the animation queue to reuse it later
        """
        self.matrixes.append((self.current_matrix, self.init_counter))
    
    def __pop_matrix(self):
        """
        Pops a new current matrix from self.matrixes, if possible
        if no matrixes are present in the list, the current matrix becomes None
        """
        if len(self.matrixes) == 0:
            self.current_matrix = None
            return
        self.current_matrix, self.init_counter = self.matrixes.pop(0)
        self.counter = self.init_counter

    def update(self):
        if self.current_matrix is None:
            return
        
        for point_i in range(self.n):
            self.x[point_i], self.y[point_i], z = self.current_matrix @ np.array([self.x[point_i], self.y[point_i], 1])
            assert z == 1

        # Special case: a "None" counter means we don't ever change matrix again.
        # Typicailly this is used for the last matrix in the list
        if self.counter != None:
            self.counter -= 1
            # If the end of the matrix is reached
            if self.counter == 0:
                # Append the current matrix if looping
                if self.repeat:
                    self.__reuse_matrix()
                # Remove the current matrix
                self.__pop_matrix()
    
    def __repr__(self) -> str:
        return f"Polygon(size={self.n}, points=[{', '.join(map(str, zip(self.x, self.y)))}])"
