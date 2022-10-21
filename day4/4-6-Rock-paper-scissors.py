import random

# This is my ROCK PAPER AND SCISSORS first CODE written. 
# 'less than zero or greater or equal to 3' condition not met plus python list not used.

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


player1_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player1_choice == 0:
    print(rock)
elif player1_choice == 1:
    print(paper)
elif player1_choice == 2:
    print(scissors)
else:
    print("Please enter either 0, 1 or 2. \n")

print("Computer chose:")

computer_choice = random.randint(0, 2)

if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)

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