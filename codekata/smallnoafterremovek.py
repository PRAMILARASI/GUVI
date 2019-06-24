from itertools import combinations

ax,y=map(int,input().split())

g=len(str(ax))

a=list(combinations(str(ax),g-y))

a=(sorted(a))

l="".join(a[0])

print(l)
