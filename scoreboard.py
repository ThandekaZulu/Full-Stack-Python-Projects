from turtle import Turtle
ALIGNMEMNT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    # Method to initialize the score display
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMEMNT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMEMNT, font=FONT)

    # Method to update the score display
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    
