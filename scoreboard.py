from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.p1_score = 0
        self.p2_score = 0
        self.font = ("Courier", 36, "bold")
        self.initialize_ball()
        self.write(f"{self.p1_score}  {self.p2_score}", move=False, align='center', font=self.font)

    def initialize_ball(self):
        self.color("white")
        self.penup()
        self.width(5)
        self.goto(0, 600)
        self.setheading(270)
        for i in range(300):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(20)
        self.hideturtle()
        self.penup()
        self.goto(0, 480)

    def p1_scored(self):
        self.p1_score += 1
        self.clear()
        self.write(f"{self.p1_score}  {self.p2_score}", move=False, align='center', font=self.font)
        self.initialize_ball()

    def p2_scored(self):
        self.p2_score += 1
        self.clear()
        self.write(f"{self.p1_score}  {self.p2_score}", move=False, align='center', font=self.font)
        self.initialize_ball()

    def game_over(self):
        self.goto(0, 0)
        if self.p1_score > self.p2_score:
            self.clear()
            self.write(f"PLAYER 1 WINS", move=False, align='center', font=self.font)
        else:
            self.clear()
            self.write(f"PLAYER 2 WINS", move=False, align='center', font=self.font)
