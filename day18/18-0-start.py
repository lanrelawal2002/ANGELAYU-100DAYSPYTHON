# start code for day18 turtle graphics

from turtle import Turtle, Screen

donatello = Turtle()
donatello.shape("turtle")
donatello.color("dodgerblue4")

for number in range(4):
    donatello.right(90)
    donatello.forward(95)
# donatello.right(90)
# donatello.forward(95)
# donatello.right(90)
# donatello.forward(95)
# donatello.right(90)
# donatello.forward(95)

working_screen = Screen()
working_screen.exitonclick()