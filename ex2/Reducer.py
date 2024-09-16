#!usr/bin/env python3
import sys
sets = {}

for line in sys.stdin:
    data = line.split("\t")
    data[0] = data[0].strip()
    data[1] = data[1].replace("\n","")
    if (data[0] not in list(sets.keys())):
        sets[data[0]] = int(data[1])
    else:
        sets[data[0]] += int(data[1])

for i in sets:
    print(i,"\t",sets[i])
