# My code for the project 9-3-Blind-auction

# from replit import clear -- this if for the sake of replit
from art import logo
print(logo)
auction_dictionary = {}

def start_event():
    bid_recall = True

    while bid_recall:
        bidder_name = input("What is your name?: ")
        bid = int(input("What is your bid?: $"))
        auction_dictionary[bidder_name] = bid
        
        repeat_auction = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
        if repeat_auction == "yes":
            print("\nsomeone else is bidding....\n")
            # clear() -- this is for sake of replit

        elif repeat_auction == "no":
            bid_recall = False
    print(auction_dictionary)
    
def blind_auction():
    all_bids = []
    for bidder in auction_dictionary:
        bid_amount = auction_dictionary[bidder]
        all_bids.append(bid_amount)
    
    highest_bid = max(all_bids)
    

    for bidder in auction_dictionary:
        individual_bid = auction_dictionary[bidder]
        if highest_bid == individual_bid:
            winner_name = bidder

    print(f"The winner is {winner_name} with a bid of ${highest_bid}.")

start_event()
blind_auction()