# day 12 namespace: local vs. global scope


################### Scope ####################


# def increase_rounds():
#     return rounds * 2

# rounds = 15

# adj_global = increase_rounds()
# print(f"round now original number {rounds}")
# print(f"returned round is {adj_global}")




def a_function(a_parameter):
    a_variable = 15
    return a_parameter

print(a_function(10))
#print(a_variable)