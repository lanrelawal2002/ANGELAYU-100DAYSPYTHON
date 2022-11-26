# my code for the project 11-1-Blackjack
# my to do list
# increase number of 'cards' and remove card from list after selection
# use blackjack not 0
# use user_rerun not game_over

import random
from art import logo

def get_card():
    """selects a random card from the deck of cards"""
    card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    selected_card = random.choice(card_deck)
    return selected_card

def add_up(cards):
    """checks deck of cards and adds up cards accordingly"""
    if 10 in cards and 11 in cards and len(cards) == 2:
        return "Blackjack"
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def verdict(user_score, computer_score):
    """compares user and computer scores"""
    if computer_score == user_score:
        return "It's a draw"
    elif computer_score == "Blackjack":
        return "You lose. Dealer has blackjack"
    elif user_score == "Blackjack":
        return "You win. Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "You win. Dealer went over"
    elif computer_score > user_score:
        return "You lose"
    elif user_score > computer_score:
        return "You win"


def blackjack():
    print(logo)
    user_cards = []
    computer_cards = []

    for number in range(2):
        user_cards.append(get_card())
        computer_cards.append(get_card())


    user_score = add_up(user_cards)
    computer_score = add_up(computer_cards)

    placeholder = True

    while placeholder:
        print(f"player cards: {user_cards}; total {user_score}")
        print(f"computer first hand: {computer_cards[0]}")
        if user_score == "Blackjack" or computer_score == "Blackjack" or user_score > 21:
            # print(f"player cards: {user_cards}; total {sum(user_cards)}")
            # print(f"computer first hand: {computer_cards[0]}")
            # print(f"result sent to cache as \"{user_score}\" for user/\"{computer_score}\" for computer:")
            placeholder = False
        elif user_score < 21:
            # print(f"player cards: {user_cards}; total {sum(user_cards)}")
            # print(f"computer first card: {computer_cards[0]}")
            user_question = input("Do you want to take another card? 'y' or 'n': ")
            if user_question == "y":
                user_cards.append(get_card())
                user_score = add_up(user_cards)
            elif user_question == "n":
                # print(f"user declined and sent to cache:")
                placeholder = False
        

    while computer_score != "Blackjack" and computer_score < 17:
        computer_cards.append(get_card())
        computer_score = add_up(computer_cards)
    
    print(f"player final hand: {user_cards}; final score {user_score}")
    print(f"computer final hand: {computer_cards}; final score: {computer_score}")

    result = verdict(user_score, computer_score)
    print(result)


game_play = True

while game_play:
    request = input(f"Play Blackjack? 'y' or 'n': ")
    if request == "y":
        blackjack()
    elif request == "n":
        game_play = False
    else:
        print("enter either 'y' or 'n'\n")