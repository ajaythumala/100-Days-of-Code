# import time
from turtle import Screen
from player import Player
from car_manager import CarManager
# from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

player = Player()
cars = CarManager()



screen.listen()
screen.onkey(player.up, "Up")


game_is_on = True
while game_is_on:
    # time.sleep(0.1)
    screen.update()

    cars.move()
    cars.reset()

    #collision
    if cars.collides(player):
        print("hello world")
        break
    #finish line
    if player.ycor() > 280:
        player.finished()
