from PyDictionary import PyDictionary
import pyttsx3
dictionary=PyDictionary()
from threading import Thread


def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)
    engine.say(command)
    engine.runAndWait()


def meaning(word):
        values=dictionary.meaning(word).values()
        for i in values:
            for j in i:
                return j
def get():
    SpeakText(meaning("fuck"))
def gets():
    SpeakText(meaning("heros"))
if __name__ == '__main__':

    Thread(target=get()).start()
    Thread(target=gets()).run()
