from turtle import Turtle
import random


class Ball:
    def __init__(self):
        self.new_heading = None
        self.starting_heading = random.choice([i for i in range(0, 359) if i not in [0, 90, 180, 270]])
        self.ball = Turtle()
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.setheading(self.starting_heading)
        self.ball.speed("fastest")

    def forward(self, x):
        self.ball.forward(x)

    def bounce_off_wall(self):
        self.new_heading = self.starting_heading * (-1)
        self.ball.setheading(self.new_heading)
        self.starting_heading = self.new_heading

    def bounce_off_paddle(self):
        self.new_heading = 180 - self.starting_heading
        self.ball.setheading(self.new_heading)
        self.starting_heading = self.new_heading
