# 14.1 Utan att köra programmet längst ned i denna uppgift, försök beskriva vad det gör.
# 14.2 Modifiera programmet så att inte bara "kind" skrivs ut i write_things-funktionen, utan också antalet things t.ex "CARS (3 st)"
# 14.3 Lägg till en ny kategori av saker till programmet, hitta på något! Och lägg i items av denna sort i en ny lista, som skrivs ut på slutet.
# 14.4 Skriv ut items i alfabetisk ordning.
# 14.5 Låt användaren mata in innehåll i basket i form av en kommaseparerad sträng, t.ex. kan användaren mata in "banana,apple, orange" och det tolkas som listan ["banana", "apple", "orange"]


# uppgift14.py
FRUITS = ['banana', 'apple', 'orange']
CARS = ['volvo', 'ford', 'tesla']


def run():
    basket = [
    'volvo', 'is', 'an', 'orange', 'apple'
    ]
    cars = []
    fruits = []
    rest = []
    for item in basket:
        if item in CARS:
          cars.append(item)
        elif item in FRUITS:
            fruits.append(item)
        else:
            rest.append(item)
    write_things(cars, 'Cars')
    write_things(fruits, 'Fruits')
    write_things(rest, 'Misc')


def write_things(items, kind):
    print(f"{kind.upper()}")
    for item in items:
        print(f" {item}")


if __name__ == '__main__':
    run()