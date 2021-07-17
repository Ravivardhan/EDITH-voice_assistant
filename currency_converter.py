from forex_python.converter import *
import pyttsx3
c=CurrencyRates()
import speech_recognition as sr

def convert(From,To,amount):
    converted=c.convert(From,To,amount)
    print("%.2f"%(converted))


def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)
    engine.say(command)
    engine.runAndWait()


def verify():
    global MyText
    global MyText2
    r = sr.Recognizer()
    try:
        # use the microphone as source for input.
        SpeakText("can you tell me from which currency i have to convert")

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
            if MyText == "american dollars" or "american dollar":
                MyText="USD"
            elif MyText == "indian currency":
                MyText="INR"
            print(MyText)
            SpeakText("to which currency type")
            audio3 = r.listen(source2)

            # Using ggogle to recognize audio

            MyText2 = r.recognize_google(audio3)
            MyText2 = MyText2.lower()
            if MyText2 == "indian currency":
                MyText2="INR"
            elif MyText2=="american dollars" or "american dollar":
                MyText2= "USD"

            print(MyText2)
            SpeakText("how much dollars sir")
            capacity=int(input("enter how much dollars"))
            print(convert(MyText,MyText2,capacity))
    except sr.UnknownValueError:
        print("unknown error occured")



verify()