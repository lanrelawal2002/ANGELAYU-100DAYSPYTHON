
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
# print((((12/100) * 124.56) + 124.56) / 7 )
# print(124.56 * 1.12)
# print(150 * 1.12)
# print("OR")

# print((124.56 / 7) * (1.12))
print("Welcome to the tip calculator.")

total_bill = input("What was the total bill? $")

total_people = input("How many people to split the bill? ")

percent_tip = input("What percentage tip would you like to give? 10, 12, or 15? ")

total_bill_as_float = float(total_bill)
percent_tip_as_int = int(percent_tip)
total_people_as_int = int(total_people)

tip_percentage = ((percent_tip_as_int / 100) * total_bill_as_float)

tip_amount = (total_bill_as_float + tip_percentage)

initial_ind_payment = (tip_amount / total_people_as_int)

final_ind_payment = (round(initial_ind_payment, 2))

result = f"Each person should pay: ${final_ind_payment}"  

print(result)