def encrypt(plain_text, shift_number):
    text_index_in_alpha = []
    text_index_with_shift = []
    encoded_string = ""

    for letter in plain_text:
        value = alphabet.index(letter)
        text_index_in_alpha.append(value)
    #print(text_index_in_alpha)

    for number in text_index_in_alpha:
        number += shift_number
        text_index_with_shift.append(number)
    #print(text_index_with_shift)
    
    for digit in text_index_with_shift:
        cipher_letter = alphabet[digit]
        encoded_string += cipher_letter

    print(f"The encoded text is {encoded_string}.")
    

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
    encrypt(plain_text=text, shift_number=shift)
elif direction == "decode":
    decrypt(encrypted_text=text, shift_number=shift)
else:
    print(f"...enter either 'encode' or 'decode' to proceed....")