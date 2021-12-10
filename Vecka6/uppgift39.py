

def read_name_age() -> tuple:
    name = input("Namn?>")
    age = input("Ålder?>")
    return name, age


def print_name_age(name, age):
    print(f"{name} är {age} år gammal")


name, age = read_name_age()


print_name_age(name, age)
