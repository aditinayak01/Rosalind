import itertools
f = open("C:/Users/aditi/Desktop/rosalind_edta.txt", "r")
list2=[]
lengthoflist=0
input=f.read().replace('\n', '').split(">Rosalind_")
for char in input:
    if char=='':
        continue
    else:
        list2.append(char[4:])
stringA=list2[0]
stringB=list2[1]
#print(stringA,stringB)
gapcost=1
match=0
mismatch=1
EditMat= [[0 for x in range(len(stringB)+1)] for y in range(len(stringA)+1)]
for i in range(1,len(stringA)+1):
    for j in range(1,len(stringB)+1):
        EditMat[i][0]=i*gapcost
        EditMat[0][j]=j*gapcost
position=[]
def calcDirection(position,value):
    for k in range(len(position)):
        if(position[k]==value):
            direction=k
    if (direction == 0):
        backtrack[i][j]=('diagonal')
    elif(direction==1):
        backtrack[i][j]=('left')
    else:
        backtrack[i][j]=('top')
    return backtrack

backtrack=[[0 for x in range(len(stringB)+1)] for y in range(len(stringA)+1)]
direction=[]
for i in range(1,len(stringA)+1):
    for j in range(1,len(stringB)+1):
        if(stringA[i-1]==stringB[j-1]):
            position=[match+EditMat[i-1][j-1],gapcost+EditMat[i-1][j],gapcost+EditMat[i][j-1]]
            EditMat[i][j]=min(match+EditMat[i-1][j-1],gapcost+EditMat[i-1][j],gapcost+EditMat[i][j-1])
            direction=calcDirection(position,EditMat[i][j])

        else:
            position = [mismatch + EditMat[i - 1][j - 1], gapcost + EditMat[i - 1][j], gapcost + EditMat[i][j - 1]]
            EditMat[i][j]= min(mismatch + EditMat[i - 1][j - 1], gapcost + EditMat[i - 1][ j], gapcost + EditMat[i][j - 1])
            direction = calcDirection(position, EditMat[i][j])

print(EditMat[len(stringA)][len(stringB)])
lenA=len(stringA)
lenB=len(stringB)
dummystrA=stringA
dummystrB=stringB
while lenA>0 and lenB>0:
    if(backtrack[lenA][lenB]=="top"):
        lenB=lenB-1
        dummystrA=dummystrA[:lenA]+'-'+dummystrA[lenA:]
    elif(backtrack[lenA][lenB]=="left"):
        lenA =lenA- 1
        dummystrB = dummystrB[:lenB] + '-' + dummystrB[lenB:]
    else:
        lenA=lenA-1
        lenB=lenB-1
print(dummystrA)
print(dummystrB)