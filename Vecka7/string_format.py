
#
name = "Björn"
age = 40
number = 10/3
number_text = str(number).split('.')[0] + "." + str(number).split('.')[1][:2]
print("Hej", name, "du är", age, "år, 10/3 är ungefär", number_text)

greeting = "Hej " + name + " du är " + str(age) + " år, 10/3 är ungefär " + str(number_text)

print(greeting)

print(f"Hej {name} du är {age} år, 10/3 är ungefär {number:.2f}")


# Äldre sätt att göra strängformatering %
print("Hej %s du är %d år gammal, 10/3 är ungefär %.2f" % (name, age, number))


t = (name, age, number)

# Betydligt nyare är {} som placeholder och format metoden
print("Hej {} du är {} år, 10/3 är ungefär {:.2f}".format(name, age, number))



t = (1,5,6,7,23,19,99)



def find_max(t):
    if not isinstance(t, tuple):
        raise TypeError(f"Unsupported type {t.__class__}")
    if not len(t):
        raise ValueError("No max value of empty tuple")
    m = 0
    for e in t:
        if e > m:
            m = e
    return m


print(find_max(t))
