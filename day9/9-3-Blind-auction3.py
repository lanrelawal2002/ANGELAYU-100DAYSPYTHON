# my second code for project 9-3-Blind-auction

def auctioners():
    auction_dictionary = {}

    bid_recall = True

    while bid_recall:
        bidder = input("What is the name of the bidder? ")
        bid_amount = int(input("What is the bid amount? $"))

        auction_dictionary[bidder] = bid_amount

        new_bidder = input("Are there any other bidders? Answer 'yes' or 'no': ")
        if new_bidder == "yes":
            print(f"someone else is bidding\n")
        elif new_bidder == "no":
            bid_recall = False

    return auction_dictionary


def collate(current_dictionary):

    highest_bid = 0

    for bidder in current_dictionary:
        bid_amount = current_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    verdict = f"The winner is {winner} with a bid of ${highest_bid}"
    return verdict
    

working_dictionary = auctioners()
print(working_dictionary)
print(collate(working_dictionary))
