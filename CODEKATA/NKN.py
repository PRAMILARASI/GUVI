N=[int(x) for x in input().split()]
K=[int(x) for x in input().split()]
D=0
for x in K:
  if(x==N[1]):
    D=1
if(D==1):
  print("yes")
else:
  print("no")
