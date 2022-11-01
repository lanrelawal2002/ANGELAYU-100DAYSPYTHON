#Password Generator Project
from multiprocessing.sharedctypes import Value
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '@', '^', '*', '+']

print("Welcome to the PyPassword Generator!")
n_letters = int(input("How many letters would you like in your password?\n"))
n_symbols = int(input("How many symbols would you like?\n"))
n_numbers = int(input("How many numbers would you like?\n"))

letters_length = len(letters)
symbols_length = len(symbols)
numbers_length = len(numbers)

value = []

for char in range(1, n_letters + 1):
    choice = random.randint(0, letters_length - 1)
    value += letters[choice]
    #print(value)

for char in range(1, n_symbols + 1):
    choice = random.randint(0, symbols_length - 1)
    value += symbols[choice]
    #print(value)

for char in range(1, n_numbers + 1):
    choice = random.randint(0, numbers_length - 1)
    value.append(numbers[choice])
    #print(value)

print("\n")
print("Please wait.....\n")
print("Your password is been generated\n")
print(value)
random.shuffle(value)
print(value)

password = ""
for item in value:
    password += item

password_length = len(password)
print(f"Your password is:  {password}  and is '{password_length}' characters long.\n")