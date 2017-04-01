# piate.py
#       A program to take text from a file .txt and convert it to pirate-speak
#       Input text can contain space, punctuations, numbers,lowercases and upercases.

def SeparateWords(inputfile):
    from re import *
    from sys import *

    infile = open(inputfile,'r')
    data = infile.read()
    infile.close()
    regex = compile('\w+|\W+')
    wordlist = regex.findall(data)
    return wordlist

def ReplaceWord(word):
    searchword = ["hello", "hi", "my", "friend", "sir", "miss", "stranger", "officer", "where", "is", "the", "you", "old", "happy", "nearby", "restroom", "restaurant", "hotel"]
    replaceword = ["ahoy", "ay-ho-ho", "me", "bucko", "matey", "proud beauty", "scurvy dog", "foul blaggart", "whar", "be", "th", "ye", "barnacle covered", "grog-filled", "broadside", "head", "galley", "fleabag inn"]
    for i in range (0,len(searchword)):
        if word == searchword [i]:
         word = replaceword[i]
    return word

def ConvertWord(word):
    newword = word.lower()
    newword = ReplaceWord(newword)
    if word[0].isupper():
        newword = newword[0].upper() + newword[1:]
    return newword

def main():
    from random import random
    print "This translator will convert a text to pirate-speak."
    # Get the text to convert
    inputfile=raw_input("Enter the file name containing the text: ")
    wordlist = SeparateWords(inputfile)
    
    #Convert text word by word
    ConText = ""
    for word in wordlist:
        word = ConvertWord(word)
        #Randomly insert Arr after the sentence
        if (word == ". ") or (word == "! ") or (word == "? "):
            if random() < 0.5:
                word = word + "Arr. "
        ConText = ConText + word

    #Print results
    print "Converted text: ", ConText

main()
