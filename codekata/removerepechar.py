sa1=input()

l=[]

a=""

for i in sa1:

	if sa1.count(i)!=1 and i not in l:

		l.append(i)

		a=a+i

	elif sa1.count(i)==1:

		a=a+i

print(a)
