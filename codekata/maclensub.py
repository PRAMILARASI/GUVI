sa=input()
c=0
l=["a","e","i","o","u"]
for i in range(0,len(sa)-2):
	if sa[i] in l and sa[i+1] not in l:
		c+=2
		if sa[i+1] not in l and sa[i+2] in l:
			c+=1
print(c)
