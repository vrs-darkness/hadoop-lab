from operator import itemgetter
import sys

Max = []
Min = []
for line in sys.stdin:

    data = line.strip().split("\t")
    Max.append(data[data.index("max:") + 1])
    Min.append(data[data.index("min:") + 1])


print("max:\t%s\tmin:\t%s" % (max(Max),min(Min)))
