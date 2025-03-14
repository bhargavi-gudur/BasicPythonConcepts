import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


a = int(input("enter the number a: "))
b = int(input("enter the number b : "))


def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def mul(a, b):
    return a*b


def div(a, b):
    if b != 0:
        return a/b

    else:
        return "division by zero is not allowed ."


symbol = {"+": add, "-": sub, "*": mul, "/": div}

while True:
    clear_screen()  # Clears screen at the start of every loop iteration
    print("Available operations: +, -, *, /")
    operation = input("Enter the operation (or 'exit' to quit): ")

    if operation == 'exit':
        print("Exiting the program. Goodbye!")
        break

    if operation in symbol:
        result = symbol[operation](a, b)
        print(f"The result of {a} {operation} {b} is: {result}")
    else:
        print("Invalid operation. Please try again.")

    print("\n")
