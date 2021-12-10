from uppgift28 import count_vowels
import pytest

def test_count_vowels():
    assert count_vowels("aouåeiyäö") == 9


def test_count_uppercase_vowels():
    assert count_vowels("aouåeiyäö".upper()) == 9


def test_count_non_vowels():
    assert count_vowels("bcdfghjklmnpqrstvwxz") == 0


def test_count_upper_case_non_vowels():
    assert count_vowels("bcdfghjklmnpqrstvwxz".upper()) == 0


def test_non_alpha_chars():
    assert count_vowels("@£$€{[]}$£€][1234567890") == 0


# def test_numerical():
#     assert count_vowels(183576187617891568713857631) == 0


def test_iterable_non_char():
    assert count_vowels(["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]) == 0


def test_iterable_char():
    assert count_vowels(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]) == 3
