from turtle import Turtle,Screen,mainloop

def create_flower(pen, palette):
	pen.color(palette[1])
	for i in range(6):
		pen.lt(30),pen.fd(150)
		pen.bk(150 * 2), pen.goto(0, 0)

	pen.color(palette[2]),pen.seth(15)
	for i in range(6):
		pen.lt(30), pen.fd(150)
		pen.bk(150 * 2), pen.goto(0, 0)
	pen.color(palette[3], palette[4]),pen.width(5)
	pen.home(),pen.seth(90)
	pen.pu(),pen.goto(100,0),pen.pd()
	pen.begin_fill(),pen.circle(100),pen.end_fill()

def additional(pen):
	pen.pu(),pen.home(),pen.pd()
	for i in range(2):
		pen.home()
		if i % 2 != 0 :
			pen.seth(90)
		pen.fd(50),pen.bk(100)
	pen.pu(),pen.goto(25,0),pen.pd()
	for i in range(4):
		pen.fd(50),pen.bk(25)
		pen.lt(90),pen.bk(25)
		pen.fd(50)

def main():
	space = Screen()
	pen = Turtle()
	palette = ["#DCFFB2","#F3B600","#F3E700",
			   "#713700","#8C4400"]
	space.title("Sunflower"),space.setup(500,500)
	space.bgcolor("cyan")
	space.delay(3),pen.speed(8)
	pen.width(40)
	create_flower(pen, palette)
	additional(pen)
	pen.ht()

if __name__ == "__main__":
	main()
	mainloop()