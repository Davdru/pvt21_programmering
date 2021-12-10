

def foo():
    print("foo")
    return 42


a = foo()
print(a)

f = foo

print(f"variabeln f är {f}")
print("#"*80)
print(f"Nu kör vi funktionen som f pekar på och får värdet {f()}")




def cube(n):
    return n**3

print(cube(3))
print("-"*80)
print("Med list comprehension")
print([cube(x) for x in range(10)])
print("Med map och namngiven funktion (cube)")
print(list(map(cube, range(10))))
print("Med map och lambda (anonym funktion)")
print(list(map(lambda x: x**3, range(10))))
