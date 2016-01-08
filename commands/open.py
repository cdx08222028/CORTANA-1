import os, sys

apps = open("applications.txt", "r+")

class openAppClassMac:
    def init(x):
        useProgram = ""
        for app in apps:
            if app in x:
                useProgram = app

        print(useProgram)
        
        if useProgram != "":
            os.system("open -a " + useProgram)
        else:
            print("Failure to open app!")
