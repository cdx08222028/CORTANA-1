import speech_recognition as sr
import sys, os
from commands.open import openAppClassMac
from commands.add import addAppClassMac

r = sr.Recognizer()
mic = sr.Microphone()

class main:
    with mic as source:
        print("Speak your command: ")
        audioCommand = r.listen(source)
        strCommand = r.recognize_google(audioCommand)
        print(strCommand)
    if "open" in strCommand:
        openAppClassMac.init(strCommand)
    elif "add" in strCommand:
        addAppClassMac.init(strCommand)
