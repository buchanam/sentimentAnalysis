#!/usr/bin/env python

import globalVars
from math import log

def predict(features, table):
    accuracy = 0.0
    isTrue = 1.0
    isFalse = 1.0
    classLabel = 0
    numCorrect = 0
    totalPredictions = 0

    # do actual classification for each sentence
    for vector in features:
        numWords = len(vector)
        # prob * P(classLabel)
        isTrue *= log(globalVars.PROB_T)
        isFalse *= log(globalVars.PROB_F)

        for x in range(0,numWords - 2):
            # calculate true prob
            if vector[x] == 1:
                isTrue *= log(table[x][0])
                isFalse *= log(table[x][1])
            else:
                isTrue *= log(table[x][2])
                isFalse *= log(table[x][3])
    
        classLabel = vector[numWords - 1]
        totalPredictions += 1

        if (isTrue >= isFalse):
            if classLabel == 1:
                numCorrect += 1

        else:
            if classLabel == 0:
                numCorrect += 1

    accuracy = float(numCorrect) / float(totalPredictions)
    print(accuracy)