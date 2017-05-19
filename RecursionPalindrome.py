# RecursionPalindrome.py
# A program to take a single word in lowercase
# to check if this word is a palindrome
# using recursion.

def palindrome(word):
    if len(word) <= 1:
        return True
    else:
        if word[0] == word[len(word)-1]:
            return palindrome(word[1:len(word)-1])
        else:
            return False

def main():
    print('This program will check if a word is a palindrome.')
    word = input('Enter the word (lowercase): ')
    results = palindrome(word)
    print(results)

main()