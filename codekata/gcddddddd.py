n1,mm=map(int,input().split())
g=min(n1,mm)
c=1
for i in range(1,g+1):
	c*=i
print(c)
