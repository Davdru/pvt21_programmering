from math import sqrt


# Uppgift 53
# Skapa enhetstester för primtalsfaktoriseringen
# Det vi vill kontrollera är att funktionen/algoritmen vi använder för att
# ta fram alla primtalsfaktorer fungerar.
# Ni kommer märka att det blir lite komplicerat att testa eftersom


def factors():
    num = int(input(">"))
    # Vi börjar med att plocka ut alla faktorer 2 ur talen num
    # Exempel: 120 = 2 * 2 * 2 * 3 * 5
    # Här finns faktorn 2 med totalt 3 gånger. Loopen nedan tar bort dom en i taget och skriver ut i terminalen
    while num % 2 == 0:
        print(2)
        num = num / 2

    # Eftersom vi precis tagit bort samtliga faktorer 2 är det som återstår av talen num udda
    # Because math behöver vi bara leta primfaktorer upp till kvadratroten av num  plus 1
    # Eftersom alla faktorer 2 redan är borta räcker det att kolla udda tal
    for i in range(3, int(sqrt(num)) + 1, 2):
        while num % i == 0:
            print(i)
            num = num / i

    if num > 2:
        print(int(num))


if __name__ == '__main__':
    factors()
