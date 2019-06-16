a=int(input())
ss=list(map(int,input().split()))
yy=sorted(ss)[::-1]
z=""
if(ss==[0]*a):
    print("0")
else:
    for j in yy:
        z=z+str(j)
    print(int(z))
