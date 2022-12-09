# my first version of the higher lower project
# I used four(4) functions

import random
from game_data import data
from art import logo, vs

def index_selector():
    """Function to generate a list containing two distinct numbers"""
    two_digit_list = []
    duplicate_check = True

    while duplicate_check:
        for value in range(2):
            index_number = random.randint(0, end_range)
            two_digit_list.append(index_number)
        
        first_digit = two_digit_list[0]
        second_digit = two_digit_list[1]

        if first_digit == second_digit:
            two_digit_list.clear()
        else:
            duplicate_check = False      

    return two_digit_list


def reverse_second_dictionary(second_dictionary):
    repeat_check = True
    redundancy_counter = 0

    while repeat_check:
        new_index = random.randint(0, end_range)
        placeholder_index = data.index(second_dictionary)
        if new_index == placeholder_index:
            redundancy_counter += 1
        else:
            new_second_dictionary = data[new_index]
            repeat_check = False

    return new_second_dictionary


def compute(first_dictionary, second_dictionary):
    """Function to check and process user choice"""
    user_score = 0

    correct_count = True

    while correct_count:
        print(logo)
        print(f"\nCompare A: {first_dictionary['name']}, a {first_dictionary['description']}, from {first_dictionary['country']}")
        print(vs)
        print(f"Against B: {second_dictionary['name']}, a {second_dictionary['description']}, from {second_dictionary['country']}\n")

        choice = input("Who has more followers? Choose 'A' or 'B': ")
        if choice == "A" and first_dictionary['follower_count'] > second_dictionary['follower_count']:
            user_score += 1
            print(f"\nYou are right. Current score: {user_score}")
            first_dictionary = second_dictionary
            switched_second_dictionary = reverse_second_dictionary(second_dictionary)
            second_dictionary = switched_second_dictionary
        elif choice == "B" and second_dictionary['follower_count'] > first_dictionary['follower_count']:
            user_score += 1
            print(f"\nYou are right. Current score: {user_score}")
            first_dictionary = second_dictionary
            switched_second_dictionary = reverse_second_dictionary(second_dictionary)
            second_dictionary = switched_second_dictionary
        else:
            print(logo)
            return f"\nSorry, that's wrong. Final score:  {user_score}\n"


end_range = len(data) - 1

def game_play():
    current_list = index_selector()

    first_number = current_list[0]
    second_number = current_list[1]

    first_dictionary = data[first_number]
    second_dictionary = data[second_number]

    result = compute(first_dictionary, second_dictionary)
    print(result)


start_game = True

while start_game:
    play_now = input("\nDo you want to play HIGHER LOWER GAME? 'yes' or 'no': ")
    if play_now == "yes":
        game_play()
    elif play_now == "no":
        start_game = False
    else: 
        print("\nenter 'yes' or 'no'")