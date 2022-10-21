# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet():
#     print("Hello. Good morning.")
#     print("How are you doing?")
#     print("Hope you are doing just fine?")


# greet()


# def greet_with_name(name):
#     print(f"Hello {name}.")
#     print(f"How are you today {name}.")


# greet_with_name("Lanre")
# greet_with_name("Barack")


def greet_with(name, location, day):
    print(f"Hello Mr. {name}.")
    print(f"What is it like in {location} city on such a lovely {day}?")

owner = input("Enter name of owner. ")
place = input("Enter location in question. ")
selection = "Monday"
    
greet_with(name = owner, location = place, day = selection)