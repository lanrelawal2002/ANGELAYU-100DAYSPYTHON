# my version of spirograph - turtle challenge 5


## RUNNING THE CODE WILL MAKE VSCODE GET STUCK....
# leave all spirograph code commented


### START SPIROGRAPH ###
# import turtle
# import random

# ninja_turtle = turtle.Turtle()
# turtle.colormode(255)


# def any_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)

#     colors = (r, g, b)
#     return colors


# ninja_turtle.speed("fast")
# counting = True
# angle = 6

# while counting:
#     if angle > 360:
#         counter = False
#     else:
#         ninja_turtle.pencolor(any_color())
#         ninja_turtle.circle(100)
#         ninja_turtle.setheading(angle)
#         angle += 6


# print(ninja_turtle.position())
# print(ninja_turtle.heading())

# ninja_screen = turtle.Screen()
# ninja_screen.exitonclick()

### END SPIROGRAPH ###



# Visualization of number of rounds and degrees per turtle circle

counting = True
angle = 6
rounds = 1

while counting:
    if angle > 360:
        counting = False
    else:
        print(f"round {rounds} -- angle {angle}.")
        angle += 6
        rounds += 1