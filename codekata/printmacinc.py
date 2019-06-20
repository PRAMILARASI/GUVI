aa=int(input())
l=list(map(int,input().split()))
cc=1
p=[]
for i in range(0,len(l)-1):
        if l[i]<l[i+1]:
                cc=cc+1
        else:
               p.append(cc)
               cc=1
p.append(cc)
print(max(p))
