# Angela's code for the project 11-1-Blackjack
import random
from art import logo

def deal_card():
    """Select a random number from the card list"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Takes a list, checks and returns sum"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw"
    elif computer_score == 0:
        return "You lose. Oppenent has Blackjack"
    elif user_score == 0:
        return "You won. Blackjack"
    elif user_score > 21:
        return "You lose. You went over"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    elif computer_score > user_score:
        return "You lose"

def play_blackjack():
    print(logo)
    user_cards = []
    computer_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_request = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_request == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final card: {computer_cards}, final score: {computer_score}")

    verdict = compare(user_score, computer_score)
    print(verdict)


rerun_checker = True

while rerun_checker:
    Game_on = input("Do you want to play Blackjack? 'y' or 'n': ")
    if Game_on == "y":
        play_blackjack()
    else:
        rerun_checker = False