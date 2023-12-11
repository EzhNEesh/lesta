from dataclasses import dataclass, field
from collections import deque


@dataclass
class Color:
    def __init__(
            self,
            red: int = 0,
            green: int = 0,
            blue: int = 0,
    ):
        self.red = red
        self.green = green
        self.blue = blue

    @staticmethod
    def is_valid_color(value):
        if not 0 <= value <= 255:
            raise ValueError(f'The color must be represented '
                             f'by an integers between 0 and 255: {value}')
        if not isinstance(value, int):
            raise TypeError(f'The color must be represented '
                            f'by an integers between 0 and 255: {value}')

    @property
    def red(self):
        return self._red

    @red.setter
    def red(self, red):
        self.is_valid_color(red)
        self._red = red

    @property
    def green(self):
        return self._green

    @green.setter
    def green(self, green):
        self.is_valid_color(green)
        self._green = green

    @property
    def blue(self):
        return self._blue

    @blue.setter
    def blue(self, blue):
        self.is_valid_color(blue)
        self._blue = blue

    def __int_to_hex(self, num):
        self.is_valid_color(num)
        return '0' + hex(num)[-1] if num < 16 else hex(num)[-2:]

    def get_rgb_set(self):
        return self._red, self._green, self._blue

    def get_hex_represent(self):
        return f'#{self.__int_to_hex(self._red)[-2:].upper()}'\
               f'{self.__int_to_hex(self._green)[-2:].upper()}'\
               f'{self.__int_to_hex(self._blue)[-2:].upper()}'


@dataclass
class Point:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = float(value)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = float(value)


class Primitive:
    def draw(self, color: Color = Color()):
        pass


@dataclass
class Circle(Primitive):
    def __init__(self, center: Point = Point(15.0, 15.0), radius: float = 5.0):
        self.center = center
        self.radius = radius

    @property
    def center(self):
        return self._center

    @center.setter
    def center(self, new_center):
        if not isinstance(new_center, Point):
            print('meow')
            raise TypeError(f'Circle center must be Point(): {type(new_center)}')
        self._center = new_center

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, new_radius):
        self._radius = float(new_radius)

    def draw(self, color: Color = Color()):
        print(f'Drawing Circle({color.get_hex_represent()}): '
              f'{self.center.x, self.center.y} with radius {self.radius}')


@dataclass
class Triangle(Primitive):
    a: Point = Point(5.0, 5.0)
    b: Point = Point(10.0, 10.0)
    c: Point = Point(5.0, 10.0)

    def draw(self, color: Color = Color()):
        print(f'Drawing Triangle({color.get_hex_represent()}) '
              f'with points {self.a.x, self.a.y}, {self.b.x, self.b.y}, {self.c.x, self.c.y}')


@dataclass
class Rectangle(Primitive):
    a: Point = Point(20.0, 20.0)
    b: Point = Point(30.0, 30.0)

    def draw(self, color: Color = Color()):
        print(f'Drawing Rectangle({color.get_hex_represent()}) '
              f'with corner points {self.a.x, self.a.y} and {self.b.x, self.b.y}')


@dataclass
class Engine2D:
    canvas: deque[(Primitive, Color)] = field(default_factory=lambda: deque())
    current_color = Color()

    def add_figure(self, primitive: Primitive):
        self.canvas.append((primitive, self.current_color))

    def draw(self):
        while len(self.canvas):
            primitive = self.canvas.popleft()
            primitive[0].draw(primitive[1])

    def change_color(self, new_color: Color = Color(0, 0, 0)):
        self.current_color = new_color
