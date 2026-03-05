import pyttsx3
import speech_recognition as sr

def speechtxt(x):
    engine=pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate =  engine.getProperty('rate')
    engine.setProperty('rate',140)
    engine.say(x)
    engine.runAndWait()
speechtxt("Nice to Meeting You")