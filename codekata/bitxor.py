#rev
nx=int(input())
l=[int(x) for x in input().split()]
a=0
if(nx==len(l)):
	for i in range(0,nx):
		for j in range(i+1,nx):
			a=l[i]^l[j]
print(a)
