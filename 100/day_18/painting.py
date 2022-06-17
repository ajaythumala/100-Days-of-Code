import colorgram as cg
import turtle
from turtle import Turtle, Screen
from random import random, choice

ajay = Turtle()
ajay.shape()
ajay.speed("fastest")
turtle.colormode(255)

colors = cg.extract('100/day_18/1.jpg', 100)

rgb_colors = []
for color in colors:
    c = color.rgb
    rgb_colors.append((c.r, c.g, c.b ))

for _ in range(4):
    rgb_colors.remove(rgb_colors[0])

ajay.penup()
ajay.hideturtle()

ajay.setheading(225)
ajay.forward(300)
ajay.setheading(0)


# for _ in range(10):
for count in range(1, 101):
    ajay.dot(20, choice(rgb_colors)) 
    ajay.forward(50)
    if count % 10 == 0:
        ajay.left(90)
        ajay.forward(50)
        ajay.left(90)
        ajay.forward(500)
        ajay.right(180)




screen = Screen()
screen.exitonclick()

