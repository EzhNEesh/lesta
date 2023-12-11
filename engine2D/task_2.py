from dataclasses import dataclass, field
from collections import deque


@dataclass
class ValueLimiter:
    def __init__(self, value=0):
        if not 0 <= value <= 255:
            raise ValueError(f'The color must be represented '
                             f'by an integers between 0 and 255: {value}')
        if not isinstance(value, int):
            raise TypeError(f'The color must be represented '
                            f'by an integers between 0 and 255: {value}')

        self.value = value


@dataclass
class Color:
    def __init__(self,
                 red: int = 0,
                 green: int = 0,
                 blue: int = 0
                 ):
        self.__red = ValueLimiter(red)
        self.__green = ValueLimiter(green)
        self.__blue = ValueLimiter(blue)

    @staticmethod
    def __int_to_hex(num):
        ValueLimiter(num)
        return '0' + hex(num)[-1] if num < 16 else hex(num)[-2:]

    def get_rgb_set(self):
        return self.__red.value, self.__green.value, self.__blue.value

    def get_hex_represent(self):
        return f'#{self.__int_to_hex(self.__red.value)[-2:].upper()}'\
               f'{self.__int_to_hex(self.__green.value)[-2:].upper()}'\
               f'{self.__int_to_hex(self.__blue.value)[-2:].upper()}'


@dataclass
class Point:
    _x: float = 0.0
    _y: float = 0.0

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = float(value)

    @property
    def y(self):
        return self._x

    @y.setter
    def y(self, value):
        self._x = float(value)


class Primitive:
    def draw(self, color: Color = Color()):
        pass


@dataclass
class Circle(Primitive):
    center: Point = Point(15.0, 15.0)
    radius: float = 5.0

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
