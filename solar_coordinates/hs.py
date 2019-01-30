from turtle import *
from solar_coordinates.utilities import ellipse, draw_dashes


class HS:
    def __init__(self):
        self.turtle = Turtle()
        bgcolor('white')
        self.turtle.shape('circle')
        self.turtle.resizemode('auto')
        self.xrange = 720
        self.yrange = 180
        self.xscale = int(self.xrange / 30)
        self.yscale = int(self.yrange / 30)
        self.offset = 100
        self.origin = self.turtle.pos()
        self.heading = 7.25
        self.zero_long = 266
        self.base_pensize = self.turtle.pensize()
        self.degree = u'\xb0'
        self.draw_ecliptic_axes()

    def draw_ecliptic_axes(self):
        self.reset()
        self.turtle.color('black')
        self.turtle.setheading(self.heading)
        self.turtle.penup()
        self.turtle.forward(self.xrange)
        self.turtle.pendown()
        self.turtle.left(90)
        ellipse(self.turtle, self.yrange, self.xrange)
        self.reset()
        self.turtle.left(90)
        draw_dashes(self.turtle, self.yrange+40)
        self.write_name('90' + self.degree + ' lat (HS Axis)', 20)
        self.reset()
        self.turtle.right(90)
        draw_dashes(self.turtle, self.yrange+40)
        self.reset()
        self.turtle.left(self.zero_long)
        draw_dashes(self.turtle, self.yrange)
        self.write_name('0' + self.degree + ' long', 30)
        self.reset()

    def write_name(self, name, offset=20):
        temp_origin = self.turtle.pos()
        temp_heading = self.turtle.heading()
        self.turtle.penup()
        self.turtle.forward(offset)
        self.turtle.pendown()
        self.turtle.write(name, False, align="center", font=("Arial", 12, "normal"))
        self.turtle.penup()
        self.turtle.setpos(temp_origin)
        self.turtle.setheading(temp_heading)
        self.turtle.pendown()

    def reset(self):
        self.turtle.penup()
        self.turtle.setpos(self.origin)
        self.turtle.setheading(self.heading)
        self.turtle.pensize(self.base_pensize)
        self.turtle.pendown()

    def draw_object_eclip(self, name, longitude, r, color, size=5):
        self.turtle.setheading(self.zero_long)
        self.turtle.color(color)
        self.turtle.left(longitude)
        temp_long = longitude
        if temp_long >= 180:
            temp_long = temp_long - 180
        if temp_long >= 90:
            temp_long = 180 - temp_long
        ratio = temp_long / 90.0
        smart_scale = self.yscale * ratio + self.xscale * (1 - ratio)
        self.turtle.forward(r * smart_scale + self.offset)
        name_offset = 60
        if name == 'Neptune':
            name_offset = 80
        print(name_offset, name)
        self.write_name(name + ' ' + str(longitude) + self.degree, name_offset)
        self.turtle.pensize(size)
        self.turtle.stamp()

    def draw_planet(self, **planet_info):
        self.reset()
        r = float(planet_info.get('distance'))
        longitude = float(planet_info.get('longitude'))
        name = planet_info.get('name')
        color = planet_info.get('color')
        size = float(planet_info.get('size'))

        longitude = longitude - self.zero_long
        if longitude < 0:
            longitude = longitude + 360

        self.draw_object_eclip(name, longitude, r, color, size)

    def draw_sun(self):
        self.reset()
        self.turtle.penup()
        self.turtle.forward(-20)
        self.turtle.left(90)
        self.turtle.pendown()
        self.turtle.color('gold')
        self.write_name('Sun', 60)
        self.reset()
        self.turtle.pensize(20)
        self.turtle.stamp()

    def wait(self):
        done()
        
        


