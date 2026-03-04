import pyttsx3
import speech_recognition as sr

def speechtxt(x):
    engine=pyttsx3.init()
    voices = engine.getProperty('voices')#here this get the voice from the engine.
    engine.setProperty('voice',voices[0].id)#here its set the voice and 0 is for male voice and 1 is for female voice.
    rate =  engine.getProperty('rate')#here get the 'rate' form the eniginee for the speed of the voice.
    engine.setProperty('rate',140)#ste the speet of the voiec.
    engine.say(x)#for speaking the text using the x variable.
    engine.runAndWait()
speechtxt("Nice to Meeting You")