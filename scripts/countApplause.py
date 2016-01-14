import csv
import re
import collections
import operator
import sys

participantsFile = sys.argv[1]
pos = participantsFile.find("_parts")
fileName = participantsFile[:pos] + ".csv"

candidates = []
i = 0
with open(participantsFile, 'rb') as f1:
    reader = csv.reader(f1, delimiter = ",")
    for row in reader:
        if i < 2:
            candidates.extend(row)
        i+=1
for i in xrange(len(candidates)):
    candidates[i] =  candidates[i].lower()
applauseCount = collections.Counter()
speakerCount = collections.Counter()
wordCount = collections.Counter()
p = re.compile(r'\W+')
applauseKeyWord = '[applause]'
with open(fileName, 'rb') as f:
applauseKeyWord = '[applause]'
with open("Debates/csv/" + fileName + '.csv', 'rb') as f:
    reader = csv.reader(f, delimiter = ",")
    for row in reader:
        if row[1].lower() in candidates:
            applauseCount[row[1]] += row[2].count(applauseKeyWord)
            speakerCount[row[1]] += 1
            wordCount[row[1]] += len(p.split(row[2].lower()))
normalizedApplauseCount = {}
for key, value in applauseCount.iteritems():
#    normalizedApplauseCount[key] = value*1.0/speakerCount[key]
    normalizedApplauseCount[key] = value*1.0/wordCount[key]
sorted_x = sorted(normalizedApplauseCount.items(), key=operator.itemgetter(1), reverse = True)
pos = fileName.rfind("/")
debateName = fileName[pos+1:-4]
print "DEBATE NAME:", debateName
for count in sorted_x:
    print count[0], count[1]
