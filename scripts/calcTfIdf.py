import csv
import re
import collections
import operator
import sys
import numpy as np

fileName = sys.argv[1]
listTokens = []
tfDict = collections.Counter()
idfDict = collections.Counter()
windowSize = 15
#dialogues = {}
docs = {}
tfIdfScore = {}
tokenImportance = collections.defaultdict(float)

p = re.compile(r'\W+')
newDoc = []
docId = 0
with open(fileName, 'rb') as f:
    reader = csv.reader(f, delimiter = ",")
    for row in reader:
        dialogue = p.split(row[2].lower())
#        dialogues[row[0]] = dialogue
        listTokens.extend(dialogue)
        newDoc.extend(dialogue)
        if int(row[0])%windowSize == 0:
            docs[docId] = newDoc
            newDoc = []
            docId += 1

for token in listTokens:
    for docId, doc in docs.iteritems():
        if token in doc:
            idfDict[token] += 1
            tfDict[(token, docId)] = doc.count(token)

for token in listTokens:
    for docId, doc in docs.iteritems():
        tfIdfScore[(token, docId)] = tfDict[(token, docId)]*np.exp(np.log(len(docs))-np.log(idfDict[token]))
        tokenImportance[token] += tfIdfScore[(token, docId)]

tokenImportance = sorted(tokenImportance.items(), key = operator.itemgetter(1), reverse = True)

for elem in tokenImportance:
    print elem
