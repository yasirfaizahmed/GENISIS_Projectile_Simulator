import decimal
import math
import turtle
import time




ROUND = 3
RADIUS = 5
DELTA_TIME = 0.03
END = 4
SCALE = 5
g = 9.8
G = 6969
FONT_SIZE = 17
FONT = ('Arial', FONT_SIZE, 'bold')

class Projectile_Object:
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
	
	def get_flighttime(self):
		return round( (2*self.velocity_0*math.sin(self.angle)/g) , ROUND)
	
	def max_height(self):
		return round( (((self.velocity_0*math.sin(self.angle))**2)/(2*g)) , ROUND)
	
def float_range(start, end, step):
	while start < end:
		yield round(start+step, ROUND)
		start += step
	
def take_inputs():
	velocity = input("Enter velocity :")
	angle = input("Enter angle of launch :")
	return list([int(velocity), int(angle)])
	
def draw_ground(window):
	gr = turtle.Turtle()
	gr.speed(0)
	gr.hideturtle()
	gr.penup()
	gr.goto(-800,-250)
	gr.fillcolor("#734d26")
	gr.begin_fill()
	for _ in range(2):
		gr.forward(1600)
		gr.right(90)
		gr.forward(500)
		gr.right(90)
	gr.end_fill()
	window.update()		

def launch(t, ball, pen, window):
	trail = turtle.Turtle()
	trail.hideturtle()
	trail.speed(0)
	
	trail.goto(-505,-250)
	trail.color("white")
	trail.left(math.degrees(ball.angle))
	trail.forward(350)
	trail.penup()
	
	maxheight = ball.max_height()
	trail.color("red")
	trail.goto(-500,-250)
	pen.goto(-500, -250)
	for _t in t:
		time.sleep(DELTA_TIME)
		pen.clear()
		trail.fillcolor("red")
		pen.fillcolor("red")
		pen.begin_fill()
		trail.begin_fill()
		pen.circle(RADIUS)
		trail.circle(1)
		pen.end_fill()
		trail.end_fill()
		
		pen.goto(ball.get_xcor(_t)*SCALE-500, ball.get_ycor(_t)*SCALE-250)
		trail.goto(ball.get_xcor(_t)*SCALE-500, ball.get_ycor(_t)*SCALE-250+RADIUS)
		
		trail.penup()
		window.update()
	
def draw_launch(window):
	ln = turtle.Turtle()
	ln.hideturtle()
	ln.speed(0)
	ln.goto(0, 300)
	ln.color("white")
	ln.write("Hit 'Space' to LAUNCH", align="center", font=FONT)
	window.update()
	
	

def main():
	inputs = take_inputs()
	ball = Projectile_Object(inputs[0], inputs[1])
	
	END = ball.get_flighttime()
	time_list = list(float_range(0, END, DELTA_TIME))
	
	pen = turtle.Turtle()
	pen.speed(0)
	pen.hideturtle()
	
	window = turtle.Screen()
	window.title("projectile simulator")
	window.bgcolor("black")
	window.setup(width=1400, height=800)
	window.tracer(0)
	
	draw_launch(window)
	draw_ground(window)
	print(ball.max_height())
	
	window.listen()
	window.onkeyrelease(lambda:launch(time_list, ball, pen, window), "space")
	
	window.mainloop()

if __name__ == "__main__":
	main()

