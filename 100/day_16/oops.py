from turtle import Screen, Turtle

timmy = Turtle()
my_screen = Screen()    
print(my_screen.canvheight)

timmy.shape('turtle')
timmy.color('green')

timmy.forward(100)
my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column("Type", ['electric', 'water', 'fire'])

table.align = 'l'

print(table)

