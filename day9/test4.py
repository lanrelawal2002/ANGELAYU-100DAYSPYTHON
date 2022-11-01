# all_bids = [55, 12, 9, 16, 0, 136, 3, 14, 8, 74]
# print(all_bids)
# highest_bid = max(all_bids)
# print(highest_bid)

# from typing import Counter


# attempts = 3
# trial_list = []

# for k in range(5):
#     attempts *= 2
#     trial_list.append(attempts)

# print(trial_list)
# highest_value = max(trial_list)
# print(highest_value)




auction_dictionary = {
    "Harry": 18, 
    "Frank": 62,
    "Anthony": 34,
    "Terry": 77,
}

all_bids = []
for bidder in auction_dictionary:
    bid_amount = auction_dictionary[bidder]
    all_bids.append(bid_amount)

print(all_bids)
highest_bid = max(all_bids)
print(highest_bid)