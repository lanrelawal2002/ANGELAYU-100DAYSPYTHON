row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

first_digit = int(position[0]) - 1     # first_digit represents the index in selected row
second_digit = int(position[1]) - 1     # second_digit represents the row to be selected

map[second_digit][first_digit] = "X"

print(f"{row1}\n{row2}\n{row3}")