import turtle 
a =turtle.Turtle( )
turtleScreen = turtle.Screen( )
turtleScreen.setup(600,600)
turtleScreen.bgcolor("black")
def spiral(sides,trun,color,width):

	t=turtle.Turtle()
	t.color(color)
	t.width(width)
	t.speed(0)
	for n in range(sides):
		t.forward(n)
		t.right(trun)
		t.penup()
		t.left(60)
		t.forward(10)
		t.right(60)
		t.pendown()
		t.hideturtle()
spiral(150,60,"cyan",4)