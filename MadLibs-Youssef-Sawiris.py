'''
Mad Libs by Youssef Sawiris

'''

a  = [] #list for Adjectives
n  = [] #list for Nouns
ad = [] #list for Adverbs
e  = [] #list for Exclamation


def putHead():
    print("\n")
    print("\u001b[36mWelcome to Youssef's Madlibs.")
    print("We have a very exciting story to tell you!")
    print("We need your help to finish it!")
    print("Please fill out the questionaire to hear our story!\u001b[0m")
    print("\n")


def getAdjective():
    #this fuction will collect adjectives from user
    a.append(input("Type in an adjective: "))
    a.append(input("Type in another adjective: "))
    a.append(input("Type in another adjective: "))
    a.append(input("Type in another adjective: "))

def getNoun():
    #this function will collect the nouns from user
    n.append(input("Type in a boy's  name: "))
    n.append(input("Type in a girl's name: "))
    n.append(input("Type in a name of place: "))


def getAdverb():
    #this fuction will collect adverbs from user
    ad.append(input("Type in an adverb: "))
    ad.append(input("Type in another adverb: "))

def getExclamation():
    #this function will collect Exclamation from user
    e.append(input("Type in a exclamation: "))

def putStory():
    print("\n")
    print(e[0], ", it started like any other day.")
    print(n[0],"called me right around 9 am, but this time they had")
    print(a[0], "news.", n[1], "was in a fight with their")
    print(a[1], "boyfriend. I", ad[0], "ran to my car and started")
    print("driving to", n[2], ". When I got there, I found out")
    print(n[0], "and", n[1], ad[1], "threw me a", a[2], "party!")
    print("Don't I have", a[3],"friends!")
    print("\u001b[33mLuckily they brought white claws!\u001b[0m")
    print("\n")

#calling fuctions
putHead()

getAdjective()

getNoun()

getAdverb()

getExclamation()

putStory()
