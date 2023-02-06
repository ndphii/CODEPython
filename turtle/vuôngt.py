import turtle
turtleObj = turtle.Turtle( )
turtleScreen = turtle.Screen( )
turtleScreen.setup(600,600)
turtleScreen.bgcolor("black")
turtleObj.shape("arrow")
turtleObj.pensize(3)
turtle.speed(1)
colors = ['violet','indigo','blue','green','yellow','orange','red']
for i in range(50):
    turtleObj.pencolor(colors[i%7])
    for j in range(4):
        turtleObj.forward(200)
        turtleObj.right(90)
    turtleObj.right(10)
turtleObj.penup( )
turtleObj.stepos(-150,200)
turtleObj.write("python_scripts",font=("Arial",200,"bold"))
turtleObj.ht( )
turtleObj.done( )