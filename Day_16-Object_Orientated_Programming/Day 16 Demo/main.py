# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
#
# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Bulbasaur", "Charmander", "Squirtle"])
table.add_column("Type", ["Grass - Poison", "Fire", "Water"])
table.align = "l"
print(table)
