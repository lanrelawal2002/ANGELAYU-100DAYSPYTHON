# start code for day18 turtle graphics

from turtle import Turtle, Screen

donatello = Turtle()
donatello.shape("arrow")
donatello.color("dodgerblue4")

# for number in range(4):
#     donatello.right(90)
#     donatello.forward(95)

# for i in range(5):
#     donatello.pendown()
#     donatello.forward(10)
#     donatello.penup()
#     donatello.forward(10)

for a in range(3):
    donatello.right(120)
    donatello.forward(100)

for a in range(7):
    donatello.right(51.4)
    donatello.forward(100)

working_screen = Screen()
working_screen.exitonclick()