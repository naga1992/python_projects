# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 12:10:59 2018

@author: DS00331004
"""

# drawing stuff using turtle
import turtle

def draw_a_square():
    # create a window for pinto to draw on
    window_for_pinto=turtle.Screen() 
    window_for_pinto.bgcolor('red')
    
    pinto=turtle.Turtle()
    pinto.shape("turtle")
    pinto.color("blue")
    pinto.speed(2)
    pinto.forward(100)
    pinto.right(90)
    pinto.forward(100)
    pinto.right(90)
    pinto.forward(100)
    pinto.right(90)
    pinto.forward(100)
    pinto.right(90)
    
    
    pinter=turtle.Turtle()
    pinter.shape('arrow')
    pinter.color('red')
    
    pinter.circle(100)
    turtle.done()
    window_for_pinto.exitonclick()
    
    
    
draw_a_square()   
    