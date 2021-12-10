

class Person:
    name: str
    last_name: str
    age: int

    def __init__(self, name: str, last_name: str, age: int):
        self.name = name
        self.last_name = last_name
        self.age = age

    def greet(self):
        print(f"{self.name} är {self.age} år gammal")


def read_person() -> Person:
    name = input("Namn?>")
    l_name = input("Efternamn?>")
    age = int(input("Ålder?>"))
    return Person(name, l_name, age)


def greet_person(person: Person) -> str:
    return f"{person.name} är {person.age} år gammal"


def main():
    p = read_person()
    p.greet()
    
    #print(greet_person(p))


if __name__ == '__main__':
    main()
