l1=list(input().split())

ab=[]

for i in range(len(l1)):

	ab.append(sorted(l1[i]))

s=""

for i in ab:

	s+="".join(i)+" "

print(s.strip())
