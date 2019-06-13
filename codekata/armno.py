x,y=(input().split())
x=int(x)
y=int(y)
for i in range(x,y):
  sum=0
  temp=i
  while(temp>0):
    d=temp%10
    sum+=d**3
    temp//=10
    if(i==sum):
      print(i,end=' ')
