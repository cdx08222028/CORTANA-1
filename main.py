import speech_recognition as sr
import sys, os

r = sr.Recognizer()
mic = sr.Microphone()

class main:
    with mic as source:
        print("Speak your command")
        audioCommand = r.listen(source)

    try:
        print(r.recognize_google(audioCommand))
    except:
        print("Error occured in processing audio, please try again!")
        sys.exit()
