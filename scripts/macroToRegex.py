import sys
macros = {}
macroFile = sys.argv[2]
i = 1
macroName = None
with open(macroFile, "r") as f1:
    for line in f1:
        if i%2==1:
            macroName = line[:-1]
        else:
            macros[macroName] = "(" + "|".join(line[:-1].split()) + ")"
        i+=1
patternFile = sys.argv[1]
regex = []
with open(patternFile,"r") as f:
    for line in f:
        if "class" in line:
            print line[:-1]
        else:
            for macro, macroVal in macros.iteritems():
                line = line.replace(macro, macroVal)
            print line[:-1]
