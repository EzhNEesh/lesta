import pytest
from engine2D.task_2 import *


def test_color_empty():
    color = Color()
    assert color.get_rgb_set() == (0, 0, 0)
    color = Color(red=1)
    assert color.get_rgb_set() == (1, 0, 0)
    color = Color(green=1)
    assert color.get_rgb_set() == (0, 1, 0)
    color = Color(blue=1)
    assert color.get_rgb_set() == (0, 0, 1)


@pytest.mark.parametrize(
    'red, green, blue',
    [
        (0, 0, 0),
        (255, 255, 255)
    ]
)
def test_color_not_empty(red, green, blue):
    color = Color(red, green, blue)
    assert color.get_rgb_set() == (red, green, blue)


@pytest.mark.parametrize(
    'red, green, blue',
    [
        (-1, 0, 0),
        (0, -1, 0),
        (0, 0, -1),
        (256, 0, 0),
        (0, 256, 0),
        (0, 0, 256)
    ]
)
def test_color_value_exceptions(red, green, blue):
    with pytest.raises(ValueError):
        Color(red, green, blue)


@pytest.mark.parametrize(
    'red, green, blue',
    [
        (1.1, 0, 0),
        (0, 1.1, 0),
        (0, 0, 1.1),
        ('256', 0, 0),
        (0, '256', 0),
        (0, 0, '256'),
        (None, 0, 0),
        (0, None, 0),
        (0, 0, None)
    ]
)
def test_color_type_exceptions(red, green, blue):
    with pytest.raises(TypeError):
        Color(red, green, blue)


def test_color_get_hex_represent():
    color = Color()
    assert color.get_hex_represent() == '#000000'
    color = Color(195, 5, 214)
    assert color.get_hex_represent() == '#C305D6'
    color = Color(255, 255, 255)
    assert color.get_hex_represent() == '#FFFFFF'
