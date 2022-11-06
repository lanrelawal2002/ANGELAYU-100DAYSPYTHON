# my improvement on Angela's code for the project 10-2-Calculator
# I finally ensured that users either continue, restart, exit or be prompted 
# when they enter random inputs.

# The best version of all three.


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
    
    PROCEED = True

    while PROCEED:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))

        calculator_function = operations[operation_symbol]
        answer = calculator_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # PROCEED = False
        CONTINUE = True

        while CONTINUE:
            user_request = input(f"Type 'c' to continue with {answer},'r' to restart, 'e' to exit: ").lower()
            if user_request == "r":
                CONTINUE = False
                PROCEED = False
                calculator()
            elif user_request == "c":
                num1 = answer
                CONTINUE = False
            elif user_request == "e":
                CONTINUE = False
                PROCEED = False
            else:
                print(f"enter either 'r', 'c', or 'e': ")
                
calculator()

