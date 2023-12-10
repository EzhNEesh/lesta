from dataclasses import dataclass, field
from collections import deque


@dataclass
class Color:
    def __init__(self,
                 red: int = 0,
                 green: int = 0,
                 blue: int = 0
                 ):
        if not (0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255):
            raise Exception(ValueError, f'The color must be represented '
                                        f'by an integers between 0 and 255: ({red}, {green}, {blue}')
        if not (isinstance(red, int) and isinstance(green, int) and isinstance(blue, int)):
            raise Exception(TypeError, f'The color must be represented '
                                       f'by an integers between 0 and 255: ({red}, {green}, {blue}')

        self.red = red
        self.green = green
        self.blue = blue

    @staticmethod
    def int_to_hex(num):
        return '0' + hex(num)[-1] if num < 16 else hex(num)[-2:]

    def get_hex_represent(self):
        return f'#{self.int_to_hex(self.red)[-2:].upper()}'\
               f'{self.int_to_hex(self.green)[-2:].upper()}'\
               f'{self.int_to_hex(self.blue)[-2:].upper()}'


@dataclass
class Point:
    x: float = 0.0
    y: float = 0.0


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
