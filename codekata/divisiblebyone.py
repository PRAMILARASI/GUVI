x=int(input())
d=0
for i in range(2,x):
    if(x%i==0):
        d=d+1
if(d>=1):
    print("yes")
else:
    print("no")
