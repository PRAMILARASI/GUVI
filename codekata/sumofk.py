a,b=input().split()
a=int(a)
b=int(b)
r=0
array=[int(x) for x in input().split()]
for i in range(0,b):
  r=r+array[i]
  print(r)
