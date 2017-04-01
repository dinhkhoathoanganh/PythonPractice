# Double-Caesar.py
#       A program to encode and decode a textual message using one Key Text
#       Input text is entirely in lower case, with no punctuation

def code(text, key, mode):
    import math
    # Create string of key with the same length as text
    if len(text) >= len(key): 
        copy = int(math.ceil(float(len(text))/float(len(key))))
        newkey = key * copy 
        newkey = newkey[:len(text)]
    else:
        newkey = key[:len(text)]
    #Convert key, newtext to lists of ACSII numbers
    textls = [ord(c) for c in text]
    keyls = [ord(c) for c in newkey]
    textls = list(map(int, textls))
    # print textls
    keyls = list(map(int, keyls))
    # Convert keyls to a list of number that indicates the number of shifting
    for i in range(0,len(keyls)):
        if (keyls[i] <= 57) and (keyls[i] >= 48):       #if key character is a number
            keyls[i] = keyls[i] - 48
        elif (keyls[i] <= 90) and (keyls[i] >= 65):     #if key character is a Upercase
            keyls[i] = keyls[i] - 65
        elif (keyls[i] <= 122) and (keyls[i] >= 97):    #if key character is a Lowercase
            keyls[i] = keyls[i] - 97
        else:
            print "Key should not have special characters!!"
            quit()
    if mode < 0:
        keyls = [ -x for x in keyls]
    #print keyls
    #En/Deconde the message
    entext = [textls[i]+keyls[i] for i in range(len(textls))]
    for i in range(len(entext)):
        while (entext[i] > 122):
            entext[i] -=26
        while (entext[i] < 97):
            entext[i] +=26
        entext[i] = chr(entext[i])
    answer= ''.join(entext)
    return answer
        


def main():
    print "This is Double-Caesar Cipher"
    # Get the message to encode/decode
    inputfile=raw_input("Enter the file name containing code and key: ")
    infile = open(inputfile, 'r')
    lines = infile.readlines()
    print lines
    text = ""
    for i in range(len(lines)-1):
        text += lines[i]
    print text
    key = lines[len(lines)-1]
    print key
    message = raw_input("Do you want to encode or decode? ")
    if message[0] == "e": #Encode function
        print "You have chosen ENCODE."
        answer = code(text, key, 1)
    elif message[0] == "d": #Decode function
        print "You have chosen DECODE."
        answer = code(text, key, -1)
    else:
        print "Invalid input! Program has ended!."
        quit()
    #Print the en/decoded message
    print "Your encoded message:", answer


main()
