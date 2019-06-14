A=[int(x) for x in input().split()]
B=[int(x) for x in input().split()]
D=0
for x in B:
  if(x==A[1]):
    D=D+1
print(D)
