import numpy as np

class Polygon:
    """
    n: number of points in the polygon
    x: x coordinates of each point of the polygon
    y: y coordinates of each point of the polygon
    m: movement matrix (matrix that will make the polygon move)
    """

    def __init__(self, x: np.ndarray, y: np.ndarray, m: np.ndarray):
        self.n = len(x)
        assert(len(y) == self.n)
        self.x = x.astype(float)
        self.y = y.astype(float)
        self.m = m.astype(float)
    
    def update(self):
        for point_i in range(self.n):
            self.x[point_i], self.y[point_i], z = self.m @ np.array([self.x[point_i], self.y[point_i], 1])
            assert z == 1
    
    def __repr__(self) -> str:
        return f"Polygon(size={self.n}, points=[{', '.join(map(str, zip(self.x, self.y)))}])"
    
if __name__ == "__main__":
    polygon = Polygon(
        np.array([-0.1, -0.1, 0.1,  0.1]),
        np.array([-0.1,  0.1, 0.1, -0.1]),
        np.array([[1, 0, 1], [0, 1, 1], [0, 0, 1]])
    )
    print(polygon)