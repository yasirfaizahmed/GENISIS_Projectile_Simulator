import decimal
import math
import turtle
import time




ROUND = 3
DELTA_TIME = 0.05
END = 4
g = 9.8
G = 6969

class Projectile_Object:
	velocity_x = 0
	velocity_y = 0
	velocity_0 = 0
	xcor = 0
	ycor = 0
	angle = 0
	
	
	def __init__(self, velocity_0, angle, g=9.8, xcor=0, ycor=0):
		self.velocity_0 = velocity_0
		self.angle = math.radians(angle)
		self.xcor = xcor
		self.ycor = ycor
	
	def get_xcor(self, t):
		return round(self.velocity_0*math.cos(self.angle)*t, ROUND)
		
	def get_ycor(self, t):
		return round( (self.velocity_0*math.sin(self.angle)*t)-0.5*g*(t**2) , ROUND)
	
	def get_xvel(self):
		return round( (self.velocity_0*math.cos(self.angle)) , ROUND)
		
	def get_yvel(self, t):
		return round( (self.velocity_0*math.sin(self.angle)-g*t) , ROUND)
	
def float_range(start, end, step):
	while start < end:
		yield round(start+step, ROUND)
		start += step
	
def take_inputs():
	velocity = input()
	angle = input()
	return list([int(velocity), int(angle)])
	
def draw_ground(window):
	gr = turtle.Turtle()
	gr.speed(0)
	gr.hideturtle()
	gr.penup()
	gr.goto(-300, 0)
	gr.fillcolor("white")
	gr.begin_fill()
	for _ in range(2):
		gr.forward(600)
		gr.right(90)
		gr.forward(5)
		gr.right(90)
	gr.end_fill()
	window.update()		

def launch(t, ball, pen, window):
	pen.penup()
	pen.goto(-150,0)
	for _t in t:
		time.sleep(DELTA_TIME)
		pen.clear()
		pen.fillcolor("red")
		pen.begin_fill()
		pen.circle(5)
		pen.end_fill()
		pen.goto(ball.get_xcor(_t)*10-150, ball.get_ycor(_t)*10)
		window.update()
		


def main():
	inputs = take_inputs()
	ball = Projectile_Object(inputs[0], inputs[1])
	
	time_list = list(float_range(0, END, DELTA_TIME))
	
	pen = turtle.Turtle()
	pen.speed(0)
	pen.hideturtle()
	
	window = turtle.Screen()
	window.title("projectile simulator")
	window.bgcolor("black")
	window.setup(width=600, height=500)
	window.tracer(0)
	
	draw_ground(window)
	
	#turtle.onscreenclick(btnclick, 1)
	
	
	# pen.goto(0, 0)
	# pen.clear()
	# pen.fillcolor("black")
	# pen.begin_fill()
	# pen.circle(50)
	# pen.end_fill()
	
	window.mainloop()

if __name__ == "__main__":
	main()

