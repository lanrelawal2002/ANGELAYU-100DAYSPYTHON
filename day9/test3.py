
# dict = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
# }

# # print(dict)

# for key in dict:
#     dict[key] += 1
    
# dict[1] = 4
# print(dict[1])

# ***********************************************************************


# order = {
#     "starter": {1: "Salad", 2: "Soup"},
#     "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
#     "dessert": {1: ["Ice Cream"], 2: []},
# }

# print(order["main"][2])

# **************************************************************************



order2 = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: {0: "SFC", 4: "McD"}},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order2["main"][2][0])