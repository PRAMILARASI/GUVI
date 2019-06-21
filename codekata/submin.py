kk=int(input())
a=[int(x) for x in input().split()]
b=[0]
for i in range(kk):
    for j in range(i,kk):
        c=a[i:j+1]
        b.append(sum(c))
print(min(b))
