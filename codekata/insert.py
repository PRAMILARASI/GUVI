n=list(input())
if len(n)%2==0:
    n[int(len(n)/2)] ='*'
    n[int(len(n)/2)-1]='*'
else:
    n[int(len(n)/2)] ='*'
for i in range(0,len(n)):
    print(n[i],end='')
