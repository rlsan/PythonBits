#Generates sentences written in a completely made-up language.

import random

string = ""

consonants = ["a","e","i","o","u"]
vowels = ["b","p","d","g","h","f"]
punc = [".",",","!","?","???","!!!","!?"]

def addConsonant():
    rand = random.randint(0,len(consonants)-1)
    return consonants[rand]

def addVowel():
    rand = random.randint(0,len(vowels)-1)
    return vowels[rand]

def addPunc():
    rand = random.randint(0,len(punc)-1)
    return punc[rand]

def createWord():
    tempString = ""
    for x in range(0, random.randint(2,12)):
        if(x % 2 == 0):
            tempString += addVowel()
        else:
            tempString += addConsonant()
    return tempString

for x in range(0, 8):
    string += createWord()

    if(random.random() <= 0.4):
        string += addPunc()
    
    string += " "

print(string)
