import pyautogui as ag
import time
import pyttsx3


def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)
    engine.say(command)
    engine.runAndWait()


def pscd():

    txt=open(r"C:\Users\DELL\Desktop\passwords.txt")
    IID=[]
    lines=txt.readlines()
    print(lines)
    SpeakText(lines)
def get_info():
    time.sleep(3)
    ag.doubleClick(437,176)
    ag.doubleClick(326,199)
    time.sleep(12)
    ag.moveTo(587,417)
    ag.doubleClick(587,417)
    ag.hotkey('ctrl','c')
    ag.click(165,213)
    ag.hotkey('ctrl','v')
    time.sleep(2)
    ag.doubleClick(685,419)
    ag.hotkey('ctrl','c')
    ag.click(165,213)
    ag.hotkey('ctrl','v')
    time.sleep(2)
    ag.doubleClick(742,423)
    ag.hotkey('ctrl','c')
    ag.click(165,213)
    ag.hotkey('ctrl','v')

    ag.rightClick(165,213)
    ag.doubleClick(657,498)
    ag.hotkey('ctrl','c')

    ag.click(165,213)
    ag.press('enter')
    ag.hotkey('ctrl','v')

    ag.hotkey('ctrl','s')
    pscd()



