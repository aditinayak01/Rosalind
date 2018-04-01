import string
from collections import OrderedDict
f = open("C:/Users/aditi/Desktop/rosalind_grph.txt", "r")
list2=[]
list1=f.read().replace('\n', '').split(">Rosalind_")  #creating rosalind free list

for char in list1:
    if char=='':
        continue
    else:
        n = 4
        list2.append(char[n:])                       #removing numbers from the list1


c=open("C:/Users/aditi/Desktop/rosalind_grph.txt", "r")
Rosalindlist=[]
while True:
    l = c.readline().strip()
    if ("" == l):
        break
    if'>' in l:
        Rosalindlist.append(l.replace(">",""))        #Creating a list having only rosalind entries
a={}
a=OrderedDict(zip(Rosalindlist, list2))               #creating dicitonary of list2 and Rosalindlist

results=[]
for key, value in a.items():
        for key2, value2 in a.items():
            if key != key2 and value.endswith(value2[:3]):  #Creating a graph representation
                results.append((key, key2))

graph = '\n'.join(map(str, results))
graph= graph.replace("'",'').replace(",",'').replace('(','').replace(')','') #printing answer in required format
print(graph)