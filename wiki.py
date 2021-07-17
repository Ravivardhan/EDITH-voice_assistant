
from gtts import gTTS
import tkinter
from tkinter import *
import os
from tkinter import messagebox
import wikipedia
import pyttsx3
import speech_recognition as sr
import gtts
from playsound import playsound


def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)
    engine.say(command)
    engine.runAndWait()


def ask_anything(subject):
    ######################################################################################

    wiki_window = tkinter.Tk()

    wiki_search = wikipedia.summary(subject,sentences=4)

    wiki_lable = Label(wiki_window, text=wiki_search).grid()

    wiki_window.mainloop()
    SpeakText(wiki_search)