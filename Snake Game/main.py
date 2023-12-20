from turtle import Screen,Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


# Screen setup
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()

# Snake controls
screen.listen()
screen.onkey(fun=snake.up,key="Up")
screen.onkey(fun=snake.down,key="Down")
screen.onkey(fun=snake.left,key="Left")
screen.onkey(fun=snake.right,key="Right")



game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food)<15:
        food.refresh_food()
        snake.extend()
        scoreboard.increase_score()

    #  Detect collision with wal
    if(snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280):
        game_on = False
        scoreboard.game_over()  # Display game over message
        screen.update()
        time.sleep(2)  # Wait for 2 seconds before exiting
        break  # Exit the game loop


    # Detect Collision with tail
    for snake_part in snake.snake_body[1:]:
        if snake.head.distance(snake_part) < 10:
            game_is_on = False
            scoreboard.game_over()
            screen.update()
            time.sleep(2)  # Wait for 2 seconds before exiting
            break# Exit the game loop
screen.exitonclick()


