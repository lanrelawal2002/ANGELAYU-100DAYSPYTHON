# Angela's code for the project 10-2-Calculator

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


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)

    num1 = float(input("What is the first number?: "))

    for symbol in operations:
        print(symbol)

    RERUN_CALCULATOR = True
    while RERUN_CALCULATOR:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))

        calculator_function = operations[operation_symbol]
        answer = calculator_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        user_rerun = input(f"Type 'y' to continue with {answer}, or type 'n' to start over: ").lower()
        if user_rerun == "n":
            RERUN_CALCULATOR = False
            calculator()
        elif user_rerun == 'y':
            num1 = answer
       

calculator()

