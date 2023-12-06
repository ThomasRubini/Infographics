import numpy as np

class Transformation:
    """
    matrix: the transformation matrix
    n: the number of frames for the animation
        Note: "None" can be used as a number of frames, to specify that we should never stop using that matrix (infinite frames)
    """

    def __init__(self, matrix: np.ndarray, n: int=None):
        self.matrix = matrix
        self.n = n