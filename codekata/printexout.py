sp=input()
l=[]
for i in range(len(sp)):
	if sp[i].isdigit():
		l.append(sp[i-1]*(int(sp[i])-1))
	else:
		l.append(sp[i])
print("".join(l))
