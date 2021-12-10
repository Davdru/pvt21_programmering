

# 25.1 Skriv en funktion som vänder en text baklänges
def reverse(text: str) -> str:
    count = 1
    ny_lista = []
    for i in range(0, len(text)):
        ny_lista.append(text[len(text) - count])
        count += 1
    return "".join(ny_lista)


def reverse2(text: str) -> str:
    res = []
    for c in text:
        res.insert(0, c)
    return "".join(res)




# 25.2 Skriv en funktion som tar in en textsträng och returnerar antalet stora bokstäver i strängen.
# Lösning 1. Använd strängars inbyggda isupper()
def num_uppercase(text: str) -> int:
    res = 0
    for c in text: #  för varje tecken c i strängen text
        if c.isupper():
            res += 1
    return res


def num_uppercase2(text: str) -> int:
    return len([c for c in text if c.isupper()])


def test_reverse():
    assert reverse("hej") == "jeh"
    print(reverse("En text som skall vändas"))
    print(reverse2("En text som skall vändas"))


if __name__ == '__main__':
    # test_reverse()
    teststr = "test test"

    assert num_uppercase(teststr) == 0
    assert num_uppercase(teststr.upper()) == 8

    assert num_uppercase2(teststr) == 0
    assert num_uppercase2(teststr.upper()) == 8