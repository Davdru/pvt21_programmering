def read_regno() -> str:
    return input("regno>")


def print_regno(regno: tuple[str, str]):
    letters, numbers = regno
    print(f"Bokstavsgrupp: {letters}")
    print(f"Siffergrupp: {numbers}")


def split_regno(regno: str) -> tuple[str, str]:
    return regno[:3], regno[3:]


def main():
    regno = read_regno()
    s_regno = split_regno(regno)
    print_regno(s_regno)


if __name__ == '__main__':
    main()
