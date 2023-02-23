from turtle import Turtle, Screen

matsuyoki = Turtle()


def move_forwards():
    matsuyoki.forward(20)


def move_backwards():
    matsuyoki.backward(20)


def counter_clockwise():
    matsuyoki.left(10)


def clockwise():
    matsuyoki.right(10)


def clear_drawing():
    test_screen.resetscreen()
    # matsuyoki.clear()
    # matsuyoki.penup()
    # matsuyoki.home()
    # matsuyoki.pendown()


test_screen = Screen()
test_screen.listen()
test_screen.onkey(fun=move_forwards, key="w")
test_screen.onkey(fun=move_backwards, key="s")
test_screen.onkey(fun=clockwise, key="d")
test_screen.onkey(fun=counter_clockwise, key="a")
test_screen.onkey(fun=clear_drawing, key="c")
test_screen.exitonclick()
