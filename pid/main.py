import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import numpy as np
from math import pi

from pid.matrix_movement_builder import MatrixMovementBuilder
from pid.polygon import Polygon
from pid.transformation import Transformation
from pid.mpl_display import mpl_display

def create_road():
    idling = Transformation(MatrixMovementBuilder().get_ref(), 500)

    m = MatrixMovementBuilder()
    m.rotate_origin(-pi/300)
    rotation = Transformation(m.get_ref(), 300)

    return Polygon(
        np.array([-4,  4,   4,  -4]),
        np.array([15, 15, -15, -15]),
        idling,
        {idling: rotation},
        "#343434"
    )

def create_lines():
    idling1 = Transformation(MatrixMovementBuilder().get_ref(), 500)

    m = MatrixMovementBuilder()
    m.rotate_origin(-pi/300)
    rotation = Transformation(m.get_ref(), 300)

    idling2 = Transformation(MatrixMovementBuilder().get_ref(), 20)

    m = MatrixMovementBuilder()
    m.translate(0, -0.4)
    move_down = Transformation(m.get_ref(), 75)

    m = MatrixMovementBuilder()
    m.translate(0, 30)
    reset = Transformation(m.get_ref(), 1)

    # LINE 0 (just to render 1 more line while the road rotates)
    line0 = Polygon(
        np.array([-0.2, 0.2, 0.2, -0.2]),
        np.array([  13,  13,  20,   20]),
        idling1,
        {idling1: rotation},
        "#F5D551"
    )

    # LINE 1
    line1 = Polygon(
        np.array([-0.2, 0.2, 0.2, -0.2]),
        np.array([ -17, -17, -10,  -10]),
        idling1,
        {idling1: rotation, rotation: idling2, idling2: move_down, move_down: reset, reset: move_down},
        "#F5D551"
    )

    # LINE 2
    m = MatrixMovementBuilder()
    m.translate(0, -0.4)
    move_init_l2 = Transformation(m.get_ref(), 50)

    line2 = Polygon(
        np.array([-0.2, 0.2, 0.2, -0.2]),
        np.array([  -7,  -7,   0,    0]),
        idling1,
        {idling1: rotation, rotation: idling2, idling2: move_init_l2, move_init_l2: reset, reset: move_down, move_down: reset},
        "#F5D551"
    )

    # LINE 3
    m = MatrixMovementBuilder()
    m.translate(0, -0.4)
    move_init_l3 = Transformation(m.get_ref(), 25)

    line3 = Polygon(
        np.array([-0.2, 0.2, 0.2, -0.2]),
        np.array([   3,   3,  10,   10]),
        idling1,
        {idling1: rotation, rotation: idling2, idling2: move_init_l3, move_init_l3: reset, reset: move_down, move_down: reset},
        "#F5D551"
    )

    return [line0, line1, line2, line3]

def create_truck():
    idling1 = Transformation(MatrixMovementBuilder().get_ref(), 400)

    m = MatrixMovementBuilder()
    m.translate(0, -0.5)
    appear1 = Transformation(m.get_ref(), 54)

    m = MatrixMovementBuilder()
    m.rotate_origin(pi)
    positioning = Transformation(m.get_ref(), 1)

    idling2 = Transformation(MatrixMovementBuilder().get_ref(), 700)

    m = MatrixMovementBuilder()
    m.translate(0, -0.02)
    appear2 = Transformation(m.get_ref(), 675)

    m = MatrixMovementBuilder()
    m.translate(0.01, 0)
    first_derivation = Transformation(m.get_ref(), 50)

    m = MatrixMovementBuilder()
    m.translate(-0.01, 0)
    left_derivation = Transformation(m.get_ref(), 100)

    m = MatrixMovementBuilder()
    m.translate(0.01, 0)
    right_derivation = Transformation(m.get_ref(), 100)

    return [
        Polygon(
            np.array([-1, -3.3, -3.3, -1]),
            np.array([17,   17,   12, 12]),
            idling1,
            {idling1: appear1, appear1: positioning, positioning: idling2, idling2: appear2, appear2: first_derivation,
            first_derivation: left_derivation, left_derivation: right_derivation, right_derivation: left_derivation},
            "#AAA"
        ),
        Polygon(
            np.array([-3.3, -1, -1.3,   -3]),
            np.array([  12, 12, 11.7, 11.7]),
            idling1,
            {idling1: appear1, appear1: positioning, positioning: idling2, idling2: appear2, appear2: first_derivation,
            first_derivation: left_derivation, left_derivation: right_derivation, right_derivation: left_derivation},
            "#777"
        ),
        Polygon(
            np.array([-3.2, -2.8, -3.1]),
            np.array([11.5, 11.3, 11.3]),
            idling1,
            {idling1: appear1, appear1: positioning, positioning: idling2, idling2: appear2, appear2: first_derivation,
            first_derivation: left_derivation, left_derivation: right_derivation, right_derivation: left_derivation},
            "#700"
        ),
        Polygon(
            np.array([-1.1, -1.5, -1.2]),
            np.array([11.5, 11.3, 11.3]),
            idling1,
            {idling1: appear1, appear1: positioning, positioning: idling2, idling2: appear2, appear2: first_derivation,
            first_derivation: left_derivation, left_derivation: right_derivation, right_derivation: left_derivation},
            "#700"
        ),
        Polygon(
            np.array([-2.9, -1.4, -1.5, -2.8]),
            np.array([11.9, 11.9,   10,   10]),
            idling1,
            {idling1: appear1, appear1: positioning, positioning: idling2, idling2: appear2, appear2: first_derivation,
            first_derivation: left_derivation, left_derivation: right_derivation, right_derivation: left_derivation},
            "#B00"
        ),
        Polygon(
            np.array([-2.8, -1.5, -1.7, -2.6]),
            np.array([11.3, 11.3, 11.2, 11.2]),
            idling1,
            {idling1: appear1, appear1: positioning, positioning: idling2, idling2: appear2, appear2: first_derivation,
            first_derivation: left_derivation, left_derivation: right_derivation, right_derivation: left_derivation},
            "#0AF"
        ),
        Polygon(
            np.array([-1.2, -3.1]),
            np.array([  16,   16]),
            idling1,
            {idling1: appear1, appear1: positioning, positioning: idling2, idling2: appear2, appear2: first_derivation,
            first_derivation: left_derivation, left_derivation: right_derivation, right_derivation: left_derivation},
            "#555"
        ),
        Polygon(
            np.array([-1.2, -3.1]),
            np.array([  15,   15]),
            idling1,
            {idling1: appear1, appear1: positioning, positioning: idling2, idling2: appear2, appear2: first_derivation,
            first_derivation: left_derivation, left_derivation: right_derivation, right_derivation: left_derivation},
            "#555"
        ),
        Polygon(
            np.array([-1.2, -3.1]),
            np.array([  14,   14]),
            idling1,
            {idling1: appear1, appear1: positioning, positioning: idling2, idling2: appear2, appear2: first_derivation,
            first_derivation: left_derivation, left_derivation: right_derivation, right_derivation: left_derivation},
            "#555"
        ),
        Polygon(
            np.array([-1.2, -3.1]),
            np.array([  13,   13]),
            idling1,
            {idling1: appear1, appear1: positioning, positioning: idling2, idling2: appear2, appear2: first_derivation,
            first_derivation: left_derivation, left_derivation: right_derivation, right_derivation: left_derivation},
            "#555"
        )
    ]

def create_cactus():
    idling1 = Transformation(MatrixMovementBuilder().get_ref(), 500)
    
    m = MatrixMovementBuilder()
    m.translate(15, 0)
    rotation = Transformation(m.get_ref(), 1)
    
    idling2 = Transformation(MatrixMovementBuilder().get_ref(), 320)
    
    m = MatrixMovementBuilder()
    m.translate(0, -0.4)
    move_down_init = Transformation(m.get_ref(), 40)
    move_down1 = Transformation(m.get_ref(), 75)
    move_down2 = Transformation(m.get_ref(), 75)

    m = MatrixMovementBuilder()
    m.translate(-15, 30)
    reset1 = Transformation(m.get_ref(), 1)

    m = MatrixMovementBuilder()
    m.translate(15, 30)
    reset2 = Transformation(m.get_ref(), 1)

    return Polygon(
        np.array([-8, -7,   -7, -6, -6, -6.3, -6.6, -6.6,  -7, -7, -7.5, -8,  -8, -8.4, -8.4, -8.7, -9,  -9,  -8]),
        np.array([-2, -2, -0.5,  0,  2,  2.3,    2,  0.6, 0.4,  4,  4.5,  4, 1.8,    2,    3,  3.3,  3, 1.4, 0.9]),
        idling1,
        {idling1: rotation, rotation: idling2, idling2: move_down_init, move_down_init: reset1, reset1: move_down1, move_down1: reset2, reset2: move_down2, move_down2: reset1},
        "#382"
    )

def create_lines2():

    m = MatrixMovementBuilder()
    m.homothety(0.95, 5, 0.625)
    move = Transformation(m.get_ref(), 100)

    m = MatrixMovementBuilder()
    m.homothety(169, 5, 0.625)
    reset = Transformation(m.get_ref(), 1)

    # LINE 1
    line1 = Polygon(
        np.array([-3.3, -2.7,  -4.7, -6.6]),
        np.array([ -10,  -10, -15,  -15]),
        move,
        {move: reset, reset: move},
        "#F5D551"
    )

    return [line1]

def create_truck2():
    
    return [
        Polygon(
            np.array([0, 2.5,  2.5,  0]),
            np.array([1, 0.6, -1.5, -4]),
            None, {},
            "#AAA"
        ),
        Polygon(
            np.array([-4, 0, 0, -4]),
            np.array([ 1, 1, -4, -4]),
            None, {},
            "#777"
        ),
        Polygon(
            np.array([-4.5, -3.8, -0.2, -0.2, -1.3, -4.5]),
            np.array([-0.3,  0.8,  0.8,   -4,   -5,   -5]),
            None, {},
            "#700"
        ),
        # Polygon(
        #     np.array([-1.1, -1.5, -1.2]),
        #     np.array([11.5, 11.3, 11.3]),
        #     idling1,
        #     {idling1: appear1, appear1: positioning, positioning: idling2, idling2: appear2, appear2: first_derivation,
        #     first_derivation: left_derivation, left_derivation: right_derivation, right_derivation: left_derivation},
        #     "#700"
        # ),
        # Polygon(
        #     np.array([-2.9, -1.4, -1.5, -2.8]),
        #     np.array([11.9, 11.9,   10,   10]),
        #     idling1,
        #     {idling1: appear1, appear1: positioning, positioning: idling2, idling2: appear2, appear2: first_derivation,
        #     first_derivation: left_derivation, left_derivation: right_derivation, right_derivation: left_derivation},
        #     "#B00"
        # ),
        # Polygon(
        #     np.array([-2.8, -1.5, -1.7, -2.6]),
        #     np.array([11.3, 11.3, 11.2, 11.2]),
        #     idling1,
        #     {idling1: appear1, appear1: positioning, positioning: idling2, idling2: appear2, appear2: first_derivation,
        #     first_derivation: left_derivation, left_derivation: right_derivation, right_derivation: left_derivation},
        #     "#0AF"
        # ),
        # Polygon(
        #     np.array([-1.2, -3.1]),
        #     np.array([  16,   16]),
        #     idling1,
        #     {idling1: appear1, appear1: positioning, positioning: idling2, idling2: appear2, appear2: first_derivation,
        #     first_derivation: left_derivation, left_derivation: right_derivation, right_derivation: left_derivation},
        #     "#555"
        # ),
        # Polygon(
        #     np.array([-1.2, -3.1]),
        #     np.array([  15,   15]),
        #     idling1,
        #     {idling1: appear1, appear1: positioning, positioning: idling2, idling2: appear2, appear2: first_derivation,
        #     first_derivation: left_derivation, left_derivation: right_derivation, right_derivation: left_derivation},
        #     "#555"
        # ),
        # Polygon(
        #     np.array([-1.2, -3.1]),
        #     np.array([  14,   14]),
        #     idling1,
        #     {idling1: appear1, appear1: positioning, positioning: idling2, idling2: appear2, appear2: first_derivation,
        #     first_derivation: left_derivation, left_derivation: right_derivation, right_derivation: left_derivation},
        #     "#555"
        # ),
        # Polygon(
        #     np.array([-1.2, -3.1]),
        #     np.array([  13,   13]),
        #     idling1,
        #     {idling1: appear1, appear1: positioning, positioning: idling2, idling2: appear2, appear2: first_derivation,
        #     first_derivation: left_derivation, left_derivation: right_derivation, right_derivation: left_derivation},
        #     "#555"
        # )
    ]


# SCENE 1
scene1 = []

# BACKGROUND
scene1.append(Polygon(
    np.array([-10, 10,  10, -10]),
    np.array([ 10, 10, -10, -10]),
    None, {}, "#FFAE42"
))

# ROAD
scene1.append(create_road())

# LINES
scene1 += create_lines()

# TRUCK
scene1 += create_truck()

# CACTUS
scene1.append(create_cactus())

# SCENE 2
scene2 = []

# GROUND
scene2.append(Polygon(
    np.array([-10, 10,  10, -10]),
    np.array([  0,  0, -10, -10]),
    None, {}, "#FFAE42"
))

# SKY
scene2.append(Polygon(
    np.array([-10, 10, 10, -10]),
    np.array([ 10, 10,  0,   0]),
    None, {}, "#2AE"
))

# ROAD
scene2.append(Polygon(
    np.array([4, 5,   5,  -12]),
    np.array([0, 0, -10, -10]),
    None, {}, "#343434"
))

# LINES
scene2 += create_lines2()

# MOUNTAINS
scene2.append(Polygon(
    np.array([-10, -10, -9, -4, 2, 6, 13]),
    np.array([  0,  2,  1,  3, 2, 4,  0]),
    None, {}, "#EE7D21"
))

# TRUCK
scene2 += create_truck2()

# DISPLAY
# mpl_display([[scene1, 2500], [scene2, 200]])
mpl_display([[scene2, -1]])
