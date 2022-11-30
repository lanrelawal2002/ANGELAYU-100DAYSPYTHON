import random


# for number in range(1, 4):
#     print(number)

# number = random.randrange(2)
# print(number)

# score = random.randint(7, 10)
# print(score)



def check_value():
    while value:
        if score > 1:
            # value = False
            return "no coins left"
        elif score < 1:
            # value = False
            return "find coins first"


value = True
score = 11


result = check_value()
print(result)