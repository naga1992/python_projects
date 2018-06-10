# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 12:10:59 2018

@author: DS00331004
"""

# drawing stuff using turtle
import turtle

def draw_a_sqauare(turtle_instance):
    for i in range(1,5):
        turtle_instance.forward(100)
        turtle_instance.right(90)

def draw_art():
    # create a window for pinto to draw on
    window_for_pinto=turtle.Screen()
    window_for_pinto.bgcolor('red')
    
    pinto=turtle.Turtle()
    pinto.shape("turtle")
    pinto.color("blue")
    for i in range(1,37):
        draw_a_sqauare(pinto)
        pinto.right(10)
    turtle.done()
    window_for_pinto.exitonclick()
    
    
    
draw_art()   
    