import math
def prime(aa1):
  x=0
  if aa1 == 2 and aa1 == 3:
    return True
  for i in range(2,int(math.sqrt(aa1))+1):
    if aa1%i==0:
      return False
      x=x+1
      break
  if x==0:
    return True

a3=int(input())
for i in range(2,100+1):
  if a3 % i == 0:
    if prime(i):
      print(i,end=' ')
