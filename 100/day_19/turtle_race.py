from turtle import Turtle, Screen, pen, penup 
from random import randint

screen = Screen()
screen.setup(width = 500, height = 400)

race_on = False
user_bet = screen.textinput(title = "Make a bet", prompt = "Which turtle will win, pick a color: ")

colors = ["purple", "blue", "green", "yellow", "orange", "red"]
turtles = []
for i in range(len(colors)):
    turtles.append(Turtle(shape = "turtle"))
    turtles[i].penup()
    turtles[i].color(colors[i])

y = -125
for turtle in turtles:
    turtle.goto(-230, y)
    y += 50

if user_bet:
    race_on = True

winner = None
while race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            if user_bet == winner:
                print(f"You wonn!! {turtle.pencolor()} was the winner!")
            else:
                print(f"You lost :( {turtle.pencolor()} was the winner!")

            race_on = False
            break


        turtle.forward(randint(1,10))
        

    




screen.exitonclick()
