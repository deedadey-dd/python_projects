# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("coral2")
# print(timmy)
# timmy.forward(100)
# timmy.left(120)
# timmy.forward(100)
# timmy.left(120)
# timmy.forward(100)
# timmy.right(60)
# timmy.forward(100)
# timmy.right(60)
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable
table = PrettyTable()

c1 = {
    "Pokemon Name": ["Pikachu", "Squirtle", "Charmander"],
    "Type": ["Electric", "Water", "Fire"],
}
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])

for key in c1.keys():
    table.add_column(key, c1[key])

table.align = "r"

print(table)
