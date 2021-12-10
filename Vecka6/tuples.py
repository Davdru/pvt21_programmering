

l = ["hej", "en annan sträng", "a"]
print(l)
print(l[0])  # l[0] Hämtar vi det första elementet i listan

for e in l:
    print(e)

print(len(l))

l.append(2)
l.append(6)

print(l)
l.remove("hej")
print(l)
# En lista kan förändras, vi kan sortera om den, lägga till och ta bort element
# en lista är en ordnad samling element




# En tuple skapas på liknande sätt som en lista, fast istället för hakparanteser [] använder
# vi normala paranteser ()
t = ("hej", "en annan sträng", "a")
# Här skapar vi en tuple kallad t med samma innehåll som listan vi arbetade med tidigare


# Vi kan skriva ut den, hämta ut specifika element med index, precis som med en lista
print(t)
print(t[0])
print(t[-1])
print("-"*80)
for e in t:
    print(e)

# remove() och append() finns inte på en tuple
# En tuple är oföränderlig. när den skapats kan den inte ändras. Den engelska termen för det är
# immutable



# Uppgift 38
# 1. Bygg en funktion som tar en tuppel med två tal som indata, och returnerar dessa i omvänd ordning. T.ex.
#
# t = (5, 6)
# print(swaptuple(t))
#
# .. ska ge följande utskrift:
#
# (6, 5)

def swaptuple(t: tuple) -> tuple:
    return (t[1], t[0])

print(swaptuple((5, 6)))

def swaptuple_reversed(t: tuple) -> tuple:
    return tuple(reversed(t))

print(swaptuple_reversed((5,6)))


# n = (1,2,3,4,5,6)
# for i in n:
#     print(i)
# print("-"*80)
#
# for i in reversed(n):
#     print(i)


# 2. Bygg en funktion som tar in en lista ls, och returnerar en tuple som bygger på listan. T.ex.
#
# print(to_tuple([1, 2, 3]))
#
# ... ska ge:
#
# (1, 2, 3)

def to_tuple(ls: list) -> tuple:
    return tuple(ls) # Vi kan enkelt lösa problemet att skapa en tuple från en lista genom att skicka in listan i tuple()

print(to_tuple([1,2,3]))

# Tuple unpacking

res = ("Björn", "40") # Som i uppgift 39, en funktion har gett en tuple tillbaks med namn och ålder

# Ett sätt är att använda index,
# name = res[0]
# age = res[1]
# Ett alternativ är tuple unpacking
name, age = res
print(name)
print(age)




