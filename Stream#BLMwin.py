# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 13:30:04 2020

@author: chrec
"""

#import
import webbrowser
import time
import pyautogui as pyg
from timeit import default_timer as timer
import random 

#gets middle of the screen pixel
position_y = (pyg.size()[1])/2
position_x = (pyg.size()[0])/2

#Start timer at 0 seconds
start = timer()
end = 0

while end - start < 40000:

    #Opens video in new tab, then centers mouse
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=bCgLa25fDHM")
    pyg.moveTo(position_x, position_y)

    #the number of random videos watched is a random number between 3 and 5
    x = random.randint(3,5)
    time.sleep(10)

    #increases volume 10 times, 5% each time
    for i in range(10):
        pyg.press('up')
        time.sleep(1)
    
    #let sit for 65 mins, watches whole video + ads
    time.sleep(3900)
    print(x)
    #watch next few random videos
    for i in range(x):
        pyg.keyDown('shift')
        pyg.press('n')
        pyg.keyUp('shift')
        time.sleep(10)
        
    #close tab
    pyg.keyDown('ctrl')
    pyg.press('w')
    pyg.keyUp('ctrl')

    #cycle will repeat until 40,000 seconds has elapsed
    end = timer()