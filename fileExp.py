import os
import pyttsx3
import pyautogui


def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)
    engine.say(command)
    engine.runAndWait()


def path(doc_name):
    if doc_name=='file':
        SpeakText("opening file explorer")
        pyautogui.moveTo(582,1048)
        pyautogui.click()
    if doc_name=='desktop':
        SpeakText("opening desktop file")
        os.startfile(r'C:\Users\DELL\Desktop')
    if doc_name=='downloads':
        SpeakText("opening downloads file")
        os.startfile(r'C:\Users\DELL\Downloads')
    if doc_name=='Pictures':
        SpeakText("opening pictures file")
        os.startfile(r'C:\Users\DELL\Pictures')
    if doc_name=='music':
        SpeakText("opening music file")
        os.startfile(r'C:\Users\DELL\Music')
    if doc_name=='videos':
        SpeakText("opening videos file")
        os.startfile(r'C:\Users\DELL\Videos')
    if doc_name=='marriage':
        SpeakText("playing sisters marriage video")
        os.startfile(r'C:\Users\DELL\Videos\a title.mp4')