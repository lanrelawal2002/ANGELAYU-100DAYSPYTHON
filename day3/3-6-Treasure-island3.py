print("Welcome to TREASURE ISLAND")
print("Your mission is to find the treasure!!")

choice1 = input("Go 'left' or 'right'. \"Decide now\" ").lower()
if choice1 == "left":
    choice2 = input("Now 'swim' or 'wait' \"Decide now\" ").lower()
    if choice2 == "wait":
        choice3 = input("Choose a door. \"Red\", \"Yellow\", or \"Blue\" ").lower()
        if choice3 == "red":
            print("In a room on fire. Game over")
        elif choice3 == "yellow":
            print("You found the treasure. You won!!!")
        elif choice3 == "blue":
            print("You entered a room filled with beasts. Game over")
        else:
            print("This door does not exist. Game over")
    else:
        print("You got attacked by a trout. Game over")
else:
    print("You fell into a hole. Game over")

