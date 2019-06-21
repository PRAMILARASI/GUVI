kk,lk=map(int,input().split())
a=list(map(int,input().split()))
b=[]
for i in a:
    if a.count(i)<l and i not in b:
        b.append(i)
c=sorted(b)
print(*c)
