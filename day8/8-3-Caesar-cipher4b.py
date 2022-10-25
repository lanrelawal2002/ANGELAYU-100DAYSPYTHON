# This is caesar cipher 4 using method 1 of caesar cipher 3
# i.e where there is an if elif statement in the function.

# I also enforced the use of only 'encode' or 'decode' as direction 
# in order to use to cipher.

from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(path, user_message, shift_count):
    if path == "encode" or path == "decode":
        output_string = ""
        for char in user_message:
            if char in alphabet:
                position = alphabet.index(char)
                if path == "encode":
                    new_position = position + shift_count
                    output_string += alphabet[new_position]
                elif path == "decode":
                    new_position = position - shift_count
                    output_string += alphabet[new_position]
            else:
                output_string += char
        print(f"The {path}d text is '{output_string}'.\n")
    else:
        print(f"You have to enter either \"encode\" or \"decode\"\n")





def cipher_start():
    print(logo)
    print(f"bluegate edition\nversion 2.0.2\n")
    CONTINUE_CIPHERING = False

    while not CONTINUE_CIPHERING:
        print(f"------")
        print(f"----------------")
        print(f"----------------------------")
        print(f"cipher loading...\n5% done\n25% done\n80% done\n100% loaded\n\nCipher up and running\n")
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        if shift > 26:
            new_shift = shift % 26
            shift = new_shift

        caesar(path=direction, user_message=text, shift_count=shift)

        restart_cipher = input("Type 'yes' to continue or 'no' to end.\n").lower()
        
        if restart_cipher == "no":
            CONTINUE_CIPHERING = True
        elif restart_cipher == "yes":
            print("\n")

    print("\n")
    print("Ciphering Ended.....\nRERUN CODE TO START ALL OVER!!!!.")

cipher_start()

