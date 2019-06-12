p,q=input().split()
p=int(p)
q=int(q)
r=0
array=[int(x) for x in input().split()]
for i in range(0,q):
  r=r+array[i]
  print(r)
