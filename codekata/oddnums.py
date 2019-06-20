n,m=map(int,input().split())
cd=[]
for i in range(n,m+1):
    if(i%2!=0):
        cd.append(i)
print(sum(cd)) 
