from functools import reduce


def line(t=""):
    print(f"{t:-^100}")


# Idag
# Repetition av:
#  Map - Applicera en funktion på varje element i någon samlig
def square(n):
    return n * n


l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Kvadera varje tal

res = []
for i in l:
    res.append(square(i))

print(res)
# Kan förenklas genom att använda map-funktionen

# map(square, l) -> en ny samling bestående av varje element från l
# skickade igenom funktionen square
#
print(list(map(square, l)))


#  Filter
def even(n):
    return n % 2 == 0


# Vill vi har varje jämt tal ur listan res
# Kan vi göra så här

res_even = []
for i in res:
    if even(i):
        res_even.append(i)

print(res_even)

# Vi kan uppnå samma sak med filterfunktionen

print(list(filter(even, res)))
#  Funktioner som objekt


# Nytt för idag
# Reduce
#
# fakultet, skrivs som ex 5!, betyder 5*4*3*2*1
line("Reduce")


def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res = res * i
    return res


print(factorial(5))


# reduce tar två (tre) argument, en funktion som skall ta två argument samt en samlig av något

# en funktion som tar två argument
def mul(a, b):
    return a * b


l2 = [1, 2, 3, 4, 5]

print(reduce(mul, l2))


# ta de två första talen ur listan l2, dvs 1 och 2
# Skicka in i funktionen mul
# mul(1, 2) -> 2
# Skicka in resultatet, 2 och nästa sak ur listan l2, dvs 3 i mul
# mul(2, 3) -> 6
# Skicka in resultatet 6 och nästa sak ur listan l2, dvs 4 i mul
# mul(6, 4) -> 24
# mul(24, 5) -> 120

def add(a, b):
    return a + b


print(reduce(add, l2))
# reduce(add, l2) motsvarar sum(l2)
# reduce börjar applicera funktionen add på de två första elementen ur
# l2, får 3 som resultat
# applicerar add på 3 och nästa element ur l2, och får 6 som resultat
# applicerar add på 6 och nästa element ur l2 och får 10 som resultat
# applicerar add på 10 och sista elementet ur l2 och får 15 som resultat
# [1,2,3,4,5]
# [3,3,4,5]
# [6,4,5]
# [10,5]
# 15
# listan reduceras till ett tal


# Skriv en funktion som tar en lista av boolska värden, [True, False, True]
# och ger True om alla element i listan är True
# Annars False
line("Uppgift 57")
l3 = [True, True, True]
l4 = [True, False, True, True]


# [True, True, True]
# [True, True]
# True

def and_(a, b):
    return a and b


def all_true(l):
    return reduce(and_, l)


print(all_true(l3))
print(all_true(l4))

line("List comprehensions")
# List comprehensions
# Grundläggande
# []

res_squares = [i * i for i in l]
res_squares2 = [square(i) for i in l]
print("Med i*i                ", res_squares)
print("Med anrop till square  ", res_squares2)

print([f"{i} i kvadrat är {i * i:>4}" for i in l])
# Exemplen ovan motsvarar ganska väl vad vi kan göra med map-funktionen
# [square(i) for i in l] motsvarar list(map(square, l)))


# filter då?
# Ta fram alla jämna tal i listan l

print("Jämna tal i listan med list comprehension ", [i for i in l if i % 2 == 0])
print("Jämna tal i listan med filter             ", list(filter(even, l)))

line("Uppgift 58")
import requests

questions = requests.get("https://bjornkjellgren.se/quiz/v2/questions").json()['questions']

all_prompts = [q['prompt'] for q in questions]

all_prompts_gt_500_ans = [q['prompt'] for q in questions if int(q['times_asked']) > 500]
for q in all_prompts_gt_500_ans:
    print(q)

line("Dictionary comprehension")
# Dict comprehensions
squares = {str(i): i * i for i in range(20)}
# På liknande sätt som list comprehension, men eftersom vi skapar en dictionary
# behöver vi ha nyckel och värde. Ex 12:144, vi skriver det som i:i*i i det här fallet
print(squares)
print(squares['12'])

line("Uppgift 59")
import requests

questions = requests.get("https://bjornkjellgren.se/quiz/v2/questions").json()['questions']

all_questions = {int(q['id']): q for q in questions}
print(all_questions[2])
line("Lambda")

# map, filter och reduce vill ha en funktion som argument
# map vill exempelvis har en funktion som ger True eller False tillbaks

# Exempel, reduce som vi såg tidigare för att kontrollera om samtliga element
# i en lista är True
print(reduce(lambda a, b: a and b, [True, True, True, False]))
print(reduce(lambda a, b: a and b, [True, True, True, True]))

min_lambda_func = lambda a, b: a and b

print(type(min_lambda_func))

print(min_lambda_func(True, False))
print(min_lambda_func(True, True))

l5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# kvadrera alla tal i en lista, med hjälp av en en lambda funktion och map
# lambda x: x*x ger oss en anonym funktion som tar ett argument, och ger som resultat kvadraten av argumentet
print(list(map(lambda x: x * x, l5)))

# Använd filter och lambda för att ta fram bara de udda talen i listan l5
print(list(filter(lambda x: x % 2, l5)))

# Kvadrera alla udda tal från 1 till 100
map(lambda x: x*x, filter(lambda x:x % 2, range(1, 101)))


# Vad är summan av kvadraten av alla udda tal från 1-100?
# filter(lambda x:x % 2, range(1, 101)) ger oss alla udda tal mellan 1-100
# lambda x:x % 2 är en funktion som True om talet x inte är jämt delbart på 2

# map(lambda x: x*x, filter(lambda x:x % 2, range(1, 101)))
# använder lambda x: x*x för att kvadrera varje tal i listan av udda tal mellan 1-100

# reduce(lambda a,b: a+b, ...) summerar listan, vi hade lika gärna kunnat använda sum
print(reduce(lambda a,b: a+b, map(lambda x: x*x, filter(lambda x:x % 2, range(1, 101)))))

line("sorted")
l6 = ["Björn", "Ett väldigt långt namn", "Louise", "Carl", "Alma"]

# sorted ger en sorterad kopia
# Vi kan skicka in ett argument key, som är en funktion som låter välja vad vi skall sortera på
# Exempel ned, key=lambda s: len(s) gör att vi sorterar textsträngarna i storleksordning
# istället för bokstavsordning
# För omvänd sorteringsordning använd argumentet reverse=True
print(sorted(l6))
print(sorted(l6, key=lambda s: len(s)))





# sorted
# Funktioner av högre ordning
# rekursiva funktioner
