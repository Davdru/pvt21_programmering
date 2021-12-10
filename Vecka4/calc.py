import numbers


class CalculatorError(Exception):
    pass


def _check_operand(operand):
    if not isinstance(operand, numbers.Number):
        raise CalculatorError(f"Unsupported operand {operand} not a number")


def operand_checker(f):
    def inner(*operands):
        for operand in operands:
            _check_operand(operand)
        return f(*operands)
    return inner


@operand_checker
def add(a, b):
    _check_operand(a)
    _check_operand(b)
    return a + b


@operand_checker
def subtract(a, b):
    return a - b


@operand_checker
def multiply(a, b):
    return a * b


@operand_checker
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise CalculatorError(e)




if __name__ == '__main__':
    print(multiply("en text", 7))
