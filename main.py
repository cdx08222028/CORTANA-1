import speech_recognition as sr
import sys, os
from commands.open import openAppClassMac
from commands.weather import weatherClassMac

r = sr.Recognizer()

class main:
    while True:
        with sr.Microphone() as source:
            print("Speak your command: ")
            strCommand = r.recognize_google(r.listen(source)).lower()
            print(strCommand)
            
        if "open" in strCommand:
            openAppClassMac.init(strCommand)

        if "weather" in strCommand:
            weatherClassMac.init(strCommand)

        if "thanks" in strCommand:
            print("See you!")
            sys.exit()
