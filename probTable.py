#!/usr/bin/env python

import classifier

def createTable(features, vocab, probTable):
    # vector structure: [TT, TF, FT, FF]
    vocabSize = len(classifier.VOCABULARY)

    countTT = countTF = countFT = countFF = countT = countF = 0
    for x in range(0, vocabSize - 2):
        # counts for (word | CL) calculations
        for vector in features:
            # see if word is true
            if (vector[x] == 1):
                if (vector[vocabSize - 1] == 1):
                    countTT += 1
                    countT += 1
                else:
                    countTF += 1
                    countF += 1
            else:
                if (vector[vocabSize - 1] == 1):
                    countFT += 1
                    countT += 1
                else:
                    countFF += 1
                    countF += 1

    # calculate (word | CL) probabilities
    

    probTT = ()
    probVec = [countTT, countTF, countFT, countFF]


    
        