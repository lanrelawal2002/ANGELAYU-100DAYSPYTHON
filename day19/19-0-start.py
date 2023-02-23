from turtle import Turtle, Screen

matsuyoki = Turtle()


def move_right():
    matsuyoki.forward(50)
    matsuyoki.right(35)
    matsuyoki.forward(10)


instant_screen = Screen()
instant_screen.listen()
instant_screen.onkeyrelease(fun="move_right", Key="Up")
instant_screen.exitonclick()
