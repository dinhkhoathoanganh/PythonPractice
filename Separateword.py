# Read text from a file, separating out each word and "run" of
# punctuation and spacing as separate items.

# This contains "advanced" code for the benefit of anyone who wants to
# have fun with it, but not part of expected knowledge for CS 111.

# Written by Dave Musicant.

from re import *
from sys import *

infile = open('source.txt','r')
data = infile.read()
infile.close()
regex = compile('\w+|\W+')
print regex.findall(data)
# for word in regex.findall(data):
#     stdout.write(word)

# I use stdout.write above instead of print here because print
# automatically puts a space after each word. That's a problem in this
# case, because the spaces that are already present between words are
# read as separate words and automatically printed.