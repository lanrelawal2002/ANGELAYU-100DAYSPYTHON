import random


# for number in range(1, 4):
#     print(number)

# number = random.randrange(2)
# print(number)

# score = random.randint(7, 10)
# print(score)



def check_value():
    while value:
        if score > 1 and (score * 2) == 15:
            # value = False
            return "no coins left"
        elif score > 55 and (score **2) < 5 and (score + 18) != 13:
            # value = False
            return "find coins first"
        elif score == 11:
            return 11


value = True
score = 11


result = check_value()
print(result)