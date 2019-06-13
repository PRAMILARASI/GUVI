m,n=input().split()
m= int(m)
n=int(n)
for i in range(m+1,n):
  if i>1:
    for k in range(2,i):
      if(i%k)==0:
        break
    else:
      print(i,end=' ')
