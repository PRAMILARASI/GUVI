sa=input()
l=[]
for i in range(len(sa)):
	if sa[i].isdigit():
		l.append(sa[i-1]*(int(sa[i])-1))
	else:
		l.append(sa[i])
print("".join(l))
