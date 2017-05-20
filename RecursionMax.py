# RecursionMax.py
# A program to take a list of numbers, separated by space, from a file .txt and find the maximum number
# using recursion.

def SeparateNum(inputfile):    
    infile = open(inputfile,'r')
    data = infile.read()
    infile.close()
    return data.split()

def FindMax(numlist):
    if len(numlist) == 1:
        return int(numlist[0])
    elif len(numlist) == 0:
        print('Emptylist!')
        quit()
    else:
        maxnum = FindMax(numlist[1:])
        if maxnum > int(numlist[0]):
            return maxnum 
        else:
            return int(numlist[0])

def main():
    print('This program will find your maximum number.')
    # Get the list
    inputfile = input('Enter the file name containing the number list: ')
    numlist = SeparateNum(inputfile)

    #Find max
    maxnum = FindMax(numlist)

    #Print results
    print('Maximum number:', maxnum)

main() 
