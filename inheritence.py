# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 18:46:05 2018

@author: DS00331004
"""

class Parent():
    def __init__(self,last_name,eye_color):
        print("Calling Parent Class Constructor")
        self.last_name=last_name
        self.eye_color=eye_color
        
        
class Child(Parent):
    def __init__(self,last_name,eye_color,number_of_toys):
        print("Calling Child class Constructor")
        Parent.__init__(self,last_name,eye_color)
        self.number_of_toys=number_of_toys
           
        
suresh_jr=Child("donda","blue",600)
print(suresh_jr.number_of_toys)       