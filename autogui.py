import pyautogui as ag
import time

def refresh(n):
   for i in range(n):
        ag.moveTo(490,300)
        time.sleep(1)
        ag.rightClick()
        time.sleep(1)
        ag.click(533,381)
time.sleep(4)


