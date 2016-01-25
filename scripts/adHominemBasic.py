import csv
import re
import collections
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

lastSpeaker = None
adHominemCounts = {}
with open(fileName, 'rb') as f:
    reader = csv.reader(f, delimiter = ",")
    for row in reader:
        if row[1].lower() in candidates:
            if row[1].lower() not in adHominemCounts:
                adHominemCounts[row[1].lower()] = [0,collections.Counter()]
            if lastSpeaker in candidates and row[1].lower() in candidates:
                adHominemCounts[row[1].lower()][0] += 1
                adHominemCounts[row[1].lower()][1][lastSpeaker] += 1
            for candidate in candidates:
                if candidate in row[2].lower():
                    adHominemCounts[row[1].lower()][0] += 1
                    adHominemCounts[row[1].lower()][1][candidate] += 1
        lastSpeaker = row[1]
pos = fileName.rfind("/")
debateName = fileName[pos+1:-4]
print "DEBATE NAME:", debateName
for person1, totCount in adHominemCounts.iteritems():
    for person2, count in totCount[1].iteritems():
        print person1, person2, count
