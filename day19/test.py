# run all tests here

from turtle import Turtle, Screen

matsuyoki = Turtle()
matsuyoki.speed("slow")

# def counter_clockwise():
#     matsuyoki.left(10)
#     matsuyoki.forward(30)

number_of_sides = 10

angle = 360 / number_of_sides
for w in range(number_of_sides):
    matsuyoki.right(angle)
    matsuyoki.forward(55)

for number in range(5):
    matsuyoki.forward(55)
    matsuyoki.setheading(33)

matsuyoki.clear()

test_screen = Screen()
# test_screen.listen()
# test_screen.onkeyrelease(fun=counter_clockwise, key="a")
# test_screen.clearscreen()
# test_screen.resetscreen()
test_screen.exitonclick()
