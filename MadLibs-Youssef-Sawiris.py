'''
Mad Libs by Youssef Sawiris

'''

a  = [] #list for Adjectives
n  = [] #list for Nouns
ad = [] #list for Adverbs

def getAdjective():
    a.append(input("Type in an adjective: "))
    a.append(input("Type in an adjective 1: "))
    a.append(input("Type in an adjective 2: "))
    a.append(input("Type in an adjective 3: "))

def getNoun():
    n.append(input("Type in an noun: "))
    n.append(input("Type in an noun 1: "))
    n.append(input("Type in an noun 2: "))

def getAdverb():
    ad.append(input("Type in an adverb: "))
    ad.append(input("Type in an adverb1: "))

getAdjective()
getNoun()
getAdverb()

print(a[0])
