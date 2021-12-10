# 15.1 Implementera ett program som räknar ord och bokstäver i en text
# 15.2 Ta in en godtycklig text (testa att copy-paste från lorumipsum.com)
#       och skriv ut hur många vokaler som finns i strängen. Tips: "a" in "abcd" är True!
# 15.3 Göteborgsvarvet, vilken placering kom XYZ på? Implementera resten av detta program:
# runners_in_order = “Lisa Lasse Louise Leopold Lova Love Lennart Lena Lisette Linus”.split()
# vem = input(“Ange löpare du söker placering för”)


text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor 
in reprehenderit in voluptate velit esse cillum dolore eu 
fugiat nulla pariatur. Excepteur sint occaecat cupidatat non 
proident, sunt in culpa qui officia deserunt mollit anim 
id est laborum."""
test_text = "Detta Är, en   sträng£"
VOWELS = 'aeiouyåäö'


def count_vowels(t: str) -> int:
    i = 0
    for letter in t:
        if letter.lower() in VOWELS:
            i += 1
    return i


def count_letters(t):
    i = 0
    for letter in t:
        if letter.isalpha():
            i += 1
    return i


def count_words(t):
    return len(t.split())


def main():
    # Vi skall kunna skriva in ett namn och programmet skall svara med
    # personens plats i loppet.
    # List -> 1, Love -> 6
    runners_in_order = "Lisa Lasse Louise Leopold Lova Love Lennart Lena Lisette Linus".split()
    vem = input("Ange löpare du söker placering för")
    i = 1
    found = False
    for runner in runners_in_order:
        if runner == vem:
            print(f"{runner} kom på plats {i}")
            found = True
        i += 1
    if not found:
        print(f"{vem} deltog inte")


def find_runner():
    runners_in_order = "Lisa Lasse Louise Leopold Lova Love Lennart Lena Lisette Linus".split()
    vem = input("Ange löpare du söker placering för>").strip().title()

    try:
        print(f"{vem} kom på plats {runners_in_order.index(vem) + 1}")
    except ValueError:
        print(f"{vem} deltog inte i tävlingen")


if __name__ == '__main__':
    # print(count_letters(text))
    # print(count_words(text))
    # print(count_vowels(test_text))
    # main()
    find_runner()
