kk=int(input())
a=[int(x) for x in input().split()]
bb=[]
for i in range(kk):
    c=a[:i+1]
    if sum(c)%2==0:
        bb.append(str(sum(c)))
    else:
        bb.append(str(a[i]))
print(" ".join(b))
