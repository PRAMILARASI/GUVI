n1,kk=map(int,input().split())
l=[int(x) for x in input().split()]
a=l[:kk]
b=l[kk:]
a.sort()
b.sort(reverse=True)
print(*a,*b)
