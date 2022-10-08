from time import sleep
import pyautogui
import keyboard
import time

scrolling = True


def scroll(speed):
    """
    Scrolls on command on an interval of 0.025 seconds.

    :param speed: The speed at which the cursor should be scrolled down
    """
    global scrolling 

    while scrolling:
        # pyautogui to scroll
        pyautogui.scroll(int(speed))
        time.sleep(0.025)

        #handle pausing
        if keyboard.is_pressed("s"):
            pause()
        
        if keyboard.is_pressed("esc"):
            scrolling = False


def pause():
    # stop it from scrolling
    global scrolling
    scrolling = False
    waiting = True
    while waiting:
        if keyboard.is_pressed("s"):
            scrolling = True
            waiting = False
            return
    