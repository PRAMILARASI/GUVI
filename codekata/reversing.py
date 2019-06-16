aA=input().split()
b=[]
for i in aA:
  b.append(i[::-1])
print(*b,sep=' ')
