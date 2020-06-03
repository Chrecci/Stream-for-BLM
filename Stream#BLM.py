# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 13:30:04 2020

@author: chrec
"""

#import
import webbrowser
import time
from pynput.mouse import Button, Controller as MouseC
from pynput.keyboard import Key, Controller as KeyboardC
from timeit import default_timer as timer
import random 

#sepearte Controller for keyboard and mouse
keyboard = KeyboardC()
mouse = MouseC()

#Start timer at 0 seconds
start = timer()
end = 0

while end - start < 40000:

    #Opens video in new tab, then centers mouse
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=bCgLa25fDHM")
    mouse.position = (775, 375)

    #the number of random videos watched is a random number between 3 and 5
    x = random.randint(3,5)
    time.sleep(10)

    #increases volume 10 times, 5% each time
    for i in range(10):
        keyboard.press(Key.up)
        keyboard.release(Key.up)
        time.sleep(1)
    
    #let sit for 65 mins, watches whole video + ads
    time.sleep(3900)

    #watch next few random videos
    for i in range(x):
        with keyboard.pressed(Key.shift):
            keyboard.press('n')
        keyboard.release('n')
        keyboard.release(Key.shift)
        time.sleep(10)
        
    #close tab
    with keyboard.pressed(Key.ctrl):
        keyboard.press('w')
    keyboard.release('w')
    keyboard.release(Key.ctrl)

    #cycle will repeat until 40,000 seconds has elapsed
    end = timer()
