f = open("C:/Users/aditi/Desktop/rosalind_fibd (1).txt","r")
for k in f:
    list1=k.split()
n,m= int(list1[0]),int(list1[1])
alive_Rabbits= [0, 1, 1]
for count in range(3, n + 1):
    if count <= m:
        total = alive_Rabbits[count - 1] + alive_Rabbits[count - 2]
    elif count == m + 1:
        total = alive_Rabbits[count - 1] + alive_Rabbits[count - 2] - 1
    else:
        total = alive_Rabbits[count - 1] + alive_Rabbits[count - 2] - alive_Rabbits[count - m - 1]
    alive_Rabbits.append(total)
print(alive_Rabbits[-1])