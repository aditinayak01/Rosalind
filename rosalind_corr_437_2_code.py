import collections
f = open("C:/Users/aditi/Desktop/rosalind_corr (1).txt", "r")
list2=[]
list1=f.read().replace('\n', '').split(">Rosalind_")  #creating rosalind free list
for char in list1:
    if char=='':
        continue
    else:
        n = 4
        list2.append(char[n:])                       #removing numbers from the list1
list3=[]
for line in list2:
    teststring=''.join(reversed(line))
    list3.append(teststring)
list4=[]
teststring=''
complement = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
for line in list3:
    teststring=''
    for i in line:
         teststring=teststring+(''.join([complement[i]]))
    list4.append(teststring)
list4 =list2+list4
c = collections.Counter(list4)
corr=[]
incorr=[]
for i in c:
    if c[i]>=2:
        corr.append(i)
    elif i in list2:
        incorr.append(i)

corrections= []
for seq1 in incorr:
    for seq2 in corr:
        changes = 0
        for x in range(len(seq1)):
            if seq1[x] != seq2[x]:
                changes += 1
        if changes==1:
            corrections.append([seq1, seq2])
for i in corrections:
    print  "->".join(i)