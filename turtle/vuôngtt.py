import turtle 
a =turtle.Turtle( )
turtleScreen = turtle.Screen( )
turtleScreen.setup(500,500)
turtleScreen.bgcolor("black")
a.color("cyan")
a.speed(0)
def draw_square():
	for side in range(4):
		a.forward(100)
		a.right(90)
		for side in range(4):
			a.forward(50)
			a.right(90)
draw_square()

def new_function():
	for suqre in range(30):
		draw_square()
		a.penup()
		a.forward(20)
		a.left(45)
		a.pendown()
new_function()