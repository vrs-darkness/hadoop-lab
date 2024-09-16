#!usr/bin/env python3

import sys
element = []
sets = {}
all_elements = ""
for line in sys.stdin:
    data = line.split("\t")[1].split(",")
    data[-1] = data[-1].replace("\n","")
    all_elements += ",".join(data) + "|"
    for i in data:
        if i in element:
            sets[i] +=1
        else:
            sets[i] = 1
            element.append(i)

        for j in list(sets.keys()):
            item = i + "," + j

            if item in list(sets.keys()):
                sets[item] +=1
            elif item in all_elements:
                sets[item] = 1
for i in sets:
    print(i,"\t",sets[i])
