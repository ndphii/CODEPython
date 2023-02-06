import turtle 
a =turtle.Turtle( )
turtleScreen = turtle.Screen( )
turtleScreen.setup(600,600)
turtleScreen.bgcolor("black")
a.color("#EA005E")
a.speed(0)
def draw_square(lenght):
	for side in range(4):
		a.forward(lenght)
		a.right(90)
		for side in range(4):
			a.forward(50)
			a.right(90)


a.penup( )
a.back(20)
a.pendown( )

for squaare in range(80):
	draw_square(5)
	a.forward(5)
	a.left(5)
a.hideturtle( )
print('{:-^11}'.format('END'))