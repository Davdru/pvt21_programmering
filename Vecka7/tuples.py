import random


def line():
    print("-" * 80)


l = [1, 2, 3, 4, 4]
print(l[0])
print(l[3])

print("-" * 80)

t = (1, 2, 3, 4, 4)
print(t[0])
print(t[3])

print("-" * 80)

d = {1: "1", 2: "2", 2: "2"}
print(d)
print(d[2])
d[2] = 100
print(d[2])
print(d)
print("-" * 80)

l2 = [1, 2, 3, 4, 5]
print(l2)
l2[2] = 100
print(l2)
print("-" * 80)

t2 = (1, 2, 3, 4, 5)
print(t2)
print("-" * 80)


# En funktion som ger en slumpmässig koordinat tillbaks
def random_point(x_min=0, x_max=10, y_min=0, y_max=10):
    x = random.randint(x_min, x_max)
    y = random.randint(y_min, y_max)
    return x, y  # Paranteser är inte nödvändiga, det skapas en tuple ändå


p = random_point(-10, 10, -10, 10)
print(type(p))
print(f"x:{p[0]}, y:{p[1]}")

x, y = p
print(f"x:{x}, y:{y}")

# Vi kan packa upp returvärdet direkt
x2, y2 = random_point()
print(f"x:{x2}, y:{y2}")
print("-" * 80)

t3 = (1, 2, 3)
try:
    a, b = t3
except ValueError:
    print("När vi använder en tuple unpack på det här viset måste antalet element och variabler matcha")
print("-" * 80)

# Första elementet hamnar i a, resten som en lista i b
a, *b = t3
print(a)
print(b)
print("-" * 80)

t4 = (1, 2, 3, 4, 5, 6.99, 7, 8, 9, "Hej")
a, *b, c = t4
# Första elementet hamnar i a
# Sista elementet i c
# Resten som en lista i b

print(f"Första elementet {a}")
print(f"Sista elementet {c}")
print(f"Övriga {b}")
print("-" * 80)

t5 = (1, 2, 3)
t6 = (4, 5, 6)

print((t5, t6))
t7 = t5[0], t5[1], t5[2], t6[0], t6[1], t6[2]
print(t7)

# * på höger sida som här packar upp en tuple,
# i det här fallet skapas en ny tuple med alla värden från
# t5 och alla värden från t6
t8 = (*t5, *t6)
print(t8)
print("-" * 80)


def print_xy(x, y):
    print(f"x:{x}, y:{y}")


p2 = random_point()
print(p2)

print_xy(p2[0], p2[1])
# Vi kan packa upp en tuple för att fylla argumenten till print_xy
print_xy(*p2)

p3 = (10, 5, 1)
try:
    print_xy(*p3)
except TypeError:
    print(
        "Om vi använder unpacking vid funktionsanrop skall antalet element i tuplen match antalet argument funktionen förväntar sig")
print("-" * 80)

"""1. Skapa en funktion som ger oss en slumpmässig punkt i tre dimensioner. Det vill säga (x, y, z)

2. Skapa en funktion som skriver ut en sådan punkt på ett snyggt sätt
3. Skapa en funktion kallad translate som tar en punkt (x, y, z) och en annan tuple med tre värden, vi kan kalla dom (d_x, d_y, d_z) och ger som resultat(returvärde) en ny punkt (x+d_x, y+d_y, z+d_z)




Tänk efter först hur du kan testa att dina funktioner fungerar
Försök lösa problemet med hjälp av tuple unpacking snarare än genom att använda index."""


def random_3d_point(x_min=-10, x_max=10, y_min=-10, y_max=10, z_min=-10, z_max=10):
    x = random.randint(x_min, x_max)
    y = random.randint(y_min, y_max)
    z = random.randint(z_min, z_max)
    return x, y, z


def print_3d_point(p):
    x, y, z = p
    print(f"x:{x}, y:{y}, z:{z}")


print_3d_point(random_3d_point())


def translate(p: tuple, t: tuple) -> tuple:
    x, y, z = p
    dx, dy, dz = t
    return x + dx, y + dy, z + dz


p = (0, 0, 0)
t = (0, 2, 0)
e = (0, 2, 0)

if translate(p, t) == e:
    print("Verkar funka")
else:
    print("Funkar inte")

line()
# _ notation

p = (1, 2, 3, 4, 2, 4, 5)
a, b, *_ = p

# Normalt använder vi _ som variabel när vi inte är intresserade av värdet
# I det här fallet använder vi *_ för att fånga upp resten av tuplen vi inte
# bryr oss om när vi använder en tuple unpack för att hämta de två första värdena
# och spara i a och b
line()

# +

t1 = 1, 2, 3
t2 = 4, 5, 6

t3 = (*t1, *t2)
print(t3)

print(t1 + t2)
# + operatorn kräver att båda sidor är en tuple
line()
# len
# Vi kan använd len för att ta reda på hur många element som finns i en tuple
print(len(t3))
print(len("en text"))
print(len([1, 2, 3, 4]))
line()
# loop
# Eftersom en tuple är en sekvens av saker kan vi iterera över den med hjälp av en for-loop
for e in t3:
    print(e)

# join
t = ("En", "tuple", "med", "strängar")
print(" ".join(t))
# Vi kan använda strängobjektets join för att slå samman till en ny sträng, precis som vi kan med listor

line()


# Strängar och listor beter sig lite lika i det att båda är en sekvens av saker.
# I fallet listor kan den bestå av i stort sett vilken typ av sak som helst
# Medans i strängar så har vi bara bokstäver


# Slicing
# Vi kan använda index för att välja ut ett element ur en lista eller en sträng
l = [1,2,3]
s = "hej"
# första elementet
print(l[0])
print(s[0])
# Sista elementet
print(l[-1])
print(s[-1])
line()

s = "En lite längre textsträng"
l = [1,2,3,4,5,6,7,8,9,10]

# [start: stop]
# Exempel, de fem första elementen
print(s[0:5])
print(l[0:5])
# Vi kan utelämna 0 om vi vill
print(s[:5])
print(l[:5])
#
print(l[2:5])
# [:stop]
print(s[:7])
# Stanna vid det sista elementet, ta inte med det
print(s[:-1])
# [start:]
print(s[5:])
print(l[5:])
line()
# [:]
s[:]
print(id(l))
l2 = l[:] # Ger en kopia av listan l, kalla den l2
print(l)
print(l2)
# Båda listorna, l och l2 innehåller samma element
print(id(l))
print(id(l2))

l2.append(99)
print(l)
print(l2)
line()

# step [start:stop:step
#  positiva steg
# Här går vi igenom listan och stegar två element i taget
print(l[::2])
# Här tar vi fram de jämna elementen genom att börja på det andra elementet och gå två steg i taget
print(l[1::2])
#  negativa steg
print(l[::-1])
# [::-1] reversera
# [-3:] sista tre elementen
print(l[-3:])
# Varför?
print(l[-3]) # Det tredje elementet från slutet
# [-3:] tolkas från tredje elementet och framåt
# [:-3] allt utom de sista tre elementen
print(l[:-3])
