sa,k=input().split()
k=int(k)
a=""
for i in range(len(sa)):
	if (i+1)%k==0:
		a+=sa[i].upper()
	else:
		a+=sa[i]
print(a)
