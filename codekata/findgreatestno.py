aa,bb=map(int,input().split())
L=[]
for i in range(1,bb+1):
    if(aa%i==0 and bb%i==0):
        L.append(i)
print(max(L))
