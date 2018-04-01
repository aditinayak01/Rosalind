f = open("C:/Users/aditi/Desktop/rosalind_ba9i (1).txt","r")
list1=f.read().strip()
print(list1)
length=len(list1)
arraylist=[]
str=''
for i in range(0,length):
    lastchar=list1[-1:]
    str=str+lastchar
    list1=list1[:-1]
    str1=''.join((list1,str))
    arraylist.append(str1[::-1])
BWT=[]
for i in arraylist:
    index=i.find('$')
    reversestring=i[:index:-1]
    i=i[:index]+i[index]+reversestring
    BWT.append(i)
BWTsort=sorted(BWT)


BWTstr=''
for i in BWTsort:
    BWTstr=BWTstr+i[-1]
print(BWTstr)