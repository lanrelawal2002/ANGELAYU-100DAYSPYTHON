import random


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


End_of_selection = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

print(f"The chosen word is \"{chosen_word}\"")

display = []

for _ in range(word_length):
    display += "_"

Guess_checker = False

while not End_of_selection:
    
    all_guesses = ""

    guess = input("Guess a letter: ").lower()
    
    for character in guess:
        all_guesses += character

    while Guess_checker:
        if guess in all_guesses:
            print("You have guessed that letter already.\nPlease guess a different letter.")
            Guess_checker = False
    # while not Repitition_check:   

        
        # for character in guess:
        #     all_guesses += character

        # if guess in all_guesses:
        #     print("You have guessed that letter already.\n Please guess another letter.")
        # else:
        #     Repitition_check = True

    for position in range(word_length):
        if chosen_word[position] == guess:
            display[position] = guess
    

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            End_of_selection = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        End_of_selection = True
        print("You win.")

    print(stages[lives])
    Guess_checker = True