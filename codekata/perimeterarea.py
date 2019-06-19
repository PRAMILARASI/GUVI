n2,k=map(int,input().split())
p=(n2//2)-1
for i in range(1,p+1):
  if i*p==k:
    print("yes")
    break
  else:
    p-=1
else:
  print("no")
