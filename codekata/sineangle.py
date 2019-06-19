import math 
d=float(input())
m1=math.radians(d)
n=math.sin(m1)
if(m1<1):
    print(round(n,1))
elif(m1>1):
    print(round(n))
