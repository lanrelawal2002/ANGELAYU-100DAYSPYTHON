# part 3 (reorganising our code) of caesar cipher project
# Angela Yu's methods.
# Uncomment the desired method to use it.


# METHOD1 -------ANGELA YU

# def caesar(path, user_message, shift_count):
#     output_string = ""
#     for letter in user_message:
#         position = alphabet.index(letter)
#         if path == "encode":
#             new_position = position + shift_count
#         elif path == "decode":
#             new_position = position - shift_count
#         output_string += alphabet[new_position]
#     print(f"The {path}d text is {output_string}.")

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
# 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
# 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# caesar(path=direction, user_message=text, shift_count=shift)



# METHOD2 ------ANGELA YU
# This method introduced a bug that was fixed by taking the if statement
# out of the for loop.

def caesar(path, user_message, shift_count):
    output_string = ""
    if path == "decode":
            shift_count *= -1
    for letter in user_message:
        position = alphabet.index(letter)
        new_position = position + shift_count
        output_string += alphabet[new_position]
    print(f"The {path}d text is {output_string}.")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(path=direction, user_message=text, shift_count=shift)