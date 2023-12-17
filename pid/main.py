import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import numpy as np
from math import pi

from pid.matrix_movement_builder import MatrixMovementBuilder
from pid.polygon import Polygon
from pid.ellipse import Ellipse
from pid.transformation import Transformation
from pid.mpl_display import mpl_display

def create_road():
    idling = Transformation(MatrixMovementBuilder().get_ref(), 300)

    m = MatrixMovementBuilder()
    m.rotate_origin(-pi/200)
    rotation = Transformation(m.get_ref(), 200)

    return Polygon(
        np.array([-4,  4,   4,  -4]),
        np.array([15, 15, -15, -15]),
        idling,
        {idling: rotation},
        "#343434"
    )

def create_lines():
    idling1 = Transformation(MatrixMovementBuilder().get_ref(), 300)

    m = MatrixMovementBuilder()
    m.rotate_origin(-pi/200)
    rotation = Transformation(m.get_ref(), 200)

    idling2 = Transformation(MatrixMovementBuilder().get_ref(), 20)

    m = MatrixMovementBuilder()
    m.translate(0, -1)
    move_down = Transformation(m.get_ref(), 30)

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
    m.translate(0, -1)
    move_init_l2 = Transformation(m.get_ref(), 20)

    line2 = Polygon(
        np.array([-0.2, 0.2, 0.2, -0.2]),
        np.array([  -7,  -7,   0,    0]),
        idling1,
        {idling1: rotation, rotation: idling2, idling2: move_init_l2, move_init_l2: reset, reset: move_down, move_down: reset},
        "#F5D551"
    )

    # LINE 3
    m = MatrixMovementBuilder()
    m.translate(0, -1)
    move_init_l3 = Transformation(m.get_ref(), 10)

    line3 = Polygon(
        np.array([-0.2, 0.2, 0.2, -0.2]),
        np.array([   3,   3,  10,   10]),
        idling1,
        {idling1: rotation, rotation: idling2, idling2: move_init_l3, move_init_l3: reset, reset: move_down, move_down: reset},
        "#F5D551"
    )

    return [line0, line1, line2, line3]

def create_truck():
    idling1 = Transformation(MatrixMovementBuilder().get_ref(), 200)

    m = MatrixMovementBuilder()
    m.translate(0, -1)
    appear1 = Transformation(m.get_ref(), 27)

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
            "#058"
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
    
    idling = Transformation(MatrixMovementBuilder().get_ref(), 550)
    
    m = MatrixMovementBuilder()
    m.translate(0, -1)
    move_down1 = Transformation(m.get_ref(), 30)
    move_down2 = Transformation(m.get_ref(), 30)

    m = MatrixMovementBuilder()
    m.translate(-15, 30)
    reset1 = Transformation(m.get_ref(), 1)

    m = MatrixMovementBuilder()
    m.translate(15, 30)
    reset2 = Transformation(m.get_ref(), 1)

    return Polygon(
        np.array([-8, -7,   -7, -6, -6, -6.3, -6.6, -6.6,   -7, -7, -7.5, -8,   -8, -8.4, -8.4, -8.7, -9,   -9,   -8]),
        np.array([10, 10, 11.5, 12, 14, 14.3,   14, 12.6, 12.4, 16, 16.5, 16, 13.8,   14,   15, 15.3, 15, 13.4, 12.9]),
        idling,
        {idling: move_down1, move_down1: reset2, reset2: move_down2, move_down2: reset1, reset1: move_down1},
        "#382"
    )

def create_astral_bodies():
    idle1 = Transformation(MatrixMovementBuilder().get_ref(), 599)
    idle2 = Transformation(MatrixMovementBuilder().get_ref(), 599)

    m = MatrixMovementBuilder()
    m.translate(0, -10)
    move_down = Transformation(m.get_ref(), 1)

    m = MatrixMovementBuilder()
    m.translate(0, 10)
    move_up = Transformation(m.get_ref(), 1)

    m = MatrixMovementBuilder()
    m.rotate(pi/600, 0, 1)

    m2 = MatrixMovementBuilder()
    m2.rotate(pi/600, 0.5, 1)

    return [
        Polygon(
            np.array([-10, 10, 10, -10]),
            np.array([ 10, 10,  1,   1]),
            None, {}, "#2AE"
        ),
        Polygon(
            np.array([-10, 10, 10, -10]),
            np.array([ 20, 20, 11,  11]),
            idle1, {idle1: move_down, move_down: idle2, idle2: move_up, move_up: idle1},
            "#041A40"
        ),
        Ellipse(
            6, 1, 3, 3,
            Transformation(m.get_ref()), {},
            "#FF5"
        ),
        Ellipse(
            -6, 1, 3, 3,
            Transformation(m.get_ref()), {},
            "#FFA"
        ),
        Ellipse(
            -5.5, 1, 2.2, 2.2,
            Transformation(m2.get_ref()), {},
            "#041A40"
        )
    ]

def create_cactus2():
    m = MatrixMovementBuilder()
    m.homothety(0.95, 5, 0.625)
    movement1 = Transformation(m.get_ref(), 70)
    movement2 = Transformation(m.get_ref(), 53)
    
    m = MatrixMovementBuilder()
    m.translate(-24, 5)
    m.homothety(16, 5, 0.625)
    reset1 = Transformation(m.get_ref(), 1)
        
    m = MatrixMovementBuilder()
    m.translate(54.3717, -11.3329)
    m.homothety(34.35, 5, 0.625)
    reset2 = Transformation(m.get_ref(), 1)
    
    return Polygon(
        np.array([ 15,  19,  19,  23,  23,  21.8, 20.6,  20.6,    19, 19, 17, 15,    15, 13.4, 13.4,  12.2,  11,    11,    15]),
        np.array([-32, -32, -26, -24, -16, -14.8,  -16, -21.6, -22.4, -8, -6, -8, -16.5,  -16,  -12, -10.8, -12, -18.4, -20.4]),
        movement1,
        {movement1: reset1, reset1: movement2, movement2: reset2, reset2: movement1},
        "#382"
    )

def create_lines2():

    m = MatrixMovementBuilder()
    m.homothety(0.95, 5, 0.625)
    move = Transformation(m.get_ref(), 66)
    init_l2 = Transformation(m.get_ref(), 48)
    init_l3 = Transformation(m.get_ref(), 30)
    init_l4 = Transformation(m.get_ref(), 12)

    m = MatrixMovementBuilder()
    m.homothety(29.6, 5, 0.625)
    reset = Transformation(m.get_ref(), 1)
    
    # LINE 1
    line1 = Polygon(
        np.array([ -4,  -3,  -9, -10.77]),
        np.array([-10, -10, -18,    -18]),
        move,
        {move: reset, reset: move},
        "#F5D551"
    )
    
    # LINE 2
    line2 = Polygon(
        np.array([   1.22,    1.64, -0.88789,  -1.6239]),
        np.array([-3.8375, -3.8375, -7.19485, -7.19485]),
        init_l2,
        {init_l2: reset, move: reset, reset: move},
        "#F5D551"
    )
    
    # LINE 3
    line3 = Polygon(
        np.array([  3.4124,   3.5888,   2.5271,    2.218]),
        np.array([-1.24925, -1.24925, -2.65934, -2.65934]),
        init_l3,
        {init_l3: reset, move: reset, reset: move},
        "#F5D551"
    )
    
    # LINE 4
    line4 = Polygon(
        np.array([ 4.333208,  4.407296,    3.9614,   3.83155]),
        np.array([-0.162185, -0.162185, -0.754422, -0.754422]),
        init_l4,
        {init_l4: reset, move: reset, reset: move},
        "#F5D551"
    )

    return [line1, line2, line3, line4]

def create_truck2():
    
    m = MatrixMovementBuilder()
    m.translate(0.02, 0)
    right_slide = Transformation(m.get_ref(), 40)
    
    m = MatrixMovementBuilder()
    m.translate(-0.02, 0)
    left_slide = Transformation(m.get_ref(), 40)
    
    return [
        Ellipse(
            0.7, -3.3, 0.6, 1.4,
            right_slide, {left_slide: right_slide, right_slide: left_slide},
            "#111"
        ),
        Ellipse(
            2.2, -1.8, 0.4, 0.9,
            right_slide, {left_slide: right_slide, right_slide: left_slide},
            "#111"
        ),
        Ellipse(
            -4.8, -5.5, 0.8, 1.7,
            right_slide, {left_slide: right_slide, right_slide: left_slide},
            "#111"
        ),
        Polygon(
            np.array([0, 2.5,  2.5,  0]),
            np.array([1, 0.6, -1.5, -4]),
            right_slide, {left_slide: right_slide, right_slide: left_slide},
            "#AAA"
        ),
        Polygon(
            np.array([-4, 0, 0, -4]),
            np.array([ 1, 1, -4, -4]),
            right_slide, {left_slide: right_slide, right_slide: left_slide},
            "#777"
        ),
        Polygon(
            np.array([-4.5, -3.8, -0.2, -0.2, -1.3, -4.5]),
            np.array([-0.3,  0.8,  0.8,   -4,   -5,   -5]),
            right_slide, {left_slide: right_slide, right_slide: left_slide},
            "#700"
        ),
        Polygon(
            np.array([-4.2, -1.5, -1.5, -4.2]),
            np.array([-0.5, -0.5, -1.7, -1.7]),
            right_slide, {left_slide: right_slide, right_slide: left_slide},
            "#058"
        ),
        Polygon(
            np.array([-0.5, -1, -1, -0.5]),
            np.array([-0.4, -0.5, -1.6, -1.4]),
            right_slide, {left_slide: right_slide, right_slide: left_slide},
            "#058"
        ),
        Polygon(
            np.array([-5.4, -4.5, -1.3, -1.3, -2.4, -5.4]),
            np.array([  -3,   -2,   -2,   -5,   -6,   -6]),
            right_slide, {left_slide: right_slide, right_slide: left_slide},
            "#B00"
        ),
        Polygon(
            np.array([-5, -3, -3, -5]),
            np.array([-5.5, -5.5, -3.5, -3.5]),
            right_slide, {left_slide: right_slide, right_slide: left_slide},
            "#777"
        ),
        Polygon(
            np.array([-4.8, -3.2]),
            np.array([  -5,   -5]),
            right_slide, {left_slide: right_slide, right_slide: left_slide},
            "#333"
        ),
        Polygon(
            np.array([-4.8, -3.2]),
            np.array([-4.5, -4.5]),
            right_slide, {left_slide: right_slide, right_slide: left_slide},
            "#333"
        ),
        Polygon(
            np.array([-4.8, -3.2]),
            np.array([  -4,   -4]),
            right_slide, {left_slide: right_slide, right_slide: left_slide},
            "#333"
        ),
        Ellipse(
            -1.8, -5.5, 0.8, 1.7,
            right_slide, {left_slide: right_slide, right_slide: left_slide},
            "#111"
        ),
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

# ASTRAL BODIES (SKY, SUN AND MOON)
scene2 += create_astral_bodies()

# GROUND
scene2.append(Polygon(
    np.array([-10, 10,  10, -10]),
    np.array([  0,  0, -10, -10]),
    None, {}, "#FFAE42"
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

# CACTUS
scene2.append(create_cactus2())

# TRUCK
scene2 += create_truck2()

# DISPLAY
mpl_display([[scene1, 2000], [scene2, 1700]])
