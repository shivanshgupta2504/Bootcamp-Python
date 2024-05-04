from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreborard()

    def update_scoreborard(self):
        """
        Update the scoreboard
        :return:
        """
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """
        Increase the score
        """
        self.score += 1
        self.clear()
        self.update_scoreborard()

    def game_over(self):
        """
        Game over
        """
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

