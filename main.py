from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball


Ball_Speed = 0.4


screen = Screen()
screen.setup(1920, 1080)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
scoreboard = Scoreboard()
paddle1 = Paddle(-920)
paddle2 = Paddle(920)
ball = Ball()
screen.onkeypress(paddle1.forward, "w")
screen.onkeypress(paddle1.backward, "s")
screen.onkeypress(paddle2.forward, "Up")
screen.onkeypress(paddle2.backward, "Down")
screen.listen()


game_is_on = True
while game_is_on:
    screen.update()
    ball.forward(Ball_Speed)

    if ball.ball.xcor() > 920:
        scoreboard.p1_scored()
        ball.ball.hideturtle()
        ball = Ball()

    if ball.ball.xcor() < -920:
        scoreboard.p2_scored()
        ball.ball.hideturtle()
        ball = Ball()

    if ball.ball.ycor() > 500 or ball.ball.ycor() < -500:
        ball.bounce_off_wall()

    if ball.ball.distance(paddle1.paddle) <= 50 or ball.ball.distance(paddle2.paddle) <= 50:
        ball.bounce_off_paddle()

    if scoreboard.p1_score == 5 or scoreboard.p2_score == 5:
        game_is_on = False
        scoreboard.game_over()


screen.exitonclick()
