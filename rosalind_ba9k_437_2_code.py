f = open("C:/Users/aditi/Desktop/rosalind_ba9k.txt","r")
str1=f.readline().strip()
a=sorted(str1)
str2=''.join(a)
index=int(f.readline())
letter=str1[index]
count=0
dummystr=str1[:index+1]
for j in dummystr:
   if(j==letter):
        count+=1
counter=0
pointer=0
for i in str2:
    if(letter==i):
        counter+=1
        if counter==count:
            for index, c in enumerate(str2):
                if c == letter:
                    pointer += 1
                    if pointer==counter:
                        print(str2.index(i)+counter-1)
                        break