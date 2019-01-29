from turtle import *
import math

topdown = Turtle()
bgcolor('black')
topdown.shape('circle')
topdown.resizemode('auto')
gc = 266 + ((51+(6.2/60))/60)
star_tilt = 7.25
neptune_coors = (344 + (2 + (29.2/60))/60, -(58+(1.4/60))/60, 29.938)
pluto_coors = (336 + (2 + (29.2/60))/60, -(13 + (58+(1.4/60))/60), 41)
xrange = 720
yrange = 180
xscale = int(xrange/30)
yscale = int(yrange/30)


tdoffset = 0
topdown.penup()
topdown.setpos(tdoffset, tdoffset)
topdown.pendown()
origin = topdown.pos()
heading = 0


degree = u'\xb0'

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

    while True:
        x, y = x_center + math.cos(theta_radians) * x_radius, y_center + math.sin(theta_radians) * y_radius
        # readjust x & y to set the angle of the ellipse based on the original heading of the turtle
        x, y = x - x_center, y - y_start
        x, y = x * cos_heading - y * sin_heading, x * sin_heading + y * cos_heading
        x, y = x + x_center, y + y_start

        turtle.setheading(turtle.towards(x, y))  # turtle faces direction in which ellipse is drawn
        turtle.goto(x, y)

        if theta_radians == extent_radians:
            break

        theta_radians = min(theta_radians + step_radians, extent_radians)  # don't overshoot our starting point

    turtle.setheading(turtle.towards(x_center, y_start))  # set correct heading for the next thing we draw

    if not down:  # restore pen state on return
        turtle.penup()


def drawObjectRect(r, c, x, y, z, name, scale=1, line=True):
    r.penup()
    r.setpos(origin)
    r.setheading(gc)
    r.pendown()
    r.color(c)
    r.forward(x*scale)
    r.left(90)
    r.forward(y*scale)
    # right(90+45)
    # forward(z*scale)
    r.write(name, False, align="center", font=("Arial", 12, "normal"))

def drawObjectUSC(t, c, longitude, r, name, scale=1, line=True):
    t.penup()
    t.setpos(origin)
    t.setheading(gc)
    t.pendown()
    t.color(c)
    if not line:
        t.penup()
    t.left(longitude)
    t.forward(r*scale)
    t.write(name, False, align="center", font=("Arial", 12, "normal"))
    if not line:
        t.pendown()

def drawObjectEclip(t, c, longitude, r, name, scale=1, line=True):
    t.penup()
    t.setpos(origin)
    t.setheading(0)
    t.pendown()
    t.color(c)
    if not line:
        t.penup()
    t.left(longitude)
    if not line:
        t.pendown()


def reset():
    topdown.penup()
    topdown.setpos(origin)
    topdown.setheading(heading)
    topdown.pendown()


def write_name(name, offset=20):
    temp_origin = topdown.pos()
    temp_heading = topdown.heading()
    topdown.penup()
    topdown.forward(offset)
    topdown.pendown()
    topdown.write(name, False, align="center", font=("Arial", 12, "normal"))
    topdown.penup()
    topdown.setpos(temp_origin)
    topdown.setheading(temp_heading)
    topdown.pendown()


def drawEclipticAxes():
    # Ecliptic
    # drawObjectEclip(topdown, 'green', 0, xrange, 'Vernal Equinox')
    reset()
    topdown.color('red')
    topdown.forward(xrange)
    write_name('0' + degree + ' long', 30)
    topdown.left(90)
    ellipse(topdown, yrange, xrange)
    reset()
    topdown.left(90)
    topdown.forward(yrange + 40)
    write_name('90' + degree + ' lat (Ecliptic Axis)', 20)
    reset()
    topdown.right(90)
    topdown.forward(yrange + 40)
    reset()
    



def drawHSAxes():
    #H-S
    drawObjectEclip(topdown, 'blue', gc, xrange, '0d GC')
    drawObjectEclip(topdown, 'blue', (gc - 180), xrange, '180d GC')
    drawObjectEclip(topdown, 'blue', (gc - 90), yrange, '90d GC')
    drawObjectEclip(topdown, 'blue', (gc + 90), yrange, '180d GC')



def test_planet(long):
    reset()
    r = 30
    longitude = long

    drawObjectEclip(topdown, 'purple', longitude, r, 'Test', 12, True)
    if longitude >= 180:
        longitude = longitude - 180
    if longitude >= 90:
        longitude = 180 - longitude
    long_radians = math.radians(longitude)
    # smart_scale = xscale*math.cos(long_radians) + yscale*math.sin(long_radians)
    ratio = longitude/90.0
    smart_scale = yscale*ratio + xscale*(1-ratio)
    print(longitude, smart_scale)
    topdown.forward(r * smart_scale)
    write_name('Test' + str(longitude), 90)
    topdown.pensize(1)
    topdown.stamp()


def draw_neptune():
    r = 30
    longitude = 346
    drawObjectEclip(topdown, 'aqua', longitude, r, 'Neptune', 12, True)
    if longitude >= 180:
        longitude = longitude - 180
    if longitude >= 90:
        longitude = 180 - longitude
    p = (longitude / 90) * 2
    smart_scale = p * yscale + (1 - p) * xscale
    print(longitude, p, smart_scale)
    topdown.forward(r * smart_scale)
    write_name('Neptune 344' + degree + '2\' 29.2\"', 90)
    topdown.pensize(5)
    topdown.stamp()


def draw_earth():
    r = 1
    longitude = 0
    drawObjectEclip(topdown, 'blue', longitude, r, 'Earth', 12, True)
    if longitude >= 180:
        longitude = longitude - 180
    if longitude >= 90:
        longitude = 180 - longitude
    p = longitude / 90
    smart_scale = p * yscale + (1 - p) * xscale
    if smart_scale < 100:
        smart_scale = 100
    topdown.forward(r * smart_scale)
    write_name('Earth 0' + degree + '0\' 0.0\"', 90)
    topdown.pensize(1)
    topdown.stamp()

def draw_sun():
    reset()
    topdown.penup()
    topdown.forward(-20)
    topdown.left(90)
    topdown.pendown()
    topdown.color('gold')
    write_name('Sun', 40)
    reset()
    topdown.pensize(10)
    topdown.stamp()

def draw_planets():
    draw_neptune()
    draw_earth()
    draw_sun()



def convert_to_new(old):
    long = old[0]
    lat = old[1]
    r = old[2]
    new_long = long-gc
    while new_long < 0:
        new_long += 360
    new_lat = lat-7.25
    new_r = r
    return (new_long, new_lat, new_r)

def convert_to_rect(polar):
    long = radians(polar[0])
    lat = radians(polar[1])
    r = polar[2]
    x = r*cos(lat)*cos(long)
    y = r*cos(lat)*sin(long)
    z = r*sin(lat)
    print(x, y, z)
    return x, y, z

drawEclipticAxes()






draw_planets()





# origin = origin_td
# drawObjectEclip(topdown, 'green', neptune_coors[0], neptune_coors[2], 'Neptune', default_scale, False)
# origin = origin_td
# drawObjectEclip(topdown, 'green', pluto_coors[0], pluto_coors[2], 'Pluto', default_scale, False)




# neptune_coors = convert_to_new(neptune_coors)
# print(neptune_coors)
# drawObjectUSC(topdown, 'blue', neptune_coors[0], neptune_coors[2], 'Neptune', default_scale, False)
# neptune_coors = convert_to_rect(neptune_coors)
# drawObjectRect(topdown, 'red', neptune_coors[0], neptune_coors[1], neptune_coors[2], 'Neptune', default_scale)


# # mars
# drawObjectEclip(topdown, 'green', 24, 1.465, 'Mars', 10, False)
#
# # jupiter
# drawObjectEclip(topdown, 'green', 253, 5.347, 'Jupiter', 10, False)
# drawObjectEclip(topdown, 'green', 282, 10, 'Saturn', 10, False)
# drawObjectEclip(topdown, 'green', 28, 20, 'Uranus', 10, False)

#
# # # Z Axis
# drawObject(topdown, 'green', 305, 300, 'Ecliptic Orthogonal')
# drawObject(topdown, 'green', (305-180), 300, '')
#
#
# # #New Coordinates
# # #galactic center is at gc degrees long, so offset that
# #
# # # X Axis gc degrees off Eliptic
# drawObject(topdown, 'blue', gc, 300, '0d GC')
# drawObject(topdown, 'blue', (gc-180), 300, '180d GC')
# drawObject(topdown, 'blue', (gc-90), 300, '90d GC')
# drawObject(topdown, 'blue', (gc+90), 300, '180d GC')
#
# #Sun's poles are 7 degrees off the eliptic
#
# # # Z Axis
# drawObject(topdown, 'blue', 305+7, 300, 'Stellar Pole')
# drawObject(topdown, 'blue', (305+7)-180, 300, '180 d Stellar Pole')
#
#
# # long gc d 51 min 6.2 sec
# # lat 17 d 47 min 40.8 sec
#
# # mars
# drawObject(topdown, 'red', 24, 1.465, 'Mars', 10, False)
#
# # jupiter
# drawObject(topdown, 'orange', 253, 5.347, 'Jupiter', 10, False)
# drawObject(topdown, 'yellow', 282, 10, 'Saturn', 10, False)
# drawObject(topdown, 'blue', 28, 20, 'Uranus', 10, False)
# drawObject(topdown, 'blue', 344, 30, 'Neptune', 10, False)
#
#

#

#
#
# # 266d 51m 06.2s GC
# # 344d 2m 29.2s, -0d 58m 1.4s, 29.938 Nep
# # 7.25d Sun's Tilt
#
#
#
#

done()




