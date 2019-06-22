nk1=input()
l=[]
c=0
for i in range(0,len(nk1)-1):
    k=int(nk1[i])+int(nk1[i+1])
    if k%2!=0:
        c+=1
    else:
        l.append(c)
        c=0
    l.append(c)
m=max(l)
if m==0:
    print(0)
else:
    print(m+1)
