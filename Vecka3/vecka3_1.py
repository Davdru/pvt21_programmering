

def square(x: int) -> int:
    return x * x


def mul(a: int, b: int) -> int:
    return a * b


if __name__ == '__main__':
    print(mul(10, 2))  # 20?
    print(mul(5, 5))

    print(square(2))
    print(square(mul(2, 2)))
