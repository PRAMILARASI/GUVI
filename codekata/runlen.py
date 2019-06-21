sk=input()
i=0
k=""
j=i+1
c=1
while j<len(sk):
	if sk[i]==sk[j]:
		c=c+1
	else:
		k=k+sk[i]+str(c)
		i=j
		c=1
 
	j=j+1
k=k+sk[i]+str(c)
print(k)
