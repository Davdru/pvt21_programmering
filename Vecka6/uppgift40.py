

def read_name_age() -> tuple:
    name = input("Namn?>")
    age = input("Ålder?>")
    return name, age


def greeting(name, age):
    return f"{name} är {age} år gammal"


def main():
    name, age = read_name_age()
    print(greeting(name, age))


if __name__ == '__main__':
    main()
