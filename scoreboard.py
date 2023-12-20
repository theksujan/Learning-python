from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score=0
        self.r_score=0
        self.color("white")
        self.hideturtle()
        self.up()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 180)
        self.write(f"{self.l_score}", False, "center", ("Courier", 50, 'normal'))
        self.goto(100, 180)
        self.write(f"{self.r_score}", False, "center", ("Courier", 50, 'normal'))



    def l_point(self):
        self.l_score+=1
        self.clear()
        self.update_scoreboard()

    def r_point(self):
        self.r_score+=1
        self.clear()
        self.update_scoreboard()


