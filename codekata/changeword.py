as1=list(input().split())

if len(as1)>1:

	for i in range(len(as1)):

		if as1[i]=='and':

			as1[i-1],as1[i+1]=as1[i+1],as1[i-1]

	print(*as1)

else:

	print(*as1)
