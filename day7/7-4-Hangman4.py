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



while not End_of_selection:
    guess = input("Guess a letter: ").lower()
    
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
   