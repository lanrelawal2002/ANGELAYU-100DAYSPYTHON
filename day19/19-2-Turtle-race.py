# my version of turtle racing game  

# CHECK FOR PURPLE TURTLE ALWAYS WINNING ALL RACES

# run all tests here

import random
# run all tests here
import random
from turtle import Turtle, Screen
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_coordinates = [-170, -104, -38, 38, 104, 170]

race_is_on = False
all_turtles = []

for number in range(6):
    ninjitsu = Turtle(shape="turtle")
    # ninjitsu.speed("slow")
    ninjitsu.color(colors[number])
    ninjitsu.penup()
    ninjitsu.goto(x=-235, y=y_coordinates[number])
    all_turtles.append(ninjitsu)

shao_screen = Screen()
shao_screen.setup(width=500, height=400)
user_guess = shao_screen.textinput(title="TURTLE RACING", prompt="What turtle color will win the race? ")

if user_guess:
    race_is_on = True

while race_is_on:
    for current_turtle in all_turtles:
        if current_turtle.xcor() > 230:
            race_is_on = False
            winning_color = current_turtle.pencolor()
            if winning_color == user_guess:
                print(f"You have won. The {winning_color} turtle is the winner!")
            else:
                print(f"You lost. The {winning_color} turtle is the winner!")

    selected_distance = random.randint(0, 10)
    current_turtle.forward(selected_distance)


shao_screen.exitonclick()
