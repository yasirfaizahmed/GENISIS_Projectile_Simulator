import decimal
import math
import turtle
import time
#
ROUND = 3
RADIUS = 5
DELTA_TIME = 0.02
END = 4
SCALE = 10

G = 6969
FONT_SIZE = 17
FONT = ('Arial', FONT_SIZE, 'bold')
#
colors = {
        1: "white",
        2: "yellow",
        3: "orange",
        4: "pink",
        5: "red",
        6: "light green",
        7: "green",
        8: "#6C1592"
    }
class Projectile_Object:
    velocity_0 = 0
    xcor = 0
    ycor = 0
    angle = 0
    g = 9.8
    color = "red"
    planet = 3
    def __init__(self, velocity_0, angle, xcor=0, ycor=0, planet=3):
        self.velocity_0 = velocity_0
        self.angle = math.radians(angle)
        self.xcor = xcor
        self.ycor = ycor
        self.planet = planet
        if planet == 1:
            self.g = 3.61
        elif planet == 2:
            self.g = 8.83
        elif planet == 3:
            self.g = 9.8
        elif planet == 4:
            self.g = 3.75
        elif planet == 5:
            self.g = 26.0
        elif planet == 6:
            self.g = 11.2
        elif planet == 7:
            self.g = 10.5
        elif planet == 8:
            self.g = 13.3
        self.color = colors[planet]
    def get_xcor(self, t):
        self.xcor = round(self.velocity_0*math.cos(self.angle)*t, ROUND)
        return self.xcor
    def get_ycor(self, t):
        self.ycor = round( (self.velocity_0*math.sin(self.angle)*t)-0.5*self.g*(t**2) , ROUND)
        return self.ycor
    def get_xvel(self):
        return round( (self.velocity_0*math.cos(self.angle)) , ROUND)
    def get_yvel(self, t):
        return round( (self.velocity_0*math.sin(self.angle)-self.g*t) , ROUND)
    def get_flighttime(self):
        return round( (2*self.velocity_0*math.sin(self.angle)/self.g) , ROUND)
    def max_height(self):
        return round( (((self.velocity_0*math.sin(self.angle))**2)/(2*self.g)) , ROUND)
    def range(self):
        return round( (self.velocity_0**2)*math.sin(2*self.angle)/self.g , ROUND)
def float_range(start, end, step):
    while start < end:
        yield round(start+step, ROUND)
        start += step
def take_inputs():
    try:
        velocity = int(input("\t\tEnter velocity in m/s        :"))
        angle = int(input("\t\tEnter angle of launch in degrees:"))
        planet = int(input("\n\t\tWhich planet are you in?, enter the number\n\tMercury-->1\n\tVenus-->2\n\tEarth-->3\n\tMars-->4\n\tJupyter-->5\n\tSaturn-->6\n\tUranus-->7\n\tNeptune-->8\n\n\tAll at once-->9\n\t\t"))
        
    except:
        print("\tOnly integral values are allowed!")
        return take_inputs()
    return list([velocity, angle, planet])
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
    #drawing the angle line
    trail.goto(-685,-250)
    trail.color("white")
    trail.left(math.degrees(ball.angle))
    trail.forward(350)
    trail.penup()
    #going to the default positions
    trail.goto(-680,-250)
    pen.goto(-700, -250)
    i = 0
    for _t in t:
        time.sleep(DELTA_TIME)
        pen.clear()
        trail.fillcolor(ball.color)
        pen.fillcolor(ball.color)
        pen.begin_fill()
        trail.begin_fill()
        pen.circle(RADIUS)
        trail.circle(1)
        pen.end_fill()
        trail.end_fill()
        #drawing the ball and trail at once
        pen.goto(ball.get_xcor(_t)*SCALE-680, ball.get_ycor(_t)*SCALE-250)
        trail.goto(ball.get_xcor(_t)*SCALE-680, ball.get_ycor(_t)*SCALE-250+RADIUS)
        #max height
        if i == int(len(t)/2):
            trail.penup()
            trail.color("white")
            trail.goto(ball.get_xcor(_t)*SCALE-680, ball.get_ycor(_t)*SCALE-240)
            trail.write(str(ball.max_height()), align="center", font=('Arial', 13, 'bold'))
            trail.penup()
            window.update()
        #
        i += 1
        trail.penup()
        window.update()
    #max range 
    trail.penup()
    trail.goto(ball.get_xcor(_t)*SCALE-690, ball.get_ycor(_t)*SCALE-240)
    trail.write(str(ball.range()), align="center", font=('Arial', 13, 'bold'))
    trail.penup()
    window.update()
    #printing some data
    print("\n\t\tMaximum height         :", ball.max_height())
    print("\t\tMaximum horizontal range :", ball.range())
    print("\t\tX componte in velocity   :", ball.get_xvel())
    #print("\t\tY componte in velocity   :", ball.get_yvel())
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
    ball = Projectile_Object(inputs[0], inputs[1], planet=inputs[2])
    #
    END = ball.get_flighttime()
    time_list = list(float_range(0, END, DELTA_TIME))
    #
    pen = turtle.Turtle()
    pen.speed(0)
    pen.hideturtle()
    #
    window = turtle.Screen()
    window.title("projectile simulator")
    window.bgcolor("black")
    window.setup(width=1400, height=800)
    window.tracer(0)
    #
    draw_launch(window)
    draw_ground(window)
    #
    window.listen()
    window.onkeyrelease(lambda:launch(time_list, ball, pen, window), "space")
    #
    window.mainloop()
if __name__ == "__main__":
    main()
    
