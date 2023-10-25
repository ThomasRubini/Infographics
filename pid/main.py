import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import numpy as np

from pid.matrix_movement_builder import MatrixMovementBuilder
from pid.polygon import Polygon
from pid.mpl_display import mpl_display

builder = MatrixMovementBuilder()
# builder.translate(0.01, 0.01)
builder.rotate(0.01, 3, -4)
m = builder.get_matrix()

polygon = Polygon(
    np.array([1, 1, -1, -1]),
    np.array([1, -1, -1, 1]),
    m
)

mpl_display([polygon])
