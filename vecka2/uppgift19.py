import json

PHONEBOOK = "phonebook2.json"


def load_phonebook():
    try:
        with open(PHONEBOOK) as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save_phonebook(pb):
    with open(PHONEBOOK, "w") as f:
        json.dump(pb, f)


def print_menu():
    print("[1] List numbers")
    print("[2] Add number")
    print("[3] Delete number")


def get_new_entry():
    print("New entry")
    name = input("Name>")
    number = input("Number>")
    return name, number


def main():
    phonebook = load_phonebook()

    while True:
        print_menu()
        v = input(">")
        if v == "1":
            print_phonebook(phonebook)
        elif v == "2":
            add_phonebook_entry(phonebook)
        elif v == "3":
            del_phonebook_entry(phonebook)
        else:
            break


def del_phonebook_entry(phonebook):
    name = input("Name to delete>")
    try:
        del phonebook[name]
        save_phonebook(phonebook)
    except KeyError:
        print(f"Entry {name} not found")


def add_phonebook_entry(phonebook):
    name, number = get_new_entry()
    phonebook[name] = number
    save_phonebook(phonebook)


def print_phonebook(phonebook):
    for p in phonebook:
        print(f"{p}: {phonebook[p]}")
    print("-" * 40)


if __name__ == '__main__':
    main()
