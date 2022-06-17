from turtle import Turtle, Screen
from random import random, choice

ajay = Turtle()
ajay.shape()
ajay.color('black')
ajay.speed("fastest")

# for _ in range(4):
#     ajay.forward(100)
#     ajay.right(90)

# for _ in range(10):
#     ajay.down()
#     ajay.forward(10)
#     ajay.up()
#     ajay.forward(10)

# 120, 90, 72, 60, 51.4286, 45, 40, 36


# for num_sides in range(3,11):
#     for _ in range(num_sides):
#         ajay.pencolor(random(), random(), random())
#         ajay.forward(100)
#         ajay.right(360/num_sides)

# angles = [0, 90, 180, 270]
# ajay.pensize(15)

# for _ in range(50):
#     ajay.pencolor(random(), random(), random())
#     ajay.forward(40)
#     # ajay.right(choice(angles))
#     ajay.setheading(choice(angles))


# for _ in range(360//6):
#     ajay.pencolor(random(), random(), random())
#     ajay.circle(100)
#     ajay.left(6)








screen = Screen()
screen.exitonclick()