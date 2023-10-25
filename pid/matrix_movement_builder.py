import math

import numpy as np

class MatrixMovementBuilder:

    def __init__(self):
        # identity matrix, there is no movement when using this matrix
        self.__matrix = np.array([
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0]
        ]).astype(float)

    def translate(self, x: float, y: float):
        """
        Moves **away** from the origin
        """
        self.__matrix @= np.array([
            [1.0, 0.0, x],
            [0.0, 1.0, y],
            [0.0, 0.0, 1.0]
        ]).astype(float)

    def rotate_origin(self, angle: float):
        """
        Add a rotation to the origin using the given angle.

        :param angle: the angle to use in radians

        """
        self.__matrix @= np.array([
            [math.cos(angle), -math.sin(angle), 0.0],
            [math.sin(angle),  math.cos(angle), 0.0],
            [            0.0,              0.0, 1.0]
        ]).astype(float)

    def rotate(self, angle: float, x: float, y: float):
        """
        Add a rotation to the given rotation point using the given angle.

        :param angle: the angle to use in radians
        :param x: the point's x coordinate
        :param y: the point's y coordinate

        """ 
        self.translate(x, y)
        self.rotate_origin(angle)
        self.translate(-x, -y)

    def get_ref(self) -> np.ndarray:
        """
        Return the matrix with the movements applied before.

        """
        return self.__matrix
