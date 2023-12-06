import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import numpy as np

from pid.matrix_movement_builder import MatrixMovementBuilder
from pid.polygon import Polygon
from pid.transformation import Transformation
from pid.mpl_display import mpl_display

# BACKGROUND

background = Polygon(
    np.array([-10, 10,  10, -10]),
    np.array([ 10, 10, -10, -10]),
    None, {}, "#FFAE42"
)

# ROAD

road = Polygon(
    np.array([-4,  4,   4,  -4]),
    np.array([10, 10, -10, -10]),
    None, [], "#343434"
)

# LINE 1

m = MatrixMovementBuilder()
m.translate(0, -0.1)
move_down = Transformation(m.get_ref(), 280)

m = MatrixMovementBuilder()
m.translate(0, 28)
reset = Transformation(m.get_ref(), 1)

line1 = Polygon(
    np.array([-0.2, 0.2, 0.2, -0.2]),
    np.array([  14,  14,  10,   10]),
    move_down,
    {move_down: reset, reset: move_down},
    "#F5D571"
)

# LINE 2

m = MatrixMovementBuilder()
m.translate(0, -0.1)
move_down = Transformation(m.get_ref(), 280)

m = MatrixMovementBuilder()
m.translate(0, 28)
reset = Transformation(m.get_ref(), 1)

line1 = Polygon(
    np.array([-0.2, 0.2, 0.2, -0.2]),
    np.array([  14,  14,  10,   10]),
    move_down,
    {move_down: reset, reset: move_down},
    "#F5D571"
)

# DISPLAY

mpl_display([background, road, line1])
