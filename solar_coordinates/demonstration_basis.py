from turtle import *
from math import *

origin = pos()

def drawObject(c, longitude, r, name, scale=1, line=True):
    penup()
    setpos(origin)
    setheading(180)
    pendown()
    color(c)
    if not line:
        penup()
    right(longitude)
    forward(r*scale)
    write(name, False, align="center", font=("Arial", 12, "normal"))
    if not line:
        pendown()

# Eliptic Coordinates

hideturtle()
write("Barycenter ", False, align="center", font=("Arial", 12, "normal"))
left(180)

drawObject('green', 0, 300, 'Vernal Equinox')
drawObject('green', 180, 300, '180d')

# Y Axis
drawObject('green', 90, 300, '90d')
drawObject('green', 270, 300, '270d')

# # Z Axis
drawObject('green', 305, 300, 'Ecliptic Orthogonal')
drawObject('green', (305-180), 300, '')


# #New Coordinates
# #galactic center is at 266 degrees long, so offset that
#
# # X Axis 266 degrees off Eliptic
drawObject('blue', 266, 300, '0d GC')
drawObject('blue', (266-180), 300, '180d GC')
drawObject('blue', (266-90), 300, '90d GC')
drawObject('blue', (266+90), 300, '180d GC')

#Sun's poles are 7 degrees off the eliptic

# # Z Axis
drawObject('blue', 305+7, 300, 'Stellar Pole')
drawObject('blue', (305+7)-180, 300, '180 d Stellar Pole')


# long 266 d 51 min 6.2 sec
# lat 17 d 47 min 40.8 sec

# mars
drawObject('red', 24, 1.465, 'Mars', 10, False)

# jupiter
drawObject('orange', 253, 5.347, 'Jupiter', 10, False)
drawObject('yellow', 282, 10, 'Saturn', 10, False)
drawObject('blue', 28, 20, 'Uranus', 10, False)
drawObject('blue', 344, 30, 'Neptune', 10, False)


def convert_to_new(old):
    long = old[0]
    lat = old[1]
    r = old[2]
    new_long = long+266
    while new_long > 360:
        new_long -= 360
    new_lat = lat+7
    new_r = r
    return (new_long, new_lat, new_r)

def convert_to_rect(polar):
    long = polar[0]
    lat = polar[1]
    r = polar[2]
    x = r*cos(lat)*cos(long)
    y = r*cos(lat)*sin(long)
    z = r*sin(lat)
    return (x, y, z)

def drawObjectRect(c, x, y, z, name, scale=1, line=True):
    setpos(origin)
    setheading(180)
    # x axis
    right(266)
    forward(x*scale)
    left(90)
    forward(y*scale)
    # right(90+45)
    # forward(z*scale)
    write(name, False, align="center", font=("Arial", 12, "normal"))




neptune_coors = (344, -1, 30)
neptune_coors = convert_to_new(neptune_coors)
neptune_coors = convert_to_rect(neptune_coors)
drawObjectRect('blue', neptune_coors[0], neptune_coors[1], neptune_coors[2], 'Neptune Rect', 10)
done()




