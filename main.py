import speech_recognition as sr
import sys, os, platform, pickle
from commands.open import *
from commands.weather import *
from commands.conversation import *

r = sr.Recognizer()

try:
    name = pickle.load(open( "userName.p", "rb" ))
    print("Hey there " + name + ", what's up?")
except:
    print("Hey there! What's up?")
class main:
    waitingForVal = 1
    while True:
            try:
                with sr.Microphone() as source:
                    strCommand = r.recognize_google(r.listen(source)).lower()
                    print(strCommand)
                    waitingForVal = 0
            except:
                waitingForVal = 1
                
            if waitingForVal != 1:
                if platform.system() == "Darwin":
                    openAppClassMac.init(strCommand)
                    weatherClass.init(strCommand)
                    userConversation.init(strCommand)

                if platform.system() == "Windows":
                    userConversation.init(strCommand)
                    weatherClass.init(strCommand)

                if "bye" in strCommand or "see you" in strCommand:
                    print("See you!")
                    sys.exit()
