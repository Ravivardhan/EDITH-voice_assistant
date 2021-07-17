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





def get_notify():
    messagebox.showinfo('hello', 'enjoy your study sir....')




def want_to_read(subject):
    if subject == "mfcs":
        get_notify()
        os.startfile('E:\MFCS')

    elif subject =="algorithms":
        get_notify()
        os.startfile('E:\DAA')

    elif subject == 'dbms':
        get_notify()
        os.startfile('E:\DBMS')
    elif subject == 'java':
        get_notify()
        os.startfile('E:\java programs')
    else:
        messagebox.showinfo("not found","there is no source for the subject  {} in the files".format(subject))

