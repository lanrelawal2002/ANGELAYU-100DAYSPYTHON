# From 13 lines to 7 lines
print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))

total_people = int(input("How many people to split the bill? "))

percent_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

tip_amount = ((total_bill) + ((percent_tip) / 100) * (total_bill))

final_amount = ((tip_amount / (total_people)))

print(f"Each person should pay: ${final_amount:.2f}")

# Remember to always type cast early to keep rest of code compact and free of type cast 
# written out in full.
