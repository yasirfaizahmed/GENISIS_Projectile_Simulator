from main import *

test_ball = Projectile_Object(30, 30, 3)

def test_get_xcor():
    assert (12.99 == test_ball.get_xcor(0.5))
    assert (10.392 == test_ball.get_xcor(0.4))
    assert (7.794 == test_ball.get_xcor(0.3))
    assert (0.0 == test_ball.get_xcor(0.0))

def test_get_ycor():
    assert (2.804 == test_ball.get_ycor(0.2))
    assert (4.059 == test_ball.get_ycor(0.3))
    assert (6.275 == test_ball.get_ycor(0.5))
    assert (1.451 == test_ball.get_ycor(0.1))
    
def test_get_xvel():
    assert (25.981 == test_ball.get_xvel())
    
def test_get_yvel():
    assert (13.04 == test_ball.get_yvel(0.2))
    assert (12.06 == test_ball.get_yvel(0.3))
    assert (10.1 == test_ball.get_yvel(0.5))
    assert (14.02 == test_ball.get_yvel(0.1))    
    
def test_flighttime():
    assert (3.061 == test_ball.get_flighttime())

def test_max_height():
    assert (11.48 == test_ball.max_height())
    
def test_range():
    assert (79.533 == test_ball.range())

test_list = [0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0]
def test_float_range():
    assert (test_list == list(float_range(0, 4, 0.2)))
       
       
