aa1  = int(input())
aa2  = list(map(int,input().split()))
aa2.sort()
for i in aa2:
	if i < aa1:
		print(i,end=' ')
