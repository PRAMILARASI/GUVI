sk=input()
gk=[]
for i in sk:
	if i!=" ":
		gk.append(sk.count(i))
m=max(g)
a=""
for i in sk:
	if sk.count(i)==m and i not in a:
		a=a+i
print(m,a)
