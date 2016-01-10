import speech_recognition as sr
import sys, os
from commands.open import openAppClassMac
from commands.add import addAppClassMac

r = sr.Recognizer()

class main:
    with sr.Microphone() as source:
        print("Speak your command: ")
        strCommand = r.recognize_google(r.listen(source)).lower()
        
    if "open" in strCommand:
        openAppClassMac.init(strCommand)

    elif "thanks" in strCommand:
        print("See you!")
        sys.exit()
        
