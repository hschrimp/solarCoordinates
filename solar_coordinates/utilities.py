import math


def draw_dashes(turtle, length):
    is_blank = False
    num_dashes = round(length / 10)
    for i in range(num_dashes):
        if is_blank:
            turtle.penup()
            is_blank = False
        else:
            turtle.pendown()
            is_blank = True
        turtle.forward(10)
    turtle.pendown()


def ellipse(turtle, x_radius, y_radius, steps=60):

    down = turtle.isdown()  # record pen state for restoration later

    if not down:
        turtle.pendown()

    heading_radians = math.radians(turtle.heading())
    theta_radians = -math.pi / 2
    extent_radians = 2 * math.pi
    step_radians = extent_radians / steps
    extent_radians += theta_radians
    x_center, y_start = turtle.position()
    y_center = y_start + y_radius

    cos_heading, sin_heading = math.cos(heading_radians), math.sin(heading_radians)

    is_blank = False
    counter = 0

    while True:
        x, y = x_center + math.cos(theta_radians) * x_radius, y_center + math.sin(theta_radians) * y_radius
        # readjust x & y to set the angle of the ellipse based on the original heading of the turtle
        x, y = x - x_center, y - y_start
        x, y = x * cos_heading - y * sin_heading, x * sin_heading + y * cos_heading
        x, y = x + x_center, y + y_start

        turtle.setheading(turtle.towards(x, y))  # turtle faces direction in which ellipse is drawn
        if is_blank:
            turtle.penup()
            counter += 1
            if counter > 0:
                is_blank = False
                counter = 0
        else:
            turtle.pendown()
            counter += 1
            if counter > 0:
                is_blank = True
                counter = 0
        turtle.goto(x, y)

        if theta_radians == extent_radians:
            break

        theta_radians = min(theta_radians + step_radians, extent_radians)  # don't overshoot our starting point

    turtle.setheading(turtle.towards(x_center, y_start))  # set correct heading for the next thing we draw

    if not down:  # restore pen state on return
        turtle.penup()