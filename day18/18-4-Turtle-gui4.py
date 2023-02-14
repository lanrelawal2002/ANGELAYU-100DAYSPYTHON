from turtle import Turtle, Screen
import random


def move_right(degree):
    raphael.right(degree)
    raphael.forward(50)


def move_left(degree):
    raphael.left(degree)
    raphael.forward(50)


raphael = Turtle()
raphael.pensize(10)
raphael.speed(10)

angles = [90, 0, 180]
walking = True
counter = 100

path = [move_right, move_left]

color_list = ['red', 'black', 'orange', 'yellow', 'green', 'blue',
  'purple', 'pink', 'brown', 'gray', 'gold', 'cyan', 'Gainsboro', 'gray',
  'dimgray', 'LightSlateGray', 'AliceBlue', 'LimeGreen', 'DarkKhaki', 'Khaki']

while walking:
    if counter == 0:
        walking = False
    else:
        raphael.color(random.choice(color_list))
        angle = random.choice(angles)
        direction = random.choice(path)
        direction(angle)
        # raphael.right(angle)
        # raphael.forward(50)
        counter -= 1


rand_walk_screen = Screen()
rand_walk_screen.exitonclick()