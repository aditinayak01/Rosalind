f = open("C:/Users/aditi/Desktop/rosalind_ba9l.txt","r")
list1=f.readline().replace('\n', '').split()

pattern=f.readline().replace('\n', '').split()

LastColumn=''.join(list1)
Firstcolumn=''.join(sorted(list1[0]))


def LasttoFirst(index):
    letter=LastColumn[index]
    count=0
    dummystr=LastColumn[:index+1]
    for j in dummystr:
        if(j==letter):
            count+=1
    counter=0
    pointer=0
    for i in Firstcolumn:
        if(letter==i):
            counter+=1
            if counter==count:
                for index, c in enumerate(Firstcolumn):
                    if c == letter:
                        pointer += 1
                        if pointer==counter:
                            return(Firstcolumn.index(i)+counter-1)
                            break
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
                topindex=positions[0]
                bottomindex=positions[len(positions)-1]
                top=LasttoFirst(topindex)
                bottom=LasttoFirst(bottomindex)
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