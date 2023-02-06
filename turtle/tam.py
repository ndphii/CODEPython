import turtle
a = turtle.Screen()
a.setup(600,600)
a.bgcolor("black")
t = turtle.Turtle()
t.color("cyan")

for side in range(19):
	t.forward(29* side)
	t.right(360/3)
t.hideturtle()

