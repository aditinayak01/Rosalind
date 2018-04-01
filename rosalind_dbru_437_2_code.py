from collections import defaultdict
f = open("C:/Users/aditi/Desktop/rosalind_dbru (1).txt", "r")
list1=[]
for i in f.readlines():
    i=i.replace('\n', '')
    list1.append(i)
list2=[]
for line in list1:
    teststring=''.join(reversed(line))
    list2.append(teststring)
teststring=''
complement = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
for line in list2:
    teststring=''
    for i in line:
         teststring=teststring+(''.join([complement[i]]))
    list1.append(teststring)
list3=[]
list4=[]
for i in list1:
    list3.append(i[:-1])
    list4.append(i[1:])
d = defaultdict(list)
r=defaultdict(list)
for k, v in zip(list3,list4):
    if v not in d[k]:
        d[k].append(v)
        d[k].sort()
for k in sorted(d.iterkeys()):
        for v in d[k]:
            print "({a}, {b})".format(a = k, b = v)