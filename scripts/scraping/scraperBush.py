import sys

flag = False
filename = sys.argv[1]

with open(filename, "rb") as f:
    for line in f:
        if "RUBIO:" in line:
            flag = True
            line = line.split("RUBIO:")[1]
        elif ":" in line:
            flag = False
        if flag:
            print line
