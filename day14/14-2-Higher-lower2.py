# my second version of the higher lower project
# I used five(5) functions
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


def dictionary_creator(current_list):
    """Function to select two distinct dictionaries from current list"""
    dictionary_list = []

    first_number = current_list[0]
    second_number = current_list[1]

    first_dictionary = data[first_number]
    second_dictionary = data[second_number]

    for value in range(1):
        dictionary_list.append(first_dictionary)
        dictionary_list.append(second_dictionary)

    return dictionary_list


def reversing_dict(second_dictionary):
    """Function to create new second_dictionary"""

    redundant_counter = 0

    tracker = True
    
    while tracker:
        new_index = random.randint(0, end_range)
        placeholder_index = data.index(second_dictionary)
        if new_index == placeholder_index:
            redundant_counter += 2
        else:
            regenerated_second_dictionary = data[new_index]
            tracker = False


    return regenerated_second_dictionary            


def choice_compute(working_dict_list):
    """Function to check and process user choice based on selected dictionaries"""
    user_score = 0

    first_dictionary = working_dict_list[0]
    second_dictionary = working_dict_list[1]


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
            new_second_dictionary = reversing_dict(second_dictionary)
            second_dictionary = new_second_dictionary
        elif choice == "B" and second_dictionary['follower_count'] > first_dictionary['follower_count']:
            user_score += 1
            print(f"\nYou are right. Current score: {user_score}")
            first_dictionary = second_dictionary
            new_second_dictionary = reversing_dict(second_dictionary)
            second_dictionary = new_second_dictionary
        else:
            return f"\nSorry, that's wrong. Final score:  {user_score}\n"

end_range = len(data) - 1

def game_play():
    current_list = index_selector()

    working_dict_list = dictionary_creator(current_list)

    result = choice_compute(working_dict_list)
    print(result)


start_game = True
while start_game:
    player_run = input("\nDo you want to play HIGHER LOWER? 'yes' or 'no': ")
    if player_run == "yes":
        game_play()
    elif player_run == "no":
        start_game = False
    else:
        print("\nenter either 'yes' or 'no'")