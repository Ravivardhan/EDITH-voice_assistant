import psutil
from plyer import notification
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


def batterys():
    battery=psutil.sensors_battery()

    percentage=battery.percent
    plugged=battery.power_plugged
    if percentage<20:
        SpeakText("sir ... your battery is below 20... i think you should charge the laptop")
    if percentage==100 and plugged==True:
        SpeakText("sir charging is full... you can unplug the charger")

