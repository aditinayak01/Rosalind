f = open("C:/Users/aditi/Desktop/rosalind_ba9m.txt","r")
list1=f.readline().replace('\n', '').split()

pattern=f.readline().replace('\n', '').split()

LastColumn=''.join(list1)
Firstcolumn=''.join(sorted(list1[0]))

def Count(index,LastColumn,symbol):
    dummystring= LastColumn[:index]
    count=0
    for i in dummystring:
        if(i==symbol):
            count=count+1
    return count

def FirstOccurrence(symbol):
    index=Firstcolumn.find(symbol)
    return index

def occurence(LastColumn,symbol,top,bottom):
    a=[]
    for i in range(top,bottom+1):
        if(symbol==LastColumn[i]):
            a.append(i)
    return a


def BWMatching(Firstcolumn,LastColumn,Pattern):
    top=0
    bottom=len(LastColumn)-1
    while(top<=bottom):
        if len(Pattern):
            symbol=Pattern[-1]
            Pattern=Pattern[:-1]
            positions=occurence(LastColumn,symbol,top,bottom)
            if len(positions):
                top=FirstOccurrence(symbol)+Count(top,LastColumn,symbol)
                bottom=FirstOccurrence(symbol)+Count(bottom+1,LastColumn,symbol)-1
            else:
                return 0
        else:
            return bottom-top+1

a=[]

for i in pattern:
    index=BWMatching(Firstcolumn,LastColumn,i)
    a.append(index)
a=" ".join([str(x) for x in a])
print(a)