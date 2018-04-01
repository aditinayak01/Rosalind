import math
f = open("C:/Users/aditi/Desktop/rosalind_prob (1).txt").readlines()
letters = f[0].strip()
strip_prob=f[1].strip()
prob = map(float, strip_prob.split())
list1 = []
for p in prob:
    sum = 0
    for i in letters:
        if i == 'G' or i == 'C':
            sum += math.log((p / 2), 10)
        elif i == 'A' or i == 'T':
            sum += math.log((1 - p) / 2, 10)
    list1.append("{0:.3f}".format(sum))

for i in list1:
    print(i,end= " ")