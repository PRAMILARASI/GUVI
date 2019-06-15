a3 = list(map(int,input().split()))
aa = list(map(int,input().split()))
l=[]
for i in range(0,len(aa)):
    if aa[i]%2 !=0:
        l.append(aa[i])
print(l[a3[1]-1])
