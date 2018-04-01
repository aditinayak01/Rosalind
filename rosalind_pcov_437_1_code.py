f = open("C:/Users/aditi/Desktop/rosalind_pcov.txt", "r")
list1=[]
for i in f.readlines():
    i=i.replace('\n', '')
    list1.append(i)
print list1
text=list1[0]
list1.remove(text)
k=len(list1[0])

while len(list1)!=0:
    test=text[-(k-1):]
    for i in range(len(list1)):
        dummy=list1[i]
        if dummy[:-1] == test:
            text=text + dummy[-1]
            list1.remove(dummy)
            break
print text[:-(k-1)]