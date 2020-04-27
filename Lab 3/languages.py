#!/usr/bin/python
# -*- coding: utf-8 -*-
from sys import *
global consonants
global vowels
global uppercase

#Definition av vokaler och konsonanter
consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
vowels = "aeiouyåäöAEIOUYÅÄÖ"
uppercase = "BCDFGHJKLMNPQRSTVWXZAEIOUYÅÄÖ"

#Viskspråket
def whisper_convert(regular):
    whisper = regular
    for letter in regular:
        if letter in vowels:
            whisper = whisper.replace(letter, "")
    return whisper

#Rövarspråket
#Översätt svenska till sjörövarspråk
def robbers_convert(regular):
    robber = ""
    for word in regular:
        if word.lower() in consonants:
            robber = robber + word + "o" + word.lower()
        else:
            robber = robber + word
    return robber

#Översätt sjörövarspråk till svenska
def translate_robbers(robbers):
    regular = ""
    i = 0
    while i < len(robbers):
        if (robbers[i].lower() not in consonants):            
            regular +=robbers[i]
            i += 1
        else:      
            if  ((i + 2) < len(robbers)):
                if (robbers[i+1] == 'o'):
                    if (robbers[i+2].lower() == robbers[i].lower()): 
                        regular += robbers[i]
                        i += 3
            else:
                regular = "Error"
                break 
    return regular

#Bebisspråket
def baby_convert(regular):
    words = regular.split()
    baby = ""
    for word in words:          
        baby += (first_syllableB(word)
                 + 2* first_syllableB(word).lower() + " ")
    return (baby + "\n")

def first_syllableB(word):
    count = 0
    for letter in word:
        count += 1
        if letter in vowels:
            break
    return word[:count]

#Returnerar ??? istället för åäö vid utskrift i Bash
#åäö returneras som vanligt i IDLE

#Allspråket
def all_convert(regular):
    words = regular.split()
    all_ = ""
    for word in words:
        all_ += ((word.replace(word[0], ""))
                 + first_syllable(word).lower() + "all" + " ")  
    return (all_ + "\n") 

#Fikonspråket
def fig_convert(regular):
    words = regular.split()
    fig = ""
    for word in words:
        fig += ("fi" + word.replace(first_syllable(word), "")
                + first_syllable(word).lower() + "kon" + " ")
    return (fig + "\n")

def first_syllable(word):
    count = 0 
    for letter in word:
        count += 1
        if letter in vowels:
            break
    return word[:count-1]

#Körning
#Körs på Bash med ex. kommandot: echo "Landkrabborna försöker sänka oss med kanoner" |./languages.py -r 
def main():
    argument = ("".join(argv[1:]))
    text = stdin.readline()
    # -w: Viskspråket, -r: Rövarspråket, -tr: Översätt Rövarspråk 
    # -b: Bebisspråket, -a Allspråket, -f: Fikonspråket
    options = {"-w": whisper_convert(text), "-r": robbers_convert(text),
               "-tr": translate_robbers(text), "-b": baby_convert(text),
               "-a": all_convert(text), "-f": fig_convert(text)}
    output = options[argument]
    print(output) 

if __name__ == "__main__":
    main()
