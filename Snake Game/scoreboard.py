from turtle import Turtle,Screen
SCORE=0
ALIGNMENT="center"
FONT=('Courier',24,'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=SCORE

        # Setting display position
        self.color("white")
        self.hideturtle()
        self.up()
        self.score_x=0
        self.score_y=250
        self.goto(self.score_x,self.score_y)

        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score:{self.score}",move=False,align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()
    #
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", False,align=ALIGNMENT, font=FONT)







