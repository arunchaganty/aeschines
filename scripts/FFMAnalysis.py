import csv
import re
import collections
import operator
import sys

weightFile = sys.argv[2]
weights = {}
with open(weightFile,"rb") as f:
    reader1 = csv.reader(f, delimiter = ",")
    for row in reader1:
        try:
            weights[row[0]] = float(row[1])
        except:
            continue

participantsFile = sys.argv[1]
pos = participantsFile.find("_parts")
debateFile = participantsFile[:pos] + ".csv"
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
patternCount = collections.defaultdict(float)
speakerCount = collections.Counter()
wordCount = collections.Counter()
p = re.compile(r'\W+')
with open(debateFile, 'rb') as f:
    reader = csv.reader(f, delimiter = ",")
    for row in reader:
        if row[1].lower() in candidates:
            speech = p.split(row[2].lower())
            count = 0.0
            speechStr = " ".join(speech)
            for word, weight in weights.iteritems():
                count += weight*speechStr.count(word)
            patternCount[row[1]] += count
            speakerCount[row[1]] += 1
            wordCount[row[1]] += len(speech)
normalizedPatternCount = {}
for key, value in patternCount.iteritems():
#    normalizedPatternCount[key] = value/speakerCount[key]
    normalizedPatternCount[key] = value/wordCount[key]
sorted_x = sorted(normalizedPatternCount.items(), key=operator.itemgetter(1), reverse = True)
pos = debateFile.rfind("/")
debateName = debateFile[pos+1:-4]
print "DEBATE NAME:", debateName
pos = weightFile.rfind("/")
analysisName = weightFile[pos+1:-4]
print "PERSONALITY TYPE:", analysisName
for count in sorted_x:
    print count[0], count[1]
