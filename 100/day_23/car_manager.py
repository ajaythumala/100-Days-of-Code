COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
NUM_CARS = 20

STARTING_MOVE_DISTANCE = 0.5
MOVE_INCREMENT = 10
from turtle import Turtle
from random import randint, choice


class CarManager:
    def __init__(self) -> None:
        self.cars = []
        self.create_cars()
        
    def create_cars(self):
        for i in range(NUM_CARS):
            self.cars.append(Turtle())
            self.cars[i].shape("square")
            self.cars[i].color(choice(COLORS))
            self.cars[i].shapesize(1, 2)
            self.cars[i].penup()
            self.cars[i].goto(randint(-280, 280), randint(-250, 280))

    def move(self):
        for i in range(NUM_CARS):
            self.cars[i].goto(self.cars[i].xcor() - STARTING_MOVE_DISTANCE, self.cars[i].ycor())

    def reset(self):
        for i in range(NUM_CARS):
            if self.cars[i].xcor() < -300:
                self.cars[i].goto(300, randint(-250, 280))

    def collides(self, player):
        for i in range(NUM_CARS):
            if self.cars[i].distance(player) < 30 and (player.ycor() > self.cars[i].ycor() - 20 or player.ycor() < self.cars[i].ycor() + 20):
                return True
        return False
        

