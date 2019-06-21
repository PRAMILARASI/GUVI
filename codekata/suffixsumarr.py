kk=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(1):
    for j in range(i,kk):
        b.append(str(sum(a[:j+1])))
b=b[::-1]
print(" ".join(b))
