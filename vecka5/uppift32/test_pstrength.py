import pytest
import pwstrength


def test_10_char_str():
    assert pwstrength.compute_strength("abcdefghij") == 0

def test_11_char_str():
    assert pwstrength.compute_strength("abcdefghijk") == 1

def test_0_char_str():
    assert pwstrength.compute_strength("") == 0

def test_letters_number_less_than_10_ch():
    assert pwstrength.compute_strength("abc123") == 1

def test_letters_number_more_than_10_ch():
    assert pwstrength.compute_strength("abc123asdfgfhghh") == 2

def test_special_char_only():
    assert pwstrength.compute_strength("#%&+_-") == 1

def test_special_char_and_letters_more_than_10():
    assert pwstrength.compute_strength("#%&+_-askldjhfalkdsjhg") == 2

def test_special_char_letters_number_more_than_10():
    assert pwstrength.compute_strength("#%&+_-1254194kajsdfkjashf") == 3

def test_invalid_char():
    assert pwstrength.compute_strength("ksajhgkjhakj$%)") == 0

