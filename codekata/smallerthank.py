n1,kk=map(int,input().split())
l=[int(x) for x in input().split()]
m=0
if kk in l:
    print(kk)
else:
    for i in l:
        if i>m and i<kk:
            m=i
    print(m)
