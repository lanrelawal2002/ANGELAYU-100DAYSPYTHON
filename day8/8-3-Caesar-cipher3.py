def caesar(path, user_message, shift_count):
    if path == "encode":
        cipher_string = ""
        for letter in user_message:
            position = alphabet.index(letter)
            new_position = position + shift_count
            cipher_string += alphabet[new_position]
        print(f"The encoded text is \"{cipher_string}\"")

    elif path == "decode":
        plain_string = ""
        for letter in user_message:
            position = alphabet.index(letter)
            new_position = position - shift_count
            plain_string += alphabet[new_position]
        print(f"The decoded text is \"{plain_string}\"")

    else:
        print(f"...enter either 'encode' or 'decode' to proceed....")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(path=direction, user_message=text, shift_count=shift)