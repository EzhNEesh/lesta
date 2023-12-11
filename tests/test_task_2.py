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
    def test_point(self, x, y, expectation):
        with expectation:
            point = Point(x, y)
            assert (point.x, point.y) == (float(x), float(y))
