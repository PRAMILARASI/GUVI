def lcm(xx,yy):
  if xx>yy:
    g = xx
  else:
    g=yy
  while (True):
    if (g % xx == 0) and (g % yy ==0):
      lcm = g
      break
    g=g+1
  return lcm
  
a1 =  int(input())
a2 = list(map(int,input().split()))
xx=a2[0]
for i in range(1,len(a2)):
  xx=lcm(xx,a2[i])
print(xx)
