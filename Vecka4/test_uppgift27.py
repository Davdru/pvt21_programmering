import pytest
from calc import add, multiply, divide, CalculatorError

# 1. Sätt upp, vilka förutsättnignar krävs för att testa
# 2. Gör
# 3. Assert, kontrollera att utfallet blev det vi förväntade oss


def test_add():
    result = add(2, 3)
    assert result == 5

def test_add_zero():
    assert add(5, 0) == 5


def test_add_zero2():
    assert add(0, 10) == 10


def test_add_str_and_num():
    with pytest.raises(CalculatorError):
        add("Hej", 10)


def test_add_num_and_str():
    with pytest.raises(CalculatorError):
        add(5, "en text")


def test_multiply_num_num():
    assert multiply(10, 3) == 30


def test_multiply_str_str():
    with pytest.raises(CalculatorError):
        multiply("en text", "en annan text")


def test_multiply_str_int():
    with pytest.raises(CalculatorError):
        multiply("en text", 7)


def test_multiply_int_str():
    with pytest.raises(CalculatorError):
        multiply(9, "en text")


def test_multiply_float_int():
    assert multiply(1.5, 10) == 15.0


def test_multiply_complex_float():
    assert multiply((1+2j), 3.0) == (3+6j)


def test_divide_by_zero():
    with pytest.raises(CalculatorError):
        divide(10, 0)


