from math import sqrt


# Uppgift 53
# Skapa enhetstester för primtalsfaktoriseringen
# Det vi vill kontrollera är att funktionen/algoritmen vi använder för att
# ta fram alla primtalsfaktorer fungerar.


def prime_factors(num: int) -> list[int]:
    res = []
    # Vi börjar med att plocka ut alla faktorer 2 ur talen num
    # Exempel: 120 = 2 * 2 * 2 * 3 * 5
    # Här finns faktorn 2 med totalt 3 gånger. Loopen nedan tar bort dom en i taget och skriver ut i terminalen
    while num % 2 == 0:
        res.append(2)
        num = num / 2

    # Eftersom vi precis tagit bort samtliga faktorer 2 är det som återstår av talen num udda
    # Because math behöver vi bara leta primfaktorer upp till kvadratroten av num  plus 1
    # Eftersom alla faktorer 2 redan är borta räcker det att kolla udda tal
    for i in range(3, int(sqrt(num)) + 1, 2):
        while num % i == 0:
            res.append(i)
            num = num / i

    if num > 2:
        res.append(int(num))

    return res


def factors():
    num = int(input(">"))
    p_factors = prime_factors(num)
    for f in p_factors:
        print(f)


if __name__ == '__main__':
    factors()
