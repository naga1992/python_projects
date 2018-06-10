# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 11:31:56 2018

@author: DS00331004
"""

import os

def rename_files(path):
    deletedigits = str.maketrans(dict.fromkeys("1234567890"))
    cdir=os.getcwd()
    os.chdir(path)
    print(cdir)
    list_files=os.listdir(path)
    for file_name in list_files:
        print("old file name"+file_name)
        print("new file name"+file_name.translate(deletedigits))
        os.rename(file_name,file_name.translate(deletedigits))
       
    os.chdir(cdir)
    
rename_files("D:\python projects\secret_message\prank\prank")    