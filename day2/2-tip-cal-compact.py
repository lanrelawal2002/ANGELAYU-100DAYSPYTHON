# From 13 lines to 7 lines
print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))

total_people = int(input("How many people to split the bill? "))

percent_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

tip_amount = ((total_bill) + ((percent_tip / 100) * total_bill))

total_payment = (tip_amount / total_people)

# final_amount = round(total_payment, 2)

print("Each person should pay: ${:.2f}".format(total_payment))

# print(f"Each person should pay: ${final_amount}")
