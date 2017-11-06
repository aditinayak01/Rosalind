f = open("C:/Users/aditi/Desktop/rosalind_dna (1).txt","r")
list1=f.read()
newlist=list(list1)


A_counter=0
G_counter=0
C_counter=0
T_counter=0

for i in (newlist):
    if (i=='A'):
        A_counter+=1
    elif (i=='G'):
        G_counter+=1
    elif (i=='C'):
        C_counter+=1
    elif(i=='T'):
        T_counter+=1

print(A_counter, C_counter, G_counter,T_counter)

