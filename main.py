from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
invalid = True
race_on = True
user_input = ()
y = -140
turtles = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

while invalid:
    if user_input not in colors:
        user_input = screen.textinput(title="Make Your Bet",
                                      prompt="Which turtle will win the race? Enter a color: ").lower()
    else:
        invalid = False
for n in range(6):
    tim = Turtle(shape= "turtle")
    tim.penup()
    tim.color(colors[n])
    y += 40
    tim.goto(-220, y)
    turtles.append(tim)

while race_on:
    for turtle in turtles:
        chosen_int = random.randint(0, 10)
        turtle.forward(chosen_int)
        if turtle.xcor() >= 250:
            race_on = False
            winner = turtle

if winner.color()[0] == user_input:
    print(f"The {winner.color()[0]} turtle wins! You guessed it!")
else:
    print(f"The {winner.color()[0]} turtle wins! You lose!")
screen.exitonclick()
