# main.py
import time
from scoreboard import Scoreboard
from ball import Ball
from turtle import Turtle, Screen
from paddle import Paddle

# Screen setup
screen = Screen()
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

# Create paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Event bindings
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

screen.listen()

game_on = True
while game_on:
    ball.move()
    screen.update()
    time.sleep(0.03)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 330) or \
            (ball.distance(l_paddle) < 50 and ball.xcor() < -330):
        ball.bounce_x()

    # Detect right paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect left paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

# Start the game
screen.mainloop()
