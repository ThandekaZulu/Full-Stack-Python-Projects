from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        # self.high_score = 0
        # if self.file_exists():
        with open("scoreboard.txt") as file:
                # content = file.read().strip()
                # if content.isdigit():
          self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # Save scoreboard in a file
            with open("scoreboard.txt", mode="w") as file: # a = append
              file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
    

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        # with open("scoreboard.txt", mode="w") as file:
        #   file.write(f"{self.score},{self.high_score}")
    
