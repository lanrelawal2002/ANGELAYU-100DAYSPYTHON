# second test file
from turtle import Turtle, Screen

michelangelo = Turtle()

for value in range(5):
    michelangelo.pendown()
    michelangelo.forward(26)
    michelangelo.penup()
    michelangelo.forward(26)
    # michelangelo.pendown()
    # michelangelo.forward(26)

third_screen = Screen()
third_screen.exitonclick()