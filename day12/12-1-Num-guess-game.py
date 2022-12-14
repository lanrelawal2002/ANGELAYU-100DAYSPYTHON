# my first code for the number guessing game project
# I used only one function and one global variable

import random
from art import logo

def player_trials():
    """Function to check level and compute number guessed"""
    level_confirm = True

    while level_confirm:
        level = input(f"Choose a difficulty level. 'easy' or 'hard': ")
    
        if level == "hard":
            total_attempts = 5
            level_confirm = False
        elif level == "easy":
            total_attempts = 10
            level_confirm = False
        else:
            print("\nenter either 'easy' or 'hard' to continue....\n")


    print(f"\nYou have {total_attempts} attempts remaining.")
    
    check_input = True

    while check_input:
        player_guess = int(input("Guess the number: "))
        
        if player_guess == original_number:
            return f"\nYou got it. The number was {original_number}"
        elif player_guess > original_number:
            total_attempts -= 1
            if total_attempts == 0:
                print("Too high.")
                return f"\nYou have run out of guesses. GAME OVER!!!\nThe number was {original_number}"

            print(f"\nToo high.\nTake another guess.")
            print(f"You have {total_attempts} attempts remaining.\n")
        elif player_guess < original_number:
            total_attempts -= 1
            if total_attempts == 0:
                print("Too low.")
                return f"\nYou have run out of guesses. GAME OVER!!!\nThe number was {original_number}"
            
            print(f"\nToo low.\nTake another guess.")
            print(f"You have {total_attempts} attempts remaining.\n")
        


    
print(logo)
print(f"Welcome to the number guessing game!!!")
print(f"Guess a number between 1 and 100.")

original_number = random.randint(2, 99)
print(original_number)

final_verdict = player_trials()
print(final_verdict)

