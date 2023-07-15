from pynput.keyboard import Key, Controller
keyboard = Controller()
from pynput.mouse import Button, Controller
mouse = Controller()
import time

reps = input('How many times?')
reps = int(reps)
time.sleep(5)
x = 0
for x in range(0,reps):
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release(Key.ctrl)
    keyboard.release('c')

    time.sleep(1)

    keyboard.press(Key.ctrl)
    keyboard.press(Key.tab)
    keyboard.release(Key.ctrl)
    keyboard.release(Key.tab)

    time.sleep(1)

    keyboard.press(Key.ctrl)
    keyboard.press('v')
    keyboard.release(Key.ctrl)
    keyboard.release('v')

    time.sleep(1)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    
    time.sleep(1)

    keyboard.press(Key.ctrl)
    keyboard.press(Key.tab)
    keyboard.release(Key.ctrl)
    keyboard.release(Key.tab)

    time.sleep(1)

    keyboard.press(Key.down)
    keyboard.release(Key.down)

    time.sleep(1)





    
