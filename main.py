import speech_recognition as sr
import sys, os
from commands.open import openAppClassMac
from commands.weather import weatherClassMac
from commands.conversation import userConversation

r = sr.Recognizer()

class main:
    while True:
        with sr.Microphone() as source:
            print("Speak your command: ")
            strCommand = r.recognize_google(r.listen(source)).lower()
            print(strCommand)

            if platform.system() == "Darwin":
                openAppClassMac.init(strCommand)
                weatherClassMac.init(strCommand)
                userConversation.init(strCommand)

            if platform.system() = "Windows":
                #Windows Classes go here when Jake actually makes any :P

        if "thanks" and "see" and "you" in strCommand:
            print("See you!")
            sys.exit()
