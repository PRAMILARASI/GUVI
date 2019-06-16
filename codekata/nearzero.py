x=int(input())
y=list(map(int,input().split()))
l=max(y)
ej,f=0,0
for i in range(0,len(y)):
  for j in range(i+1,len(y)):
    if abs(y[i]+y[j])<l:
      ej,f=y[i],y[j]
      l=abs(ej+f)
print(ej,f)
