import sys

Temp = []
for line in sys.stdin:
    data = line.strip()
    word = line.split(" ")
    try:
        Temp.append(word[word.index("C") - 1])
    except:
        pass

print ("max:\t%s\tmin:\t%s" % (max(Temp),min(Temp)))



