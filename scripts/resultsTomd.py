import csv
import re
import collections
import operator
import sys

resultsFile = sys.argv[1]
f = open(resultsFile,"r")
results = {}
debates = []
debateCounts = collections.Counter()
debate = None
for line in f:
    if "DEBATE NAME" in line:
        pos = line.find(":")
        debate = line[pos+2:-1]
        debates.append(debate)
    else:
        splits = line.split()
        if splits[0] not in results:
            results[splits[0]] = {}#collections.defaultdict(float)
        results[splits[0]][debate] = (int(splits[1]),float(splits[2]))
        debateCounts[splits[0]] += 1

normResults = collections.defaultdict(float)
totResults = collections.Counter()
for candidate, debates in results.iteritems():
#    sumResults = 0.0
    for debate in debates:
#        sumResults += results[candidate][debate][1]
        normResults[candidate] += results[candidate][debate][1]
        totResults[candidate] += results[candidate][debate][0]
    normResults[candidate] /= debateCounts[candidate]

print "|Candidate|Total Count|Normalized Count"
print "---|---|---|"
for candidate, value in normResults.iteritems():
    print candidate, "|", totResults[candidate], "|", value,"|"
