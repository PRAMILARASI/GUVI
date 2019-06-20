b1  = list(map(int,input().split()))
b2  = list(map(int,input().split()))
b2.sort()
for i in b2:
	if i < b1[1]:
		print(i,end=' ')
