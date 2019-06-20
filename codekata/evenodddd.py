aa2 = int(input())
aa1 =list(map(int,input().split()))
l,l1=[],[]
for i in aa1:
    if i % 2 == 0:
        l.append(i)
    else:
        l1.append(i)
if len(l) == 1:
    print(l[0])
else:
    print(l1[0])
