# Problem Set 5: Ghost
# Name: 
# Collaborators: 
# Time: 
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

def ghost():
    gameFinished = False
    print 'Welcome to Ghost!'
    print 'Player 1 goes first.'

    word_fragment = ''
    numCalls = 0
    player_num = 1

    while not gameFinished:
        numCalls += 1
        if numCalls % 2 != 0: #player 1 is playing
            player_num = 1
            other_player = 2
        else:
            player_num = 2
            other_player = 1
        print 'Current word fragment:', word_fragment
        print 'Player ' + str(player_num) + '"s turn.'
        letter = raw_input('Player ' + str(player_num) + ' says letter: ')
        assert (letter in string.ascii_letters), 'please enter a character value'
        # print
        letter = letter.lower()
        # print 'Player', player_num, 'says letter:', letter 
        word_fragment += letter
        # print 'current word fragment:', word_fragment
        #check if current word fragment will become a word
        if all(word_fragment not in word for word in wordlist):
            print 'Current word fragment: ' + word_fragment
            print 'Player ' + str(player_num) + ' loses because no word can be formed from ' + word_fragment
            print 'Player ' + str(other_player) + ' wins'
            gameFinished = True
            break
        if len(word_fragment) > 3:
            if word_fragment in wordlist:
                print 'Current word fragment: ' + word_fragment
                print 'Player ' + str(player_num) + ' loses because ' + word_fragment + ' is a word!'
                print 'Player ' + str(other_player) + ' wins'
                gameFinished = True
                break

    



