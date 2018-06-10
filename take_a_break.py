# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 10:53:21 2018

@author: DS00331004
to-do
1) open webbrowser
2) make porgram wait for sometime
3)make program repeat for sometime
"""

import webbrowser
import time

def take_a_break(number_of_times,break_for):
    ctr=0
    while(ctr<=number_of_times):
        time.sleep(break_for)
        webbrowser.open("https://www.youtube.com/watch?v=NTHz9ephYTw")
        ctr=ctr+1
    
    
take_a_break(3,10)    
