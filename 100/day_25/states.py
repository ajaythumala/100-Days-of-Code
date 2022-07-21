from turtle import Turtle
FONT = ("Courier", 8, "normal")

class States_Screen(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
    
    def update_screen(self, answer, coordinates):
        self.goto(coordinates[0], coordinates[1])
        self.write(f"{answer}", font = FONT)
        
