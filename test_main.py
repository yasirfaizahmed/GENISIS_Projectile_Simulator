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
    
