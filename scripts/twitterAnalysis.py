import csv
import re
import collections
import operator
import sys
import numpy as np
import cPickle

fileName = sys.argv[1]
tweets = collections.defaultdict(list)
hashtagregex = re.compile(r'#\w+')
persontagregex = re.compile(r'#\w+')
newDoc = []
docId = 0
with open(fileName, 'rb') as f:
    reader = csv.reader(f, delimiter = ",")
    for row in reader:
        date, tweet = (row[0], row[1])
        hts = hashtagregex.findall(tweet)
        for ht in hts:
            tweets[ht].append(tweet)
        pts = persontagregex.findall(tweet)
        for pt in pts:
            tweets[pt].append(tweet)

tweetsOld = cPickle.load(open('tweets.pkl, 'r''))
for tweet in tweetsOld:
    for t in tweetsOld[tweet]:
        if t not in tweets[tweet]:
            tweets[tweet].append(t)
cPickle.dump(tweets, open('tweets.pkl', 'w'))
