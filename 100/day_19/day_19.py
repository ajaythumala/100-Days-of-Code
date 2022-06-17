from turtle import Turtle, Screen, clearscreen, resetscreen
ajay = Turtle()
screen = Screen()

def move_f():
    ajay.forward(10)
def move_b():
    ajay.back(10)
def turn_l():
    ajay.left(5)
def turn_r():
    ajay.right(5)
def clear():
    # could also use home() and clear()
    resetscreen()
    ajay.setposition(0,0)
    ajay.setheading(0)

screen.listen()

screen.onkeypress(key = "w", fun = move_f)
screen.onkeypress(key = "s", fun = move_b)
screen.onkeypress(key = "a", fun = turn_l)
screen.onkeypress(key = "d", fun = turn_r)
screen.onkey(key = "c", fun = clear)


screen.exitonclick()
