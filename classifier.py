#!/usr/bin/env python

# considering good review as TRUE and bad review as FALSE

import string
import globalVars
from preprocessing import processingDriver
from probTable import createTable
from predict import predict
# from bayesClassifier import 

VOCABULARY = []

# driver code
training = "trainingSet.txt"
testing = "testSet.txt"

trainFeatures = []
testFeatures = []

probTable = []

processingDriver(training, testing, trainFeatures, testFeatures)
createTable(trainFeatures, probTable)
predict(trainFeatures, probTable)
