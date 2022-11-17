# my code for the project 10-2-Calculator
# I added the 'exponent' and 'floor division' operations.

from art import logo
# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

# Exponent
def exponent(n1, n2):
    return n1 ** n2

# Floor division
def floordiv(n1, n2):
    return n1 // n2




operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": exponent,
    "//": floordiv,
}

def casio():
    print(logo)

    num1 = float(input("What is the first number?: "))

    for symbol in operations:
        print(symbol)

    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What is the next number?: "))

    calculator_function = operations[operation_symbol]
    start_answer = calculator_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {start_answer}")

    # I repeated myself here.....(DRY)
    # But I was able to restart, continue or exit the calculator.
    RERUN_CALCULATOR = True

    while RERUN_CALCULATOR:
        user_rerun = input(f"Type 'y' to continue with {start_answer}, 'r' to restart the calculator, 'e' to exit the calcultor: ")
        if user_rerun == "r":
            RERUN_CALCULATOR = False
            casio()
        elif user_rerun == 'y':
            operation_symbol = input("Pick an operation: ")
            num3 = float(input("What is the next number?: "))

            calculator_function = operations[operation_symbol]
            end_answer = calculator_function(start_answer, num3)
            print(f"{start_answer} {operation_symbol} {num3} = {end_answer}")
            start_answer = end_answer
        elif user_rerun == "e":
            print(f".......\nEXITING CALCULATOR")
            RERUN_CALCULATOR = False
        else:
            print(f"\nPlease enter either 'y', 'r' or 'e'\n")

casio()
print(f"Goodbye!!!")