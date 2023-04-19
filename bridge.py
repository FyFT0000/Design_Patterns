""" Scenario:
    Implementation independent circle abstraction: Defining the propierties if a circle and scaling it.
    Implementation dependant circle abstraction: How to draw a circle. """

class DrawingAPIOne(object):
    """ Implementation-specific abstraction: concrete class one """
    def draw_circle(self, x, y, radius):
        print(f'API 1 drawing a circle at ({x}, {y}, with radius {radius})')

class DrawingAPITwo(object):
    """ Implementation-specific abstraction concrete class two """
    def draw_circle(self, x, y, radius):
        print(f'API 2 drawing a circle at ({x}, {y}, with radius {radius})')

class Circle():
    """ Implementation-independent abstraction: for example, there could... """
    def __init__(self, x, y, radius, drawing_api) -> None:
        """ Initialize the necessary atributes """
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        """ Implementation-specific abstraction taken care of by another... """
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, percent):
        """ Implementation-independent """
        self._radius *= percent

#Build the first Circle objet using API One
circle1 = Circle(1, 2, 3, DrawingAPIOne())
#Draw a circle
circle1.draw()

#Build the second Circle objet using API Two
circle2 = Circle(2, 3, 4, DrawingAPITwo())
#Draw a circle
circle2.draw()

