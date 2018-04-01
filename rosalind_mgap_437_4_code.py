f = open("C:/Users/aditi/Desktop/rosalind_mgap (1).txt", "r")
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
print(stringA)
print(stringB)
gapcost=-1
match=1
mismatch=-100
score= [[0 for x in range(len(stringB)+1)] for y in range(len(stringA)+1)]
gap= [[0 for x in range(len(stringB)+1)] for y in range(len(stringA)+1)]
for i in range(1,len(stringA)+1):
    for j in range(1,len(stringB)+1):
        score[i][0]=i*gapcost
        score[0][j]=j*gapcost
        gap[i][0] = i
        gap[0][j] = j
for i in range(1,len(stringA)+1):

    for j in range(1,len(stringB)+1):
        if(stringA[i-1]==stringB[j-1]):
            score[i][j]=max(match+score[i-1][j-1],gapcost+score[i-1][j],gapcost+score[i][j-1])
            maxvalue=max(match+score[i-1][j-1],gapcost+score[i-1][j],gapcost+score[i][j-1])
            if maxvalue == score[i - 1][j - 1] + match:
                gap[i][j] =gap[i - 1][j - 1]
            elif maxvalue == score[i - 1][j] + gapcost:
                gap[i][j] = gap[i - 1][j]
            else:
                gap[i][j] = gap[i][j - 1] + 1

        else:
            score[i][j] = max(mismatch + score[i - 1][j - 1], gapcost + score[i - 1][j], gapcost + score[i][j - 1])
            maxvalue = max(mismatch + score[i - 1][j - 1], gapcost + score[i - 1][j], gapcost + score[i][j - 1])
            if maxvalue == score[i - 1][j - 1] + mismatch:
                gap[i][j] = gap[i - 1][j - 1]
            elif maxvalue == score[i - 1][j] + gapcost:
                gap[i][j] = gap[i - 1][j] + 1
            else:
                gap[i][j] = gap[i][j - 1] + 1
print(gap[len(stringA)][len(stringB)])