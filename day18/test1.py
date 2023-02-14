# # first test file
# import turtle as tt

# leonardo = tt.Turtle()

# number_of_sides = 3

# angle = 360 / number_of_sides
# for w in range(number_of_sides):
#     leonardo.right(angle)
#     leonardo.forward(100)

# first_screen = tt.Screen()
# first_screen.exitonclick()

import random
import turtle as tt

leonardo = tt.Turtle()

all_colors = ["indianred2", "khaki", "red", "lavenderblush3", "magenta1", "orange", 
"palegreen", "red3", "thistle1", "beige", "cornsilk4", "black"]

number_of_sides = 3
counter = True

while counter:
    if number_of_sides > 10:
        counter = False
    else:
        leonardo.color(random.choice(all_colors))
        angle = 360 / number_of_sides
        for w in range(number_of_sides):
            leonardo.right(angle)
            leonardo.forward(95)
        number_of_sides += 1

first_screen = tt.Screen()
first_screen.exitonclick()
