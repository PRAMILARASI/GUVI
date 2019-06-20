input()
lb=[]
a=list(map(int,input().split()))
for i in range(0,len(a)-1):
	if a[i]>a[i+1]:
		lb.append(a[i])
	else:
		lb.append(a[i+1])
print(sum(lb))
