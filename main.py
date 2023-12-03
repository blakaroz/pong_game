from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)


r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


is_game_on = True
while True:
    time.sleep(0.05)
    screen.update()
    ball.move()

#detect colision with wall
    if ball.ycor()>280 or ball.ycor() < - 280:
        ball.bounce_y()

#detect colision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
        ball.bounce_x()


screen.exitonclick()