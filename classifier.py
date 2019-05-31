#!/usr/bin/env python

import string

# global variables
vocabulary = []

# strips puncuation and case from vocabulary words
def cleanWord(word):
    # all lower case
    word = word.lower()
    # punctuation removal
    word = word.translate(None, "?.()[]!,'-:")

    return word


def preprocessing():
    # open files
    trainF = open("trainingSet.txt", "r")
    testF = open("testSet.txt", "r")

    global vocabulary
    # create training data vocabulary
    for line in trainF:
        for word in line.split():
            word = cleanWord(word)
            print(word)
            # if word not number
            if not (isinstance(word, int)):
                vocabulary.append(word)

    # sort vocabulary alphabetically
    vocabulary = sorted(vocabulary)

    



# driver code
preprocessing()