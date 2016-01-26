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
            a = re.compile(" "+re.escape(row[0])+" ")
            weights[row[0]] = (a,float(row[1]))
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
patternCount = collections.defaultdict(int)
patternWtdCount = collections.defaultdict(float)
speakerCount = collections.Counter()
wordCount = collections.Counter()
p = re.compile(r'\W+')

pos = debateFile.rfind("/")
debateName = debateFile[pos+1:-4]
print "DEBATE NAME:", debateName
pos = weightFile.rfind("/")
analysisName = weightFile[pos+1:-4]
print "PERSONALITY TYPE:", analysisName

with open(debateFile, 'rb') as f:
    reader = csv.reader(f, delimiter = ",")
    for row in reader:
        if row[1].lower() in candidates:
            speech = p.split(row[2].lower())
            count = 0
            wtdCount = 0.0
            speechStr = " ".join(speech)
            for word, weight in weights.iteritems():
#                a = re.compile(" "+re.escape(word)+" ")
                wCount = len(weight[0].findall(speechStr))
#                wCount = speech.count(word)
#                if wCount>0:
#                    print row[1], word, wCount
                wtdCount += weight[1]*wCount
                count += wCount
            patternCount[row[1]] += count
            patternWtdCount[row[1]] += wtdCount
            speakerCount[row[1]] += 1
            wordCount[row[1]] += len(speech)
normalizedPatternCount = {}
for key, value in patternWtdCount.iteritems():
#    normalizedPatternCount[key] = value/speakerCount[key]
    normalizedPatternCount[key] = value/wordCount[key]
sorted_x = sorted(normalizedPatternCount.items(), key=operator.itemgetter(1), reverse = True)
#pos = debateFile.rfind("/")
#debateName = debateFile[pos+1:-4]
#print "DEBATE NAME:", debateName
#pos = weightFile.rfind("/")
#analysisName = weightFile[pos+1:-4]
#print "PERSONALITY TYPE:", analysisName
for count in sorted_x:
    print count[0], patternCount[count[0]], count[1]
