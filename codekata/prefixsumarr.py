nu=int(input())
lu=[int(x) for x in input().split()]
p=[]
for i in range(nu):
    tc=lu[:i+1]
    if sum(tc)%2==0:
        p.append(str(sum(tc)))
    else:
        p.append(str(lu[i]))
print(" ".join(p))
