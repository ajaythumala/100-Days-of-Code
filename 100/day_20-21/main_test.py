from turtle import Screen
from scoreboard import Scoreboard#, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) # ii. turn of tracer


# 1. create snake body.
# turtle size - 20 x 20

# starting_pos = [(0,0), (-20, 0), (-40, 0)]
# segments = []
# for pos in starting_pos:
#     new_segment = Turtle(shape = "square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(pos)
#     segments.append(new_segment)

snake = Snake()
# 4. creating food
food = Food()
scoreboard = Scoreboard()

# 3. controlling the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# 2. moving the snake.
# i. fix the line being drawn
# ii. turn off tracer
# iii. update screen only when all segments have moved to new postion
# iv. use time.sleep() to slow down
# v. we need to link the segments of the snake

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # for seg in segments:
    #     seg.forward(20)

    snake.move()
    # for seg_num in range(len(segments) - 1, 0, -1):
    #     new_x = segments[seg_num - 1].xcor()
    #     new_y = segments[seg_num - 1].ycor()
    #     segments[seg_num].goto(new_x, new_y)
    # segments[0].forward(20)

    # 5. detecting collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        # 6. increasing score
        snake.extend()
        scoreboard.increase_score()

        #increasing size of snake

    
    # 7. detection with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # 8. detection with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


    
        
    







screen.exitonclick()