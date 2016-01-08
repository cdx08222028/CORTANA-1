import os, sys

apps = open("applications.txt", "a")

class addAppClassMac:
    def init(x):
        words = x.split()
        currentApps = []
        for val in words:
            for file in os.listdir("/Applications"):
                if file == val + ".app":
                    print("Adding")
                    apps.write(val + "\n")
                    
