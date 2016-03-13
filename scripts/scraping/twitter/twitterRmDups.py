import csv
import re
import collections
import operator
import sys


tweets = {}

opFile = "../results/allTweets.csv"

total = 0

files = sys.argv[1:]
for f1 in files:
    with open(f1,"rb") as f:
        reader = csv.reader(f, delimiter = ",")
        for row in reader:
            total += 1
            if row[0] not in tweets:
                tweets[row[0]] = row[1]

distinct = len(tweets.keys())

with open(opFile,"wb") as f:
    writer = csv.writer(f, delimiter = ",")
    for tId in tweets:
        writer.writerow([tId, tweets[tId]])

print total, distinct
