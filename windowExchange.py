import pyautogui as pg
import time
def change_windows():
    pg.hotkey('alt','tab')

def custom():
    pg.keyDown('alt','tab')
    pg.keyUp('tab')
    time.sleep(6)

