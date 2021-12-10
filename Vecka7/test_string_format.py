import pytest
from string_format import find_max


def test_find_max():
    assert find_max((12, 35, 6, 5, 3, 99)) == 99


def test_find_max_neg():
    assert find_max((-12, -124, -1)) == -1


def test_find_max_neg_and_pos():
    assert find_max((-12, 2, -1)) == 2


def test_find_max_empty_tuple():
    with pytest.raises(ValueError):
        find_max(tuple())


def test_find_max_string_argument():
    with pytest.raises(TypeError):
        find_max("Hej")