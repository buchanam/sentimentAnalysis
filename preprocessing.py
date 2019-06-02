#!/usr/bin/env python

import globalVars 

# strips puncuation and case from globalVars.VOCABULARY words
def cleanWord(word):
    # all lower case
    word = word.lower()
    # punctuation removal
    word = word.translate(None, "%+\,$&*?.()[]!'-:")

    return word
    
def convertToFeatures(file, fileName, features):
    newFile = open(fileName, "w")

    # first header line
    for word in globalVars.VOCABULARY:
        newFile.write(word + ",")
    newFile.write("classlabel\n")

    # convert sentences to features
    # create list of words in sentence
    for nextLine in file:
        lineWordList = []
        classLabel = nextLine[-4:]
        classLabel = int(classLabel)
        for word in nextLine[:-4].split():
            word = cleanWord(word)
            if not (word.isdigit() or word is None):
                lineWordList.append(word)
        lineWordList = sorted(lineWordList)

        # ~ appended so there is a sentence done symbol which won't match any word in vocab
        lineWordList.append("~")

        sentenceVector = []
        for x in range(0,globalVars.V_LENGTH - 1):
            if (lineWordList[0] == globalVars.VOCABULARY[x]):
                newFile.write("1,")
                sentenceVector.append(1)
                lineWordList.pop(0)
            else:
                newFile.write("0,")
                sentenceVector.append(0)

        newFile.write(str(classLabel))
        sentenceVector.append(classLabel)
        newFile.write("\n")    
        features.append(sentenceVector)

# preprocessing steps: clean words, create vocab, convert to features
def processingDriver(trainingFile, testingFile, trainFeatures, testFeatures):
    # open files
    trainF = open(trainingFile, "r")
    testF = open(testingFile, "r")

    
    # create training data globalVars.VOCABULARY
    for line in trainF:
        for word in line.split():
            word = cleanWord(word)
            # if word not number
            if not (word.isdigit() or word in globalVars.VOCABULARY or word is None):
                globalVars.VOCABULARY.append(word)

    trainF.close()
    trainF = open("trainingSet.txt", "r")
    # sort globalVars.VOCABULARY alphabetically
    globalVars.VOCABULARY = sorted(globalVars.VOCABULARY)
    globalVars.VOCABULARY.pop(0)
    
    globalVars.V_LENGTH = len(globalVars.VOCABULARY)

    convertToFeatures(trainF, "preprocessed_train.txt", trainFeatures)
    convertToFeatures(testF, "preprocessed_test.txt", testFeatures)

