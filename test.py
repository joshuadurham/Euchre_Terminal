import math

n = '1 3 5'.strip().split(' ')
times = []
for elem in n:
    times.append(int(elem))
i = 0
numWaits = len(times) - 1
differences = []
while(i < numWaits):
    difference = times[i+1] - times[i]
    differences.append(difference)
    i += 1
sublists = []
idx = 0
jdx = 1
while(idx < len(differences)):
    while(jdx <= len(differences)):
        sublists.append(differences[idx:jdx])
        jdx += 1
    idx += 1
    jdx = idx + 1
length = 1
while(length < len(differences)):
    listsOfLength = []
    for elem in sublists:
        if(len(elem) == length):
            listsOfLength.append(elem)
    counts = []
    for elem in listsOfLength:
        counts.append(listsOfLength.count(elem))
    allOne = True
    for elem in counts:
        if (elem > 1):
            allOne = False
    if(allOne):
        print(length)
        length = len(differences) + 1
    length += 1