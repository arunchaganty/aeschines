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
pronounCount = collections.Counter()
speakerCount = collections.Counter()
wordCount = collections.Counter()
listOfPronouns = ['i','me','my','mine','we','our','ours','we','us','myself','ourselves']
p = re.compile(r'\W+')
with open(fileName, 'rb') as f:
    reader = csv.reader(f, delimiter = ",")
    for row in reader:
        if row[1].lower() in candidates:
            count = 0
            speech = p.split(row[2].lower())
            for pronoun in listOfPronouns:
                count += speech.count(pronoun)
            pronounCount[row[1]] += count
            speakerCount[row[1]] += 1
            wordCount[row[1]] += len(speech)
normalizedPronounCount = {}
for key, value in pronounCount.iteritems():
#    normalizedPronounCount[key] = value*1.0/speakerCount[key]
    normalizedPronounCount[key] = value*1.0/wordCount[key]
sorted_x = sorted(normalizedPronounCount.items(), key=operator.itemgetter(1), reverse = True)
pos = fileName.rfind("/")
debateName = fileName[pos+1:-4]
print "DEBATE NAME:", debateName
for count in sorted_x:
    print count[0], count[1], speakerCount[count[0]]
