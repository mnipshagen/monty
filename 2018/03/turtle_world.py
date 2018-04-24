# pylint: disable=E1101
import time
import turtle


# constants for all draw functions for a nice and consistent look
LENGTH = 6
ANGLE = 35

def draw_tree(height):
    """
    Draws a fractal tree with `height` repetitions.
    
    `height` defines the overall height of the tree is also responsible for
    the length of each branch in every iteration
    """
    if height == 0:
        return
    # left branch
    turtle.forward(LENGTH * height)
    turtle.left(ANGLE)
    draw_tree(height - 1) # drawing the little tree at the end of the branch
    # right branch
    turtle.right(2 * ANGLE)
    draw_tree(height - 1)  # drawing the little tree at the end of the branch
    turtle.left(ANGLE)
    turtle.backward(LENGTH * height)


def draw_house():
    """This draws a nice and simple house!"""
    # the dimensions of our house
    height = 5 * LENGTH
    width = 7 * LENGTH
    roofside = (width ** 2 / 2) ** (1 / 2)

    # left wall
    turtle.forward(height)
    # roof
    turtle.right(45)
    turtle.forward(roofside)
    turtle.right(90)
    turtle.forward(roofside)
    turtle.right(45)
    # right wall
    turtle.forward(height)
    turtle.right(90)
    # bottom line
    turtle.forward(width)
    turtle.right(90)


def draw_world(curvature_step=0):
    """
    This draws a turtle world.
    
    The curvature step is relevant for drawing a round world.
    The higher the curvature step is, the smaller our circle will be.
    
    Each village will consist of one house and 3 trees, with one being taller.
    """
    if curvature_step > 0: # this ensures we are going full circle
        villages = 360 // 4 // curvature_step
    else: # 5 villages for our flat world
        villages = 5

    # the _ is called an anonymous variable, since we don't use it anyway
    # we don't need to give it a name. It just acts as a counter.
    for _ in range(villages):
        prepare_drawing()
        draw_house()
        finish_drawing()

        turtle.right(curvature_step)
        turtle.forward(LENGTH * 11)

        # and draw the three trees
        for j in range(3):
            prepare_drawing()
            # the middle one will be 5 high, since we iterate over 0,1,2
            # and only for 1 modulo 2 is 1 returned.
            draw_tree(3 + j % 2 * 2)
            finish_drawing()

            turtle.right(curvature_step)
            turtle.forward(LENGTH * 3)

        turtle.forward(LENGTH)


def init():
    """set up the turtle parameters"""
    turtle.reset()
    turtle.shape('turtle')
    turtle.speed('fastest')
    turtle.up()


def prepare_drawing():
    """move the pen down to actually draw and make turtle upright"""
    turtle.down()
    turtle.left(90)


def finish_drawing():
    """move pen up to stop drawing and return turtle to axis"""
    turtle.right(90)
    turtle.up()


def draw_flat_world():
    """wrapper to start drawing a flat world with 0 curvature"""
    init()
    turtle.goto(-300, 0)

    draw_world()
    turtle.goto(0,0)


def draw_round_world(curvature_step=5):
    """wrapper to draw a curved world with a default curvature step of 5"""
    init()
    turtle.goto(0, 300)
    draw_world(curvature_step)
    turtle.goto(0,0)


def draw():
    """Draw the flat world. Rest shortly to marvel at it. Draw round world."""
    draw_flat_world()
    time.sleep(3)
    draw_round_world()
    turtle.done()

# Start the party!
draw()
