from pwstrength import compute_strength


def main():
    pw = input(">")
    print(f"Password strength {compute_strength(pw)}")


if __name__ == '__main__':
    main()
