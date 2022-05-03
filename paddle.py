from turtle import Turtle


class Paddle:
    def __init__(self, x):
        self.paddle = Turtle()
        self.paddle.shape("square")
        self.paddle.shapesize(stretch_wid=1, stretch_len=4)
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.setheading(90)
        self.paddle.goto(x, 0)
        self.paddle.speed("fastest")

    def forward(self):
        if self.paddle.ycor() > 460:
            pass
        else:
            self.paddle.forward(20)

    def backward(self):
        if self.paddle.ycor() < -460:
            pass
        else:
            self.paddle.backward(20)
