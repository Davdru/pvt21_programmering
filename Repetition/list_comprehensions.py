
l = [1, 2, 4, 6, 5, 1]

squares = []
for x in l:
    squares.append(x*x)

print(l)
print(squares)

def square(n):
    return n*n

#            | Detta uttryck är det som kommer bli ett element i den nya listan
#            V
squares2 = [x*x for x in l]
squares3 = [square(x) for x in l]

print(squares2)
print(squares3)
square_of_even_numbers = []



for x in range(1, 21):
    if x % 2 == 0:
        square_of_even_numbers.append(x*x)


square_of_even_numbers2 = [x*x for x in range(1, 21) if x % 2 == 0]
print(square_of_even_numbers)
print(square_of_even_numbers2)


names = ["Björn", "Louise", "Carl", "Alma"]
ages = [41, 39, 5, 2]


name_dict = {}
for i in range(len(names)):
    name_dict[names[i]] = ages[i]


print(name_dict["Björn"])
print(name_dict["Louise"])

print(name_dict)
print({name:age for name, age in zip(names, ages)})

for v in zip(names, ages):
    print(v)

# zip tar två samlingar av saker och ger en ny samling med par av element



print({x:x*x for x in range(10)})

