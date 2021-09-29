# Detta är en kommentar jag precis lade till

def add(a, b):
    result = a + b
    return result


def subtract(a, b):
    result = a - b
    return result


def multiply(a, b):
    result = a * b
    return result


def divide(a, b):
    result = a / b
    return result

def run():
    print("This program will help with simple calculations. What do you want to do?")
    print("1 - add numbers")
    print("2 - subtract numbers")
    print("3 - multiply numbers")
    print("4 - divide numbers")
    answer = input(">>")
    a = int(input("A="))
    b = int(input("B="))
    if answer == "1":
        result = add(a, b)
    elif answer == "2":
        result = subtract(a, b)
    elif answer == "3":
        result = multiply(a, b)
    else:
        result = ""

    print("Result = " + str(result))


if __name__ == '__main__':
    run()
