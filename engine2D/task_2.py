from collections import deque


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


class Point:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError(f'A point\'s coordinates must be integer: {type(value)}')
        value = int(value)
        if value < 0:
            raise ValueError(f'A point\'s coordinates must be greater than or equal to zero: x = {value}')
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError(f'A point\'s coordinates must be integer: {type(value)}')
        value = int(value)
        if value < 0:
            raise ValueError(f'A point\'s coordinates must be greater than or equal to zero: x = {value}')
        self._y = int(value)

    def get_coordinates(self):
        return self.x, self.y


class Primitive:
    def draw(self, color: Color = Color()):
        pass


class Circle(Primitive):
    def __init__(self, center: Point = Point(15, 15), radius: int = 5):
        self.center = center
        self.radius = radius

    @property
    def center(self):
        return self._center

    @center.setter
    def center(self, new_center):
        if not isinstance(new_center, Point):
            raise TypeError(f'Circle center must be Point(): {type(new_center)}')
        self._center = new_center

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, new_radius):
        self._radius = int(new_radius)

    def draw(self, color: Color = Color()):
        print(f'Drawing Circle({color.get_hex_represent()}): '
              f'{self.center.get_coordinates()} with radius {self.radius}')


class Triangle(Primitive):
    def __init__(self,
                 a: Point = Point(5, 5),
                 b: Point = Point(10, 10),
                 c: Point = Point(5, 10)
                 ):
        self.a = a
        self.b = b
        self.c = c

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, new_a):
        if not isinstance(new_a, Point):
            raise TypeError(f'New point must be Point: {type(new_a)}')
        self._a = new_a

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, new_b):
        if not isinstance(new_b, Point):
            raise TypeError(f'New point must be Point: {type(new_b)}')
        self._b = new_b

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, new_c):
        if not isinstance(new_c, Point):
            raise TypeError(f'New point must be Point: {type(new_c)}')
        self._c = new_c

    def draw(self, color: Color = Color()):
        print(f'Drawing Triangle({color.get_hex_represent()}) '
              f'with points {self.a.get_coordinates()}, {self.b.get_coordinates()}, {self.c.get_coordinates()}')


class Rectangle(Primitive):
    def __init__(self, a: Point = Point(20, 20), b: Point = Point(30, 30)):
        self.a = a
        self.b = b

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, new_a):
        if not isinstance(new_a, Point):
            raise TypeError(f'New point must be Point: {type(new_a)}')
        self._a = new_a

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, new_b):
        if not isinstance(new_b, Point):
            raise TypeError(f'New point must be Point: {type(new_b)}')
        self._b = new_b

    def draw(self, color: Color = Color()):
        print(f'Drawing Rectangle({color.get_hex_represent()}) '
              f'with corner points {self.a.get_coordinates()} and {self.b.get_coordinates()}')


class Engine2D:
    def __init__(self):
        self.__canvas = deque()
        self.__current_color = Color()

    @property
    def canvas(self):
        return self.__canvas.copy()

    def add_figure(self, primitive: Primitive):
        if not isinstance(primitive, Primitive):
            raise TypeError(f'A new figure must be Primitive: {type(primitive)}')
        self.__canvas.append((primitive, self.__current_color))

    def draw(self):
        while len(self.__canvas):
            primitive = self.__canvas.popleft()
            primitive[0].draw(primitive[1])

    def change_color(self, new_color: Color = Color(0, 0, 0)):
        if not isinstance(new_color, Color):
            raise TypeError(f'A new color must be Color: {type(new_color)}')
        self.__current_color = new_color
