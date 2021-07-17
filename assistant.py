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
from EDITH.study import want_to_read
from EDITH.wiki import ask_anything
from EDITH.fileExp import path
from EDITH.program import launch
from EDITH.e_news import today,newspaper
from EDITH.facebooks import facebook
from EDITH.minimize import all_down
from EDITH.autogui import refresh
from EDITH.windowExchange import change_windows
from EDITH.stackover import stack_overflow
from EDITH.sleep import sleep
import sys
from EDITH.battery_care import batterys
from EDITH.fake_details import get_fakes
from EDITH.meanings import meaning
from threading import Thread
from EDITH.minimize import maximize_java
from EDITH.minimize import minimize_java
from EDITH.access_to_ios import get_info
from EDITH.inevitable import iam_inevitable
from EDITH.facts import fact
def welcome():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-25)
    engine.say("hiii.. im ADITH your personal assistant")
    engine.runAndWait()
welcome()
batterys()


def speech_text():

    global MyText
    global command
    global MyText2
    # Initialize the recognizer
    r = sr.Recognizer()

    # Function to convert text to
    # speech
    def SpeakText(command):
        # Initialize the engine
        engine = pyttsx3.init()
        voices=engine.getProperty('voices')
        engine.setProperty('voice',voices[1].id)
        rate=engine.getProperty('rate')
        engine.setProperty('rate',rate-50)
        engine.say(command)
        engine.runAndWait()



        return None
        ###############################################################################################################3
    # Loop infinitely for user to
    # speak

    for i in range(100):
        # Exception handling to handle
        # exceptions at the runtime
        try:

            # use the microphone as source for input.
            with sr.Microphone() as source2:

                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                r.adjust_for_ambient_noise(source2, duration=0.2)

                # listens for the user's input
                audio2 = r.listen(source2)

                # Using ggogle to recognize audio

                speech_text.MyText = r.recognize_google(audio2)
                speech_text.MyText = speech_text.MyText.lower()

                print(speech_text.MyText)
                #SpeakText(speech_text.MyText)
 ########################__________WIKIPEDIA__________#################################################
                wikis=speech_text.MyText.split()
                if 'wikipedia' in wikis:
                    wiki=" "
                    for i in wikis[1:]:
                        wiki+=i
                    ask_anything(wiki)

###################################################################################____STUDY___##########
                if speech_text.MyText=="i want to study":
                    SpeakText("which subject sir")
                    for i in range(1):
                            audio3=r.listen(source2)
                            speech_text.MyText2=r.recognize_google(audio3)
                            speech_text.MyText2=speech_text.MyText2.lower()
                            want_to_read(speech_text.MyText2)

###############################################################################################################
                if 'open' in wikis:
                      file=""
                      for k in wikis[1:]:
                          file+=k
                      path(file)

                if 'launch' in wikis:

                    launch(wikis[-1])
                if  'fake' and 'details' in wikis:
                    get_fakes()
################################################################################################################
                if  'access' and 'to' and 'mobile' in wikis:
                    SpeakText("sure sir... im on my way....")
                    SpeakText("getting the id and password")
                    get_info()
                if 'bring' and 'me' and 'newspaper' in wikis:

                    SpeakText("bringing you today's newspaper...dont mind wait a second ")
                    today()
                if 'what' and 'can' and 'you' and 'do' in wikis:
                    SpeakText("i can  explore files ..........."
                              "launch applications................"
                              "open your subject pdfs..........."
                              "get information of your choice by wikipedia search..."
                              "bring newspaper..................."
                              "automate windows....................."
                              "goto sleep mode....................."
                              "solve errors in python............."
                              )

                if 'close' and 'all'  in wikis:

                    iam_inevitable()
                    
############################_________OPEN FACEBOOK __________________####################################################
                if 'open' and  'facebook' in wikis:
                    SpeakText("opening facebook........just........ wait a second")
                    facebook()
###############################_________MINIMIZE ALL #####################################################################
                if 'minimize' and 'all' and 'windows' in wikis:
                    SpeakText("minimizing all windows")
                    all_down()
################__________REFRESHIG           WINDOWS -__________________#######################################
                if 'refresh' and 'times' in wikis:
                    for i in wikis:
                        if i=="one":
                            times=1
                        if i=="two":
                            times=2
                        if i=="three":
                            times=3
                        if i=="four":
                            times=4
                    SpeakText("refreshing windows")
                    all_down()
                    refresh(times)
                if 'switch' and 'window' in wikis:
                     SpeakText("changing window")
                     change_windows()
                if 'f***' in wikis:
                    SpeakText("fuck off ...bitch")
                if 'give' and 'fact' in wikis:
                    SpeakText(fact())
                if 'got' and 'error' and 'python' in wikis:
                    SpeakText("sure sir.... can you tell me what type of error you got?")
                    for i in range(1):
                        audio5= r.listen(source2)
                        speech_text.MyText4 = r.recognize_google(audio5)
                        speech_text.MyText4 = speech_text.MyText4.lower()
                        error = speech_text.MyText4
                        SpeakText("getting the solution for error...... please wait for a moment... im working on it")
                        stack_overflow(error)
                if 'go' and 'sleep' in wikis:
                    SpeakText("going to sleep")
                    sleep()
                if 'good' and 'night' in wikis:
                    SpeakText("bye for noww... see you later sirrr")
                    sys.exit()
                if 'search' and 'dictionary' in wikis:
                    SpeakText("sure sir.... tell me the word")
                    for i in range(1):
                        audio6= r.listen(source2)
                        speech_text.MyText5 = r.recognize_google(audio6)
                        speech_text.MyText5 = speech_text.MyText5.lower()
                        word = speech_text.MyText5
                        print(meaning(word))
                        SpeakText(meaning(word))


        except sr.UnknownValueError:
            print("unknown error occured")
speech_text()
#########################################################################################################################
