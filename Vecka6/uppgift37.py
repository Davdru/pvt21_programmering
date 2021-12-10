


def read_name_age():
    name = input("Namn?>")
    age = input("Ålder?>")

    print_name_age(age, name)


def print_name_age(age, name):
    print(f"{name} är {age} år gammal")


if __name__ == '__main__':
    read_name_age()