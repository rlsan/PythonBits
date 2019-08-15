#Returns the written input as a series of "regional indicator" emojis. Created to annoy people on Discord with giant messages.

phrase = input()

phrase = phrase.lower()

prefix = ":regional_indicator_"
suffix = ": "

total = ""

def makeEmoji(letter):
    return prefix + letter + suffix

for x in phrase:
    if x == " ":
        total += "         "
    elif x == "0":
        total += ":zero: "
    elif x == "1":
        total += ":one: "
    elif x == "2":
        total += ":two: "
    elif x == "3":
        total += ":three: "
    elif x == "4":
        total += ":four: "
    elif x == "5":
        total += ":five: "
    elif x == "6":
        total += ":six: "
    elif x == "7":
        total += ":seven: "
    elif x == "8":
        total += ":eight: "
    elif x == "9":
        total += ":nine: "
    elif x == "?":
        total += ":question:"
    elif x == "!":
        total += ":exclamation:"
    elif x == ".":
        total += ":wah:"
    elif x == ",":
        total += ":wah:"
    else:
        total += makeEmoji(x)
    
print(total)
