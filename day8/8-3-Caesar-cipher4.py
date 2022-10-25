# This is caesar cipher 4 using method 2 of caesar cipher 3
# i.e where the single if statement is outside the for loop

from art import logo

def caesar(path, user_message, shift_count):
    output_string = ""
    if path == "decode":
            shift_count *= -1
    for char in user_message:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_count
            output_string += alphabet[new_position]
        else:
            output_string += char
    print(f"The {path}d text is '{output_string}'.")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

RERUN_CIPHER = True

while RERUN_CIPHER:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > 26:
        new_shift = shift % 26
        shift = new_shift

    caesar(path=direction, user_message=text, shift_count=shift)

    rerun_check = input(f"Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    
    if rerun_check == "no":
        RERUN_CIPHER = False

print("Thanks for playing.")