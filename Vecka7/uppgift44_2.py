"""2. Bygg ett program där användaren matar in ett gäng heltal med komma emellan, och skriver ut följande:
Ange tal med komma emellan: 1,2,3,5,100
Första talet: 1
Sista talet: 100
Summan av talen: 111
Talen baklänges: 100, 5, 3, 2, 1

Tips: Använd slicing och inbyggda funktionen sum().
Tips 2: Det går att lösa "Talen baklänges" på två sätt: det lätta sättet
är med inbyggda funktionen reverse(). Det svåra sättet är med slicing syntax!
Pröva båda :)"""


def get_list_of_numbers() -> list[int]:
    nums = input(">").split(",")
    return list(map(int, nums))


def print_reversed(l: list[int]):
    print(f"Talen baklängses {l[::-1]}")


def main():
    nums = get_list_of_numbers()

    print(f"Första talet: {nums[0]}")
    print(f"Sista talet: {nums[-1]}")

    print(f"Summan av talen: {sum(nums)}")
    print_reversed(nums)

    print(f"orginallistan {nums}")



if __name__ == '__main__':
    main()
