
def encrypt(user_message, shift_count):
    cipher_string = ""
    for letter in user_message:
        position = alphabet.index(letter)
        new_position = position + shift_count
        cipher_letter = alphabet[new_position]
        cipher_string += cipher_letter

    print(f"The encoded text is {cipher_string}.")


def decrypt(encrypted_text, shift_number):
    decoded_string = ""
    for letter in encrypted_text:
        position = alphabet.index(letter)
        new_position = position - shift_number
        decoded_letter = alphabet[new_position]
        decoded_string += decoded_letter
    print(f"The decoded text is {decoded_string}.")
    


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


if direction == "encode":
    encrypt(user_message=text, shift_count=shift)
elif direction == "decode":
    decrypt(encrypted_text=text, shift_number=shift)
else:
    print(f"...enter either 'encode' or 'decode' to proceed....")