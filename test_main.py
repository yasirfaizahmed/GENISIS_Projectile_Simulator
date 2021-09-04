from main import *

test_ball = Projectile_Object(30, 30, 3)

def test_get_xcor():
    assert (12.99 == test_ball.get_xcor(0.5))
    assert (10.392 == test_ball.get_xcor(0.4))
    assert (7.794 == test_ball.get_xcor(0.3))
    assert (0.0 == test_ball.get_xcor(0.0))

def test_get_ycor():
    assert (2.925 == test_ball.get_ycor(0.2))
    assert (4.331 == test_ball.get_ycor(0.3))
    assert (7.031 == test_ball.get_ycor(0.5))
    assert (1.481 == test_ball.get_ycor(0.1))
    
def test_get_xvel():
    assert (25.981 == test_ball.get_xvel())
    
def test_get_yvel():
    assert (14.25 == test_ball.get_yvel(0.2))
    assert (13.5 == test_ball.get_yvel(0.4))
    assert (13.875 == test_ball.get_yvel(0.3))
    assert (14.625 == test_ball.get_yvel(0.1))    
    
def test_flighttime():
    assert (8.0 == test_ball.get_flighttime())

def test_max_height():
    assert (30.0 == test_ball.max_height())
    
def test_range():
    assert (207.846 == test_ball.range())

test_list = [0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0]
def test_float_range():
    assert (test_list == list(float_range(0, 4, 0.2)))
       