na1=input()

l=list(na1)

l=[int(i) for i in l]

a=[]

for i in range(len(l)):

	m=max(l)

	a.append(str(m))

	l.remove(m)

print("".join(a))
