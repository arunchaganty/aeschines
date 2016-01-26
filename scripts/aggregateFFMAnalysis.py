import csv
import re
import collections
import operator
import sys

resultsFile = sys.argv[1]
f = open(resultsFile,"r")
results = {}
types = []
debateCounts = collections.Counter()
for line in f:
    if "DEBATE" in line:
        continue
    elif "TYPE" in line:
        pos = line.find(":")
        personalityType = line[pos+2:-1]
        if personalityType not in types:
            types.append(personalityType)
    else:
        splits = line.split()
        if splits[0] not in results:
            results[splits[0]] = collections.defaultdict(list)
        if personalityType not in results[splits[0]]:
            results[splits[0]][personalityType] = [0,0]
        results[splits[0]][personalityType][0] += int(splits[1])
        results[splits[0]][personalityType][1] += float(splits[2])
        debateCounts[splits[0]] += 1

for candidate, types in results.iteritems():
    for persType in types:
        results[candidate][persType][1] /= debateCounts[candidate]

print "||",
for personalityType in types:
    print personalityType,"|",
print
for _ in xrange(len(types)+1):
    print "---|",
print
for candidate in results:
    print candidate,"|",
    for personalityType in types:
        print results[candidate][personalityType],"|",
    print
