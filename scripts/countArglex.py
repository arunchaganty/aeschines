import csv
import re
import collections
import operator
import sys
'''
macros = {}
macroFile = sys.argv[3]
i = 1
macroName = None
with open(macroFile, "r") as f1:
    for line in f1:
        if i%2==1:
            macroName = line[:-1]
        else:
            macros[macroName] = "(" + "|".join(line[:-1].split()) + ")"
        i+=1
'''
patternFile = sys.argv[2]
regex = collections.defaultdict(list)
with open(patternFile,"r") as f:
    for line in f:
        if "class" in line:
            className = line.split("\"")[1]
        elif len(line) > 1:
#            for macro, macroVal in macros.iteritems():
#                line = line.replace(macro, macroVal)
            try:
                line = line.replace("\n", "")
                x = re.compile(line)
                regex[className].append(line)
#                regex[className].append(x)
#                print x.pattern
            except:
                print "Fail!", line[:-1]
print "-----------------------------------------"
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
patternCount = collections.defaultdict(collections.Counter)
speakerCount = collections.Counter()
wordCount = collections.Counter()
p = re.compile(r'\W+')
with open(fileName, 'rb') as f:
    reader = csv.reader(f, delimiter = ",")
    for row in reader:
        if row[1].lower() in candidates:
            speech = p.split(row[2].lower())
            for className, rPatterns in regex.iteritems():
                count = 0
                for rPattern in rPatterns:
                    count += len(re.findall(rPattern, row[2].lower(), re.S))
#                    print count, re.findall(rPattern, row[2].lower()), rPattern, row[2].lower()
#                    count += len(rPattern.findall(row[2].lower()))
#                    print count, rPattern.findall(row[2].lower()), rPattern.pattern, row[2].lower()
                patternCount[className][row[1]] += count
            speakerCount[row[1]] += 1
            wordCount[row[1]] += len(speech)
normalizedPatternCount = collections.defaultdict(dict)
for className, counts in patternCount.iteritems():
    for key, value in counts.iteritems():
        normalizedPatternCount[className][key] = value*1.0/speakerCount[key]
#    normalizedPatternCount[key] = value*1.0/wordCount[key]
pos = fileName.rfind("/")
debateName = fileName[pos+1:-4]
print "DEBATE NAME:", debateName
for className in normalizedPatternCount.keys():
    print className
    sorted_x = sorted(normalizedPatternCount[className].items(), key=operator.itemgetter(1), reverse = True)
    if sorted_x[0][1]>0:
        for count in sorted_x:
            print count[0], count[1]
