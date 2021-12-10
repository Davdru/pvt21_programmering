print("Hello World!")  # Kalla på funktionen print med argumentet "Hello World"


# print <- funktionens namn
# Inom paranteserna ("Hello World!") anger vi funktionens argument, i det här fallet en textsträng "Hello World!"
# Vi kan se funktionen som en maskin, vi stoppar in någonting i den och så händer
# någonting, t.ex. att vi får tillbaks ett värde eller att någonting skrivs ut
# i terminalen, eller någonting annat, t.ex läser in data från terminalen eller en fil etc.
#
# Begreppet kommer från matematiken, där är en funktion någonting som tar ett värde som
# som argument och ger tillbaks ett annat värde
# Ett exempel på det skulle kunna vara funktionen som kvadrerar tal.
# Vi kan kalla den för f(x) = x^2
# Om vi stoppar in värdet två så kommer 4 ut, 3 -> 9 etc.
# f(2) = 2^2 eller 2*2 -> 4
# f(3) = 3^2 eller 3*3 -> 9
#
# Om vi tar f(x) = x^2 som exempel
# f är funktionens namn
# (x) säger att funktionen tar ett argument, kallat x
# = x^2 säger att funktionen tar argumentet x och kvadrerar det.
# Översätter vi detta till python-kod får vi något sådant här:

def f(x):
    return x * x

# def betyder i python att här kommer en ny funktions/metod-definition
# När python ser en sådan här definition skapas ett nytt funktionsobjekt
# som sparas i minnet under namnet f i det här fallet.
# return x * x talar om vad funktionen får för värde
# Om vi t.ex. stoppar in 5 som argumentet x kommer funktionen ge 25 tillbaks


f(10)
# Koden ovan kommer kalla på funktionen f, med värdet 10 som enda argument
# Python kommer ta värdet 10, ett heltal och stoppa in i funktionen f
# där kommer sedan 10 multipliceras med 10 och lämnas tillbaks som returvärde
# I det här fallet gör vi ingenting med returvärdet (100),
# vi bara anropar funktionen men sparar inte dess returvärde någonstans


a = f(11)
# Här anropar vi funktionen f med argumentet 11
# Det värde vi får tillbaks från funktionen 121, sparar vi i en variabel a

# I exemplet f har vi inte talat om vilken typ argumentet x har
# Ingenting hindrar oss att stoppa in ett konstigt värde, t.ex textsträng
# f("Hejsan")
# Betyder att funktionen f försöker göra multiplikation mellan två textsträngar
# "Hejsan" * "Hejsan"
# Python vet inte hur man gör det och programmet avbryts med ett fel
# I andra fall kan det fungera bättre, t.ex med komplexa tal eller flyttal
b = f(1.1)
c = f(5+2j)

# I python eller andra programspråk behöver inte funktioner ta något värde
# Exempel
def g():
    return 42

d = g()

# Vi kan också ha funktioner som tar flera argument
# Ett exempel:

def multiply(a, b):
    return a * b

# Funktionen har namnet multiply
# tar två argument a och b
# ger tillbaks produkten av a och b

e = multiply(10, 5)

# Än så länge har vi bara slängt bort returvärdet från funktionsanropen eller
# sparat det i variabler
# Vi kan också använda returvärdet från en funktion som argument i en annan funktion
# Exempel

print(f(7))
# Vi stoppar in 7 i funktionen f som då ger 49 som returvärde
# Detta 49 stoppar vi sedan in som argument till funktionen print som skriver ut det till terminalen
print(
    multiply(11, 3)
)

print(multiply(2, f(3)))
# Först kommer f(3) räknas ut, blir 9
# Därefter kommer multiply anropas med argumenten 2 och 9 (9 var returvärdet från f(3)
# sist kommer funktionen print anropas med argumentet 18, dvs returvärdet från multiply




# En funktion kan ha flera retur-statements. Så fort en returstatement nås avslutas funktionen
# Exempel, funktionen odd som talar om ifall ett tal är udda, d.v.s. 3 som argument skall ge True
# 4 som argument skall ge False
# Vi skriver funktionen lite onödigt lång för att illustrera multipla returstatements

def odd(n):
    if n % 2 == 0:
        return False
    else:
        return True

# Så fort vi hamnar på en return så avslutas funktionsanropet och lämnar tillbaks det värde som
# står efter return

print(odd(3))
print(odd(4))

# Vi kan förenkla många funktioner som ger True eller False tillbaks
# Even skall ge True om talen n är jämt, dvs delbart på 2, annars False
def even(n):
    return n % 2 == 0
# n % 2 == 0 kommer vara True om divisionsresten av n / 2 är 0, annars False
# Vilket är precis det beteende vi ville ha från funktionen

print(f"even(2): {even(2)}")
print(f"even(3): {even(3)}")


def odd2(n):
    return not even(n)
# not ger motsatsen. så not True -> False
# not False -> True
# Här nyttjar vi det faktum att even gör i princip det vi vill att odd skall göra, fast tvärtom

print(f"odd2(2): {odd2(2)}")
print(f"odd2(3): {odd2(3)}")



# Argument till funktioner
# Exempel från kursen, vi vill ha en funktion som frågar användaren efter ett tal mellan
# 1 och n, så har vi exempelvis 3 svarsalternativ vill vi ha ett tal mellan 1 och 3
# Vi vill också skriva ut en prompt som ger en ledtråd till vad användaren skall göra

def get_number(n, prompt="Ge mig ett tal:"):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
# Funktionen kan byggas ut så att den bara accepterar ett tal mellan 1 och n

# Argument/parametrar med ett defaultvärde skall komma efter argument/parametrar
# utan defaultvärden i funktionens argumentlista


# print(get_number(5))
# print(get_number(3, "[1-3]"))



# Rekursiva funktioner
# En rekursiv funktion är en funktion som anropar sig själv
# Viktigt är at vi har något sätt att få stopp på rekursionen
#
# def foo():
#     print("Hello!")
#     foo()
# foo()
# Den här koden kommer resultera i ett Exception, RecursionError.
# Det finns inget slut på rekursionen

# Fakultetsfunktionen är ett enkelt exempel på en rekursiv funktion
# fakultet 5 eller 5!
# 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4!
# 4! = 4 * 3!
# 3! = 3 * 2!
# 2! = 2 * 1!
# 1! = 1 * 0!
# 0! = 1

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))


# Quicksort, sorterar en lista
# Välj ett tal ur listan, kallat pivot-talet, sortera alla tal som är mindre än eller lika med pivot
# och placera dem till vänster om pivot
# sortera alla tal som är större än pivot och lägg dom till höger om pivot

def quicksort(l):
    if len(l) == 0:
        return l
    pivot = l.pop(0) # Plocka ut det första elementet ur listan och använd som pivotvärde
    left_hand_side = quicksort(list([x for x in l if x <= pivot]))
    right_hand_side = quicksort(list([x for x in l if x > pivot]))
    return left_hand_side + [pivot] + right_hand_side




print(quicksort([235,23,5,6,1,99]))


