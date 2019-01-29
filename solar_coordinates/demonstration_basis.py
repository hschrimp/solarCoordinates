from turtle import *
from math import *

origin = pos()
topdown = Turtle()
sideview = Turtle()
gc = 266 + ((51+(6.2/60))/60)
star_tilt = 7.25
neptune_coors = (344 + (2 + (29.2/60))/60, -(58+(1.4/60))/60, 29.938)
pluto_coors = (336 + (2 + (29.2/60))/60, -(13 + (58+(1.4/60))/60), 41)
xrange = 200
yrange = 200
zrange = 200
tdoffset = 200
topdown.penup()
topdown.setpos(tdoffset, tdoffset)
topdown.pendown()
origin_td = topdown.pos()
default_scale = 5

sideview.penup()
sideview.setpos(-tdoffset, -tdoffset)
sideview.pendown()
origin_sv = sideview.pos()

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
    print(origin)
    t.setpos(origin)
    t.setheading(0)
    t.pendown()
    t.color(c)
    if not line:
        t.penup()
    t.left(longitude)
    t.forward(r*scale)
    t.write(name, False, align="center", font=("Arial", 12, "normal"))
    if not line:
        t.pendown()

def drawSVAxes():
    # Ecliptic
    drawObjectEclip(sideview, 'green', 0, xrange, '')
    drawObjectEclip(sideview, 'green', 180, xrange, '0 Lat')
    drawObjectEclip(sideview, 'green', 90, zrange, 'NP')
    drawObjectEclip(sideview, 'green', 270, zrange, 'SP')

    #USC
    drawObjectEclip(sideview, 'blue', star_tilt, xrange, '0 Lat')
    drawObjectEclip(sideview, 'blue', (star_tilt+180), xrange, '0 Lat')
    drawObjectEclip(sideview, 'blue', (star_tilt + 90), yrange, 'NP')
    drawObjectEclip(sideview, 'blue', (star_tilt + 270), yrange, 'SP')

def drawTopAxes():
    # Ecliptic
    drawObjectEclip(topdown, 'green', 0, xrange, 'Vernal Equinox')
    drawObjectEclip(topdown, 'green', 180, xrange, '180d')
    drawObjectEclip(topdown, 'green', 90, yrange, '90d')
    drawObjectEclip(topdown, 'green', 270, yrange, '270d')

    #USC
    drawObjectEclip(topdown, 'blue', gc, xrange, '0d GC')
    drawObjectEclip(topdown, 'blue', (gc - 180), xrange, '180d GC')
    drawObjectEclip(topdown, 'blue', (gc - 90), yrange, '90d GC')
    drawObjectEclip(topdown, 'blue', (gc + 90), yrange, '180d GC')


def drawPlanets():
    # # mars
    # drawObjectEclip(topdown, 'green', 24, 1.465, 'Mars', 10, False)
    #
    # # jupiter
    # drawObjectEclip(topdown, 'green', 253, 5.347, 'Jupiter', 10, False)
    # drawObjectEclip(topdown, 'green', 282, 10, 'Saturn', 10, False)
    # drawObjectEclip(topdown, 'green', 28, 20, 'Uranus', 10, False)
    drawObjectEclip(topdown, 'green', 344, 30, 'Neptune', 10, False)

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
    return (x, y, z)

origin = origin_td
drawTopAxes()
origin = origin_sv
drawSVAxes()

origin = origin_td
drawObjectEclip(topdown, 'green', neptune_coors[0], neptune_coors[2], 'Neptune', default_scale, False)
origin = origin_sv
drawObjectEclip(sideview, 'green', neptune_coors[1], neptune_coors[2], 'Neptune', default_scale, False)
origin = origin_td
drawObjectEclip(topdown, 'green', pluto_coors[0], pluto_coors[2], 'Pluto', default_scale, False)
origin = origin_sv
drawObjectEclip(sideview, 'green', pluto_coors[1], pluto_coors[2], 'Pluto', default_scale, False)


origin = origin_td

neptune_coors = convert_to_new(neptune_coors)
print(neptune_coors)
drawObjectUSC(topdown, 'blue', neptune_coors[0], neptune_coors[2], 'Neptune', default_scale, False)
neptune_coors = convert_to_rect(neptune_coors)
drawObjectRect(topdown, 'red', neptune_coors[0], neptune_coors[1], neptune_coors[2], 'Neptune', default_scale)


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




