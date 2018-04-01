f = open("C:/Users/aditi/Desktop/rosalind_splc.txt", "r")
l = f.readline()
mainstr = ''
newstr=''
mainrnaread = 'False'
rnacodon={"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

while True:
    l = f.readline().strip()
    if ("" == l):
        break
    if '>' not in l and mainrnaread == 'True':
        intron = l
        mainstr = mainstr.replace(intron,'')
    if'>' in l:
        mainrnaread='True'
    if '>' not in l and mainrnaread=='False':
          mainstr=mainstr+l
for line in mainstr:
    mainstr=mainstr.replace('T','U')
finalString = ''
for i in range(0, len(mainstr), 3):
    if mainstr[i:i+3] in rnacodon.keys():
        finalString = finalString + rnacodon.get(mainstr[i:i+3])

if 'STOP' in finalString:
    finalString=finalString.replace('STOP',"")

print(finalString)