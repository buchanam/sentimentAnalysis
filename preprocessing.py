# global variables
VOCABULARY = []
V_LENGTH = 0

# strips puncuation and case from vocabulary words
def cleanWord(word):
    # all lower case
    word = word.lower()
    # punctuation removal
    word = word.translate(None, "%+\,$&*?.()[]!'-:")

    return word
    
def convertToFeatures(file, fileName):
    newFile = open(fileName, "w")

    # first header line
    for word in VOCABULARY:
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

        print("CLASS LABEL: " + str(classLabel))
        for x in range(0,V_LENGTH - 1):
            if (lineWordList[0] == VOCABULARY[x]):
                newFile.write("1,")
                lineWordList.pop(0)
            else:
                newFile.write("0,")

        newFile.write(str(classLabel))
        newFile.write("\n")    
    

# preprocessing steps: clean words, create vocab, convert to features
def preprocessingDriver():
    # open files
    trainF = open("trainingSet.txt", "r")
    testF = open("testSet.txt", "r")

    global VOCABULARY
    # create training data vocabulary
    for line in trainF:
        for word in line.split():
            word = cleanWord(word)
            # if word not number
            if not (word.isdigit() or word in VOCABULARY or word is None):
                VOCABULARY.append(word)

    trainF.close()
    trainF = open("trainingSet.txt", "r")
    # sort vocabulary alphabetically
    VOCABULARY = sorted(VOCABULARY)
    VOCABULARY.pop(0)
    global V_LENGTH
    V_LENGTH = len(VOCABULARY)

    convertToFeatures(trainF, "preprocessed_train.txt")
    convertToFeatures(testF, "preprocessed_test.txt")