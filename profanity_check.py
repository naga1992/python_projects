# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 17:06:43 2018

@author: DS00331004
"""
import urllib 

def read_text(path):
    file_content=open(path)
    fcon=file_content.read()
    file_content.close()
    profanity_check(fcon)
 
def profanity_check(text_tobe_checked):
    req = urllib.request.Request('http://www.wdylike.appspot.com/?q='+text_tobe_checked)
    resp=urllib.request.urlopen(req)
    print(resp.read())
    
 
profanity_check("shit")