from dataclasses import dataclass, field


@dataclass
class Point:
    x: float = 0.0
    y: float = 0.0


class Primitive:
    def draw(self):
        pass


@dataclass
class Circle(Primitive):
    center: Point = Point(15.0, 15.0)
    radius: float = 5.0

    def draw(self):
        print(f'Drawing Circle: ({self.center.x, self.center.y}) with radius {self.radius}')


@dataclass
class Triangle(Primitive):
    a: Point = Point(5.0, 5.0)
    b: Point = Point(10.0, 10.0)
    c: Point = Point(5.0, 10.0)

    def draw(self):
        print(f'Drawing Triangle with points ({self.a.x, self.a.y})({self.b.x, self.b.y})({self.c.x, self.c.y})')


@dataclass
class Rectangle(Primitive):
    a: Point = Point(20.0, 20.0)
    b: Point = Point(30.0, 30.0)

    def draw(self):
        print(f'Drawing Rectangle with corner points {self.a.x, self.a.y} and {self.b.x, self.b.y}')


@dataclass
class Engine2D:
    canvas: list[Primitive] = field(default_factory=lambda: [])
    pepe: int = None

    def add_figure(self, primitive: Primitive):
        print(type(primitive))
        self.canvas.append(primitive)
