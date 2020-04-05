# Problem Set 5: Ghost
# Name: Majid Roohi 
# Collaborators: Majid Roohi
# Time: 14:13
#

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

# TO DO: your code begins here!

def ghost() :

    word = ''
    CHECK = True

    print '\nWelcome to Ghost!'
    print 'Player 1 goes first.'
    print 'Current word fragment:' , word
    
    p_1 = raw_input('Player 1 says letter: ')

    if p_1 in string.ascii_letters :

        p_1 = string.upper(p_1)
        word += p_1

        while CHECK == True :

            print '\nCurrent word fragment:' , word
            print "Players 2's turn."

            p_2 = raw_input('Player 2 says letter: ')

            if p_2 in string.ascii_letters :

                p_2 = string.upper(p_2)
                word += p_2
                        
            else :

                print 'Player 2 loses because input not a alphabetic character!'

                return

            check = False
            Word = string.lower(word)
            
            if len(word) > 2 :

                for i in wordlist :

                    if i == Word :

                        print '\nCurrent word fragment:' , word
                        print "Player 2 losses because '" , word , "' is a word!"
                        print 'Player 1 wins!'

                        return
                    
                    elif i[0:len(word)] == Word : check = True

                if check == False :

                    print '\nCurrent word fragment:' , word
                    print "Player 2 losses because no word begins with'" , word , "'"
                    print 'Player 1 wins!'

                    return

            print '\nCurrent word fragment:' , word
            print "Players 1's turn."
            
            p_1 = raw_input('Player 1 says letter: ')

            if p_1 in string.ascii_letters :

                p_1 = string.upper(p_1)
                word += p_1

            else :

                print 'Player 1 loses because input not a alphabetic character!'

                return

            check = False
            Word = string.lower(word)

            if len(word) > 2 :

                for i in wordlist :

                    if i == Word :

                        print '\nCurrent word fragment:' , word
                        print "Player 1 losses because '" , word , "' is a word!"
                        print 'Player 2 wins!'

                        return
                    
                    elif i[0:len(word)] == Word : check = True

                if check == False :

                    print '\nCurrent word fragment:' , word
                    print "Player 1 losses because no word begins with'" , word , "'"
                    print 'Player 2 wins!'

                    return

    else : print 'Player 1 loses because input not a alphabetic character!'

