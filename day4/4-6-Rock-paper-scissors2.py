import random

# This is my ROCK PAPER AND SCISSORS secondCODE written. 
# 'less than zero or greater or equal to 3' condition now met plus python list used.

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

image_rep = [rock, paper, scissors]

player1_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player1_choice < 0 or player1_choice >= 3:
    print("PLEASE SELECT EITHER 0, 1 or 3.")
else:
    print(image_rep[player1_choice])

    print("Computer chose:")

    computer_choice = random.randint(0, 2)

    print(image_rep[computer_choice])

    if player1_choice == computer_choice:
        print("It's a draw.")

    if player1_choice == 0 and computer_choice == 1:
        print("You lose.")
    elif player1_choice == 0 and computer_choice == 2:
        print("You win!")

    if player1_choice == 1 and computer_choice == 0:
        print("You win!")
    elif player1_choice == 1 and computer_choice == 2:
        print("You lose.")

    if player1_choice == 2 and computer_choice == 0:
        print("You lose.")
    elif player1_choice == 2 and computer_choice == 1:
        print("You win!")