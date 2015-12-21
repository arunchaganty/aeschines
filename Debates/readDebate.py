import csv
import sys

year = sys.argv[1]
fileName = sys.argv[2][:-4]
f = open(year + fileName + ".txt","r")
speaker = None
i = 1
#(hacky implementation - subject to exact matching of format)

#Saves debate transcript as tuples of (dialogueID, speaker, speech)
with open("csv/" + fileName + '.csv', 'wb') as f1:
    writer = csv.writer(f1)
    speech = ""
    for line in f:
        line = line.replace('\n', ' ')
        if ':' in line:            
            pos = line.find(':')
            if line[:pos].upper() == line[:pos]:
                if speaker is not None:
                    writer.writerow((i,speaker, speech))
                    i+=1
                speaker = line[:pos]
                speech = line[pos+1:]
            else:
                speech += line
        else:
            speech += line

#1st row corresponds to First Names of Participants
#2nd row corresponds to Last Names of Participants
#3rd row corresponds to First Names of Moderators
#4th row corresponds to Last Names of Moderators

ff = open(year + "parts/" + fileName + "_participants.txt","r")
flag = 0
partFNs = []
partLNs = []
modFNs = []
modLNs = []
for line in ff:
    if "PARTICIPANTS" in line:
        flag = 1
    elif "MODERATORS" in line:
        flag = 2
    elif flag == 1 and len(line)>1:
        pos = line.find('(')
        if pos < 0:
            pos = line.find(';')
        splits = line[:pos].split()
        partFNs.append(splits[-2])
        partLNs.append(splits[-1])
    elif flag == 2 and len(line)>1:
        pos = line.find('(')
        if pos < 0:
            pos = line.find(';')
        splits = line[:pos].split()
        modFNs.append(splits[-2])
        modLNs.append(splits[-1])
with open("csv/" + fileName + '_parts.csv', 'wb') as f2:
    writer = csv.writer(f2)
    writer.writerow(partFNs)
    writer.writerow(partLNs)
    writer.writerow(modFNs)
    writer.writerow(modLNs)
