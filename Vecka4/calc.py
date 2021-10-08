import numbers


class CalculatorError(Exception):
    pass


def add(a, b):
    _check_operand(a)
    _check_operand(b)
    return a + b


def subtract(a, b):
    _check_operand(a)
    _check_operand(b)
    return a - b


def multiply(a, b):
    _check_operand(a)
    _check_operand(b)
    return a * b


def divide(a, b):
    _check_operand(a)
    _check_operand(b)
    try:
        return a / b
    except ZeroDivisionError as e:
        raise CalculatorError(e)


def _check_operand(operand):
    if not isinstance(operand, numbers.Number):
        raise CalculatorError(f"Unsupported operand {operand} not a number")


if __name__ == '__main__':
    print(multiply("en text", 7))
