import itertools
f = open("C:/Users/aditi/Desktop/rosalind_ctea.txt", "r")
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
optimal= [[0 for x in range(len(stringB)+1)] for y in range(len(stringA)+1)]
optimal[0][0]=1
for i in range(1,len(stringA)+1):
    for j in range(1,len(stringB)+1):
        EditMat[i][0]=i
        EditMat[0][j]=j

        optimal[i][0] = i
        optimal[0][j] = j

position=[]

for i in range(1,len(stringA)+1):

    for j in range(1,len(stringB)+1):
        count = 0
        if(stringA[i-1]==stringB[j-1]):
            EditMat[i][j]=min(match+EditMat[i-1][j-1],gapcost+EditMat[i-1][j],gapcost+EditMat[i][j-1])
            minvalue=min(match+EditMat[i-1][j-1],gapcost+EditMat[i-1][j],gapcost+EditMat[i][j-1])
            if minvalue == EditMat[i - 1][j - 1] + match:
                #print("count1", count)
                count = count + optimal[i - 1][j - 1]
            if minvalue == EditMat[i - 1][j] + gapcost:
                #print("count2", count)
                count = count + optimal[i - 1][j]
            if minvalue == EditMat[i][j - 1] + gapcost:
                #print("count3", count)
                count = count + optimal[i][j - 1]
            optimal[i][j]=count

        else:
            EditMat[i][j]= min(mismatch + EditMat[i - 1][j - 1], gapcost + EditMat[i - 1][ j], gapcost + EditMat[i][j - 1])
            minvalue = min(mismatch + EditMat[i - 1][j - 1], gapcost + EditMat[i - 1][j], gapcost + EditMat[i][j - 1])

            if minvalue == EditMat[i - 1][j - 1] + mismatch:
                #print("count1", count)
                count = count + optimal[i - 1][j - 1]
            if minvalue == EditMat[i - 1][j] + gapcost:
                #print("count2", count)
                count = count + optimal[i - 1][j]
            if minvalue == EditMat[i][j - 1] + gapcost:
                #print("count3", count)
                count = count + optimal[i][j - 1]
            optimal[i][j] = count
print(optimal[len(stringA)][len(stringB)]%134217727)