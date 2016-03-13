import csv
import collections

dates = collections.Counter()
filename = "../results/allTweets.csv"
with open(filename, "rb") as f1:
    reader = csv.reader(f1)
    for row in reader:
        dates[row[0].split(" ")[0]] += 1

for k, v in dates.iteritems():
    print k, v
