import random

names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")

index_range_end = len(names) - 1
random_name_index = random.randint(0, index_range_end)
buyer = names[random_name_index]
print(f"{buyer} is going to buy the meal today!")