import decimal
import math
import turtle

window = turtle.Screen()
window.title("projectile simulator")
window.bgcolor("black")
window.setup(width=450, height=600)
window.tracer(0)

velocity_x = 0
velocity_y = 0
angle = 90	#degrees
g = 9.8
G = 6969

v_0 = 15 #m/s



def float_range(start, end, step):
	while start < end:
		yield round(start+step, 2)
		start += step

time = list(float_range(0, 3, 0.05)) 

angle = math.radians(angle)
for t in time:
	#print( round(v_0*(math.sin(angle)) - g*t, 2))
	print( round( ((v_0*(math.sin(angle))*t - 0.5*g*(t**2)) ), 2) )
	
window.mainloop()