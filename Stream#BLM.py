# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 13:30:04 2020

@author: chrec
"""

import webbrowser
import time
from pynput.mouse import Button, Controller as MouseC
from pynput.keyboard import Key, Controller as KeyboardC
from timeit import default_timer as timer

keyboard = KeyboardC()
mouse = MouseC()
start = timer()
end = 0

while end - start < 3600:
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=bCgLa25fDHM")
    mouse.position = (775, 375)
    
    time.sleep(10)
    for i in range(10):
        keyboard.press(Key.up)
        keyboard.release(Key.up)
        time.sleep(1)
    time.sleep(5)
    for i in range(5):
        time.sleep(10)
        with keyboard.pressed(Key.shift):
            keyboard.press('n')
        keyboard.release('n')
        keyboard.release(Key.shift)
    with keyboard.pressed(Key.ctrl):
        keyboard.press('w')
    keyboard.release('w')
    keyboard.release(Key.ctrl)
    end = timer()
