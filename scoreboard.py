from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.update_level()

    def levelup(self):
        self.level += 1
        self.clear()
        self.update_level()

    def update_level(self):
        self.write(f"Level: {self.level}", font=FONT)

    def game_over_message(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!",align="center", font=FONT)
