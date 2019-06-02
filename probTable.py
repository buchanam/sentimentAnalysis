#!/usr/bin/env python

import globalVars

def checkUDP(countTT, countTF, countFT, countFF, countT, countF):
    if countTT == 0:
        countTT = (countTT + 1) / (countT + 2)
    if countTF == 0:
        countTF = (countTF + 1) / (countF + 2)
    if countFT == 0:
        countFT = (countFT + 1) / (countT + 2)
    if countFF == 0:
        countFF = (countFF + 1) / (countF + 2)

    return countTT, countTF, countFT, countFF, countT, countF

def createTable(features, probTable):
    # vector structure: [TT, TF, FT, FF]

    # THIS MIGHT CAUSE PROBLEMS


    # count classLabel trues and falses
    print("Processing probabilities for:")
    for x in range(0, globalVars.V_LENGTH ):
        print("\t" + str(globalVars.VOCABULARY[x]))
        countTT = countTF = countFT = countFF = countT = countF = 0.0
        # counts for (word | CL) calculations
        for vector in features:
            if (vector[x] == 1):
                if (vector[globalVars.V_LENGTH - 1] == 1):
                    countTT += 1.0
                    countT += 1.0
                else:
                    countTF += 1.0
                    countF += 1.0
            else:
                if (vector[globalVars.V_LENGTH - 1] == 1):
                    countFT += 1.0
                    countT += 1.0
                else:
                    countFF += 1.0
                    countF += 1.0

        # use uniform dirichlet priors to correct zero values before calculations
        countTT, countTF, countFT, countFF, countT, countF = checkUDP(countTT, countTF, countFT, countFF, countT, countF)
        
        globalVars.PROB_T = countT
        globalVars.PROB_F = countF
        
        # calculate (word | CL) probabilities
        probTT = countTT / countT
        probTF = countTF / countF
        probFT = countFT / countT
        probFF = countFF / countF

        probVec = [probTT, probTF, probFT, probFF]
        probTable.append(probVec)
    #print(probTable)


    
        