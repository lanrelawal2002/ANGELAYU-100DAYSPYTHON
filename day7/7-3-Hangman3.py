import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(f"The chosen word is \"{chosen_word}\"")

display = []

for _ in range(word_length):
    display += "_"

while "_" in display:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        if chosen_word[position] == guess:
            display[position] = guess
            
    print(display)

    if "_" not in display:
        print("You win.")