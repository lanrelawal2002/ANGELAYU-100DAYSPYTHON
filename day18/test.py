# angela's version of random walk .... challenge 4
# with my modifications of screen and import type
import turtle
import random

tim = turtle.Turtle()
turtle.colormode(255)

# def random_colors():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     colors = (r, g, b)
#     return colors

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

directions = [0, 90, 180, 270]
tim.pensize(1)
tim.speed("fastest")

for number in range(10):
    # tim.color(random_colors())
    tim.forward(30)
    tim.setheading(random.choice(directions))

print(tim.heading())
print(tim.position())

my_screen = turtle.Screen()
my_screen.exitonclick()
