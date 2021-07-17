import datetime
import pyttsx3
import speech_recognition as sr

global MyText

def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)
    engine.say(command)
    engine.runAndWait()

def add_task():
    try:
        r = sr.Recognizer()
        SpeakText("whats the task should i add sir")
        # use the microphone as source for input.
        with sr.Microphone() as source2:
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)

            # listens for the user's input
            audio2 = r.listen(source2)

            # Using ggogle to recognize audio
            file1 = open(r"C:\Users\DELL\Desktop\tasks.txt", "w")

            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print(MyText)
            file1.write(MyText)
            SpeakText("successsfully added a new task")
            get_tasks()
    except sr.UnknownValueError:
        print("unknown error occured")

def get_tasks():
    file2 = open(r"C:\Users\DELL\Desktop\tasks.txt")
    tasks=file2.readlines()
    for i in tasks:
        print(i)
        SpeakText(i)

def confirm():
    try:
        r = sr.Recognizer()

        # use the microphone as source for input.
        with sr.Microphone() as source2:
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)

            # listens for the user's input
            audio2 = r.listen(source2)

            # Using ggogle to recognize audio

            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print(MyText)
            if 'add' and 'task' in MyText:
                add_task()
    except sr.UnknownValueError:
        print("unknown error occured")




def ask():
    SpeakText("do you want to add a task")
def progress(date):


    global MyText
    global command
    global MyText2
    # Initialize the recognizer
    r = sr.Recognizer()
    for i in range(1):
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

                # Using ggogle to recognize audio



                if date=='6':
                    SpeakText("sir.... you dont have any progress or plans today")
                    ask()
                    confirm()



                if date=='7':
                    SpeakText("you have to complete design and analysis of algoriths unit 1 and unit2 today")

                    ask()
                    confirm()

                if date=='8':
                    SpeakText("you have to complete design and analysis of algorithms unit3 and unit4 today")

                    ask()
                    confirm()

                if date=='9':
                    SpeakText("you have to complete MFCS unit 1 and unit 2")

                    ask()
                    confirm()

                if date=='10':
                    SpeakText("you have to complete MFCS unit 3 and unit 4")

                    ask()
                    confirm()

                if date=='11':
                    SpeakText("you have to complete digital logic design unit 1 and unit2")

                    ask()
                    confirm()

                if date=='12':
                    SpeakText("you have to complete digital logic design unit3 and unit4")

                    ask()
                    confirm()

                if date=='13':
                    SpeakText("you have to comlete python all units today")
                    ask()
                    confirm()

     except sr.UnknownValueError:
                print("unknown error occured")

progress('7')