a=int(input())
n=list(map(int,input().split()))
i=0
s=1
m=1
while i<a-1:
  if(n[i]==n[i+1]):
    s=s+1
    if s>m:
      m=s
  else:
    s=1
  i+=1
print(m)
