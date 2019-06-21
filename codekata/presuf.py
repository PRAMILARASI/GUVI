kk=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
for i in range(1):
    for j in range(i,kk):
        b.append(sum(a[:j+1]))
l=b[::-1]
for i in range(kk):
    c.append(str(b[i]+l[i]))
print(" ".join(c))
