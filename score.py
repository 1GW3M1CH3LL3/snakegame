from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.num = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.num}",
        move = False,
        align = ALIGNMENT,
        font = FONT)
        self.hideturtle()
    def update_score(self):
        self.write(f"Score: {self.num}",
        move = False,
        align = ALIGNMENT,
        font = FONT)  
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER",
        move = False,
        align = ALIGNMENT,
        font = FONT) 

    def increase_score(self):
        self.num += 1 
        self.clear() 
        self.update_score()
        