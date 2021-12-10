import functools
import operator


def maximum(a: int, b: int, c: int) -> int:
    if a > b:
        test = a
    else:
        test = b
    if test > c:
        return test
    else:
        return c


def maximum2(a: int, b: int, c: int) -> int:
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c



# Mer lätt läst än de två första versionerna.
def maximum3(a: int, b: int, c: int) -> int:
    tmp_max = a
    if tmp_max < b:
        tmp_max = b
    if tmp_max < c:
        tmp_max = c
    return tmp_max


# Generaliserad version av maximum3 som fungerar på godtyckliga listor
def max_av_lista(talen: list[int]) -> int:
    tmp_max = talen[0]
    for i in talen:
        if tmp_max < i:
            tmp_max = i
    return tmp_max


def summera(lista: list[int]) -> int:
    summerar = 0
    for i in lista:
        summerar += i
    return summerar


def summera2(lista: list[int]) -> int:
    return functools.reduce(operator.add, lista)
# Reduce tar en lista av saker, ex [1,2,3,4]
# Tar de två första element, 1, 2 och skickar som argument till add, dvs add(1,2)
# Tar resultatet av föregående steg (3) och nästa element i listan och skickar in i add, dvs (3, 3)

def mul_list(lista: list[int]) -> int:
    m = 1
    for i in lista:
        m = m*i
    return m

def mul_list2(lista: list[int]) -> int:
    return functools.reduce(operator.mul, lista)





def test_maximum():
    assert maximum(1, 2, 3) == 3
    assert maximum(5, 2, 1) == 5
    assert maximum(-15, 1231, 5) == 1231
    assert maximum(5, 2, 555) == 555
    assert maximum(1, 2, 3) == max(1, 2, 3)
    assert maximum(5, 5, 5) == 5
    assert maximum2(1, 2, 3) == 3
    assert maximum2(5, 2, 1) == 5
    assert maximum2(-15, 1231, 5) == 1231
    assert maximum2(5, 2, 555) == 555
    assert maximum2(1, 2, 3) == max(1, 2, 3)
    assert maximum2(5, 5, 5) == 5
    assert maximum2(5, 5, 1) == 5
    assert maximum3(1, 2, 3) == 3
    assert maximum3(5, 2, 1) == 5
    assert maximum3(-15, 1231, 5) == 1231
    assert maximum3(5, 2, 555) == 555
    assert maximum3(1, 2, 3) == max(1, 2, 3)
    assert maximum3(5, 5, 5) == 5
    assert maximum3(5, 5, 1) == 5
    assert max_av_lista([1, 2, 3, 4, 5]) == 5
    assert max_av_lista([4, 1, 10, 1, 7, 9]) == 10


if __name__ == '__main__':
    print(f"Summan av alla tal är {summera2([10, 20, 30])}")
    print(f"Summan av alla tal är {summera2([10, 20, 30, 40])}")

    print(f"{mul_list2([1, 2, 3, 4, 5])} Borde bli 120")
    print(f"{mul_list2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])}")