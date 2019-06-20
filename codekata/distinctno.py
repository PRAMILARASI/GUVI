x=int(input())
l=list(map(int,input().split()))
cs=0
for i in range(x-1):
    for j in range(i+1,x):
        if(l[i]<l[j]):
            cs=cs+1
print(cs)
