import csv
import re
import collections
import operator

fileName = "Republican_Ohio_Aug_2015"

candidates = []
i = 0
with open("Debates/csv/" + fileName + '_parts.csv', 'rb') as f1:
    reader = csv.reader(f1, delimiter = ",")
    for row in reader:
        if i < 2:
            candidates.extend(row)
        i+=1
for i in xrange(len(candidates)):
    candidates[i] =  candidates[i].lower()
applauseCount = collections.Counter()
speakerCount = collections.Counter()
applauseKeyWord = '[applause]'
with open("Debates/csv/" + fileName + '.csv', 'rb') as f:
    reader = csv.reader(f, delimiter = ",")
    for row in reader:
        if row[1].lower() in candidates:
            applauseCount[row[1]] += row[2].count(applauseKeyWord)
            speakerCount[row[1]] += 1
print applauseCount
normalizedApplauseCount = {}
for key, value in applauseCount.iteritems():
    normalizedApplauseCount[key] = value*1.0/speakerCount[key]
sorted_x = sorted(normalizedApplauseCount.items(), key=operator.itemgetter(1), reverse = True)
print sorted_x
