import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import numpy as np

from pid.matrix_movement_builder import MatrixMovementBuilder
from pid.polygon import Polygon
from pid.mpl_display import mpl_display

builder = MatrixMovementBuilder()
builder.translate(0.01, 0.01)
transition_matrix = builder.get_ref()

builder = MatrixMovementBuilder()
builder.rotate(0.01, 3, -4)
rotation_matrix = builder.get_ref()

polygon = Polygon(
    np.array([1, 1, -1, -1]),
    np.array([1, -1, -1, 1]),
    [(transition_matrix, 100), (rotation_matrix, None)]
)

mpl_display([polygon])
