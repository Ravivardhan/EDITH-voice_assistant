import pyttsx3
import os
import pyautogui as ag
import time
import speech_recognition as sr


def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)
    engine.say(command)
    engine.runAndWait()


def launch(application):
    if application=="whatsapp":
        SpeakText("opening watsapp")
        ag.doubleClick(1280,1069)
    if application=="firefox":
        SpeakText("launching firefox browser")
        os.startfile(r"C:\Program Files\Mozilla Firefox\firefox.exe")
    if application=='edge':
        SpeakText("launching microsoft edge")
        os.startfile(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
    if application=='python':
        SpeakText("launching pycharm")
        os.startfile(r"C:\Program Files\JetBrains\PyCharm Community Edition 2020.1.3\bin\pycharm64.exe")
    if application=='java':
        SpeakText("launching intellij")
        os.startfile(r"C:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2020.3.1\bin\idea64.exe")
    if application=='files':
        SpeakText("launching file explorer")
        os.startfile(r"C:")

