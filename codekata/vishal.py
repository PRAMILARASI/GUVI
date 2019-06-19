n=int(input())
c1=0
for i in range(n):
	a1,b1=map(int,input().split())
	if a1<b1:
		c1=c1+1
print(c1)
