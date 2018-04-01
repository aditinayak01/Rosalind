import itertools
f = open("C:/Users/aditi/Desktop/rosalind_long.txt", "r")
list2=[]
lengthoflist=0
input=f.read().replace('\n', '').split(">Rosalind_")
for char in input:
	if char=='':
		continue
	else:
		n =4
		list2.append(char[n:])
oldLength=0
len1=0

def overLap(list2):
	stringPattern1,stringPattern2 = '',''
	newLength=0
	for string1,string2 in itertools.permutations(list2,2):
		overlapindex = len(string1)
		while overlapindex > 0:
			if string1[-overlapindex:] == string2[:overlapindex]:
				break
			overlapindex=overlapindex-1
		oldLength = overlapindex
		if oldLength > newLength:
			stringPattern1,stringPattern2=string1,string2
			newLength=oldLength
	return stringPattern1,stringPattern2,newLength

text1,text2,oldLength = overLap(list2)
while oldLength>0:
	list2.remove(text1)
	list2.remove(text2)
	list2.append(text1+text2[oldLength:])
	text1, text2, oldLength = overLap(list2)

print(''.join(list2))