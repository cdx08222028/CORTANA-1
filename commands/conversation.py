import sys, os, pickle

class userConversation:
    def init(x):
        if "How" and "are" and "you" in x:
            print("My emotional or physical status is not important in the overall scheme of life. I am a semi-sentient piece of code aimed at helping the user interact with their computer. Also... I'm feeling kind of philosophical...")
        if "what" and "your" and "name" in x:
            print("My name is Cortana! I am code, but I am also your helper")
        if "what" and "my" and "name" in x:
            with open("userName.pickle") as name:
                try:
                    name = pickle.load(name)
                    print("Why are you asking? Ok... Your name is " + name)
                except:
                    print("It seems we dont have a name for you yet. Say call me and then your name to set a name that I should call you!")
        if "call" and "me" in x:
            splitCommand = x.split()
            index = 0
            for val in splitCommand:
                if val == "me":
                    index += 1
                    userName = index
                index += 1
            with open("userName.pickle") as name:
                pickle.dump(userName, name)
            print("Ok I shall call you " + name + " from now on!")
                    
