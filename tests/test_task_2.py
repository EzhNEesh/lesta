import contextlib

import pytest
from contextlib import nullcontext as does_not_raise
from engine2D.task_2 import *


class TestColor:
    def test_color_empty(self):
        color = Color()
        assert color.get_rgb_set() == (0, 0, 0)
        color = Color(red=1)
        assert color.get_rgb_set() == (1, 0, 0)
        color = Color(green=1)
        assert color.get_rgb_set() == (0, 1, 0)
        color = Color(blue=1)
        assert color.get_rgb_set() == (0, 0, 1)

    @pytest.mark.parametrize(
        'red, green, blue, expectation',
        [
            (0, 0, 0, does_not_raise()),
            (255, 255, 255, does_not_raise()),
            (-1, 0, 0, pytest.raises(ValueError)),
            (0, -1, 0, pytest.raises(ValueError)),
            (0, 0, -1, pytest.raises(ValueError)),
            (256, 0, 0, pytest.raises(ValueError)),
            (0, 256, 0, pytest.raises(ValueError)),
            (0, 0, 256, pytest.raises(ValueError)),
            (1.1, 0, 0, pytest.raises(TypeError)),
            (0, 1.1, 0, pytest.raises(TypeError)),
            (0, 0, 1.1, pytest.raises(TypeError)),
            ('256', 0, 0, pytest.raises(TypeError)),
            (0, '256', 0, pytest.raises(TypeError)),
            (0, 0, '256', pytest.raises(TypeError)),
            (None, 0, 0, pytest.raises(TypeError)),
            (0, None, 0, pytest.raises(TypeError)),
            (0, 0, None, pytest.raises(TypeError))
        ]
    )
    def test_color_not_empty(self, red, green, blue, expectation):
        with expectation:
            color = Color(red, green, blue)
            assert color.get_rgb_set() == (red, green, blue)

    def test_color_get_hex_represent(self):
        color = Color()
        assert color.get_hex_represent() == '#000000'
        color = Color(195, 5, 214)
        assert color.get_hex_represent() == '#C305D6'
        color = Color(255, 255, 255)
        assert color.get_hex_represent() == '#FFFFFF'


class TestPoint:
    def test_point_empty(self):
        point = Point()
        assert (point.x, point.y) == (0.0, 0.0)
        point = Point(x=1.0)
        assert (point.x, point.y) == (1.0, 0.0)
        point = Point(y=1)
        assert (point.x, point.y) == (0.0, 1.0)

    @pytest.mark.parametrize(
        'x, y, expectation',
        [
            (1, 1, does_not_raise()),
            (1.5, 1.5, does_not_raise()),
            (-100, -100, does_not_raise()),
            ('1', 1, does_not_raise()),
            (1, '1', does_not_raise()),
            ('1', '1', does_not_raise()),
            (None, 1, pytest.raises(TypeError)),
            (1, None, pytest.raises(TypeError)),
            ('a', 1, pytest.raises(ValueError)),
            (1, 'a', pytest.raises(ValueError))
        ]
    )
    def test_point_not_empty(self, x, y, expectation):
        with expectation:
            point = Point(x, y)
            assert (point.x, point.y) == (float(x), float(y))


class TestPrimitives:
    def test_circle_empty(self):
        circle = Circle()
        assert (circle.center.get_coordinates(), circle.radius) == ((15, 15), 5.)
        circle = Circle(center=Point(1, 1))
        assert (circle.center.get_coordinates(), circle.radius) == ((1., 1.), 5.)
        circle = Circle(radius=10)
        assert (circle.center.get_coordinates(), circle.radius) == ((15., 15.), 10.)

    @pytest.mark.parametrize(
        ('center', 'radius', 'expectation'),
        [
            (Point(1, 1), 1, does_not_raise()),
            (Point(1, 1), '1', does_not_raise()),
            (None, 1, pytest.raises(TypeError)),
            (Point(1, 1), None, pytest.raises(TypeError))
        ]
    )
    def test_circe_not_empty(self, center, radius, expectation):
        with expectation:
            circle = Circle(center, radius)
            assert (circle.center.get_coordinates()) == (center.get_coordinates())
            assert circle.radius == float(radius)

    def test_circle_draw(self, capfd):
        circle = Circle(Point(10, 10), 5)
        color = Color(0, 100, 200)
        circle.draw(color)
        out, err = capfd.readouterr()
        assert out == 'Drawing Circle(#0064C8): (10.0, 10.0) with radius 5.0\n'

    def test_triangle_empty(self):
        triangle = Triangle()
        assert (
                (triangle.a.get_coordinates(), triangle.b.get_coordinates(), triangle.c.get_coordinates()) ==
                ((5.0, 5.0), (10.0, 10.0), (5.0, 10.0))
        )
        triangle = Triangle(a=Point(20.5, 20.5))
        assert (
                (triangle.a.get_coordinates(), triangle.b.get_coordinates(), triangle.c.get_coordinates()) ==
                ((20.5, 20.5), (10.0, 10.0), (5.0, 10.0))
        )
        triangle = Triangle(b=Point(20.5, 20.5))
        assert (
                (triangle.a.get_coordinates(), triangle.b.get_coordinates(), triangle.c.get_coordinates()) ==
                ((5., 5.), (20.5, 20.5), (5.0, 10.0))
        )
        triangle = Triangle(c=Point(20.5, 20.5))
        assert (
                (triangle.a.get_coordinates(), triangle.b.get_coordinates(), triangle.c.get_coordinates()) ==
                ((5., 5.), (10., 10.), (20.5, 20.5))
        )

    @pytest.mark.parametrize(
        'a, b, c, expectation',
        [
            (Point(1, 1), Point(2, 2), Point(2, 1), does_not_raise()),
            (None, Point(2, 2), Point(2, 1), pytest.raises(TypeError)),
            (Point(2, 2), None, Point(2, 1), pytest.raises(TypeError)),
            (Point(2, 2), Point(2, 1), None, pytest.raises(TypeError))
        ]
    )
    def test_triangle_not_empty(self, a, b, c, expectation):
        with expectation:
            triangle = Triangle(a, b, c)
            assert (
                    (triangle.a.get_coordinates(), triangle.b.get_coordinates(), triangle.c.get_coordinates()) ==
                    (a.get_coordinates(), b.get_coordinates(), c.get_coordinates())
            )

    def test_triangle_draw(self, capfd):
        triangle = Triangle(Point(10, 10), Point(20, 20), Point(10, 20))
        color = Color(200, 0, 100)
        triangle.draw(color)
        out, err = capfd.readouterr()
        assert out == 'Drawing Triangle(#C80064) with points (10.0, 10.0), (20.0, 20.0), (10.0, 20.0)\n'

    def test_rectangle_empty(self):
        rectangle = Rectangle()
        assert (
                (rectangle.a.get_coordinates(), rectangle.b.get_coordinates()) ==
                ((20.0, 20.0), (30.0, 30.0))
        )
        rectangle = Rectangle(a=Point(10.5, 10.5))
        assert (
                (rectangle.a.get_coordinates(), rectangle.b.get_coordinates()) ==
                ((10.5, 10.5), (30.0, 30.0))
        )
        rectangle = Rectangle(b=Point(40.5, 40.5))
        assert (
                (rectangle.a.get_coordinates(), rectangle.b.get_coordinates()) ==
                ((20., 20.), (40.5, 40.5))
        )

    @pytest.mark.parametrize(
        'a, b, expectation',
        [
            (Point(10, 10), Point(20, 20), does_not_raise()),
            (None, Point(20, 20), pytest.raises(TypeError)),
            (Point(20, 20), None, pytest.raises(TypeError)),
        ]
    )
    def test_rectangle_not_empty(self, a, b, expectation):
        with expectation:
            rectangle = Rectangle(a, b)
            assert (
                    (rectangle.a.get_coordinates(), rectangle.b.get_coordinates()) ==
                    (a.get_coordinates(), b.get_coordinates())
            )


class TestEngine2D:
    def test_init(self):
        engine = Engine2D()
        assert isinstance(engine.canvas, deque)

    @pytest.mark.parametrize(
        'primitives_list, expectation',
        [
            ([Circle()], does_not_raise()),
            ([Triangle()], does_not_raise()),
            ([Rectangle()], does_not_raise()),
            ([
                Circle(),
                Triangle(),
                Rectangle(),
                Circle(Point(10, 20), 10),
                Triangle(Point(8, 8), Point(30, 30), Point(3, 25)),
                Rectangle(Point(30, 5), Point(10, 70))
            ], does_not_raise()),
            ([None], pytest.raises(TypeError))
        ]
    )
    def test_add_figure(self, primitives_list, expectation):
        engine = Engine2D()
        with expectation:
            for primitive in primitives_list:
                engine.add_figure(primitive)
        for i, primitive in enumerate(engine.canvas):
            assert primitive[0] is primitives_list[i], f'primitives_list[{i}] is not equal'

    def test_change_color(self):
        engine = Engine2D()
        engine.change_color(Color(255, 255, 255))
        engine.add_figure(Circle())
        assert engine.canvas[0][1].get_rgb_set() == (255, 255, 255)
