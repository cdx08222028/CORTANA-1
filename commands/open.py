import os, sys

class openAppClassMac:
    def init(x):
        useProgram = ""
        for file in os.listdir("/Applications"):
            splitFile = os.path.splitext(file)[0].lower()
            if splitFile in x:
                useProgram = splitFile
                os.system("open -a " + useProgram)
