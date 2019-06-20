aa1=input().split()
l=[]
for i in aa1:
  l.append(len(i))
print(aa1[l.index(max(l))])
