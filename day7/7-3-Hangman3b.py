import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f"The chosen word is \"{chosen_word}\"")

display = []
word_length = len(chosen_word)

for _ in range(word_length):
    display += "_"

End_of_selection = False

while not End_of_selection:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        if chosen_word[position] == guess:
            display[position] = guess

    print(display)

    if "_" not in display:
        End_of_selection = True
        print("You win.")