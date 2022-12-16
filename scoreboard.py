from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.board()

    def board(self):
        self.clear()
        self.goto(-100, 260)
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)
        self.goto(100, 260)
        self.write(f"High Score: {self.high_score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.board()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.board()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGN, font=FONT)