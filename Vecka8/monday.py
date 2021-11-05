glob_val = 10


def do_something(a, b):
    return (a + b) * glob_val


def do_with_side_effect(a):
    global glob_val
    glob_val += 1
    return glob_val + a


def tail(li: list) -> list:
    del li[0]
    return li


# Funktionen skall ta ett tal n och en optional lista
# Ger som resultat talen 0-n i slutet på listan
# foo(5) -> [0, 1, 2, 3, 4, 5]
# foo(5, [-2, -1]) -> [-2, -1, 0, 1, 2, 3, 4, 5]
def foo(n, li=[]):
    for i in range(n+1):
        li.append(i)
    return li


def run_foo():
    """Funktionen foo har ett defaultargument li som är en tom lista
    den tomma listan skapas redan vid funktionsdefinitionen och används
    sedan vid varje anrop till foo där vi inte själva skickar med en lista
    listan är ändringsbar, så varje gång vi kör funktionen kommer den att
    byggas på.
    Detta är ett vanligt exempel på en oavsedd sidoeffekt."""
    print(foo(5, [-2, -1]))
    print(foo(5))
    print(foo(5))
    print(foo(5))
    print(foo(5))
    print(foo(10, []))
    print(foo(2))


# Funktioner som objekt
def my_func(a, b=10):
    return a+b


def func_2(a):
    return a*a

if __name__ == '__main__':
    print(my_func(5))
    print(my_func(5, 2))

    my_func(5, 2)
    print(my_func)

    print(type("Hej"))
    print(type(my_func))

    f = my_func
    type(f)

    print(f(2))
    print(my_func(2))

    print(my_func.__name__)
    print(f.__name__)

    l1 = [1, 2, 3]
    l2 = l1

    print(l1)
    print(l2)

    l1.append(4)
    print(l1)
    print(l2)

    f_list = []
    f_list.append(my_func)
    f_list.append(func_2)
    print(f_list)

    for f in f_list:
        print(f.__name__, f(2))
