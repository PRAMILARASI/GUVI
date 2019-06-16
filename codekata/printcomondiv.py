Ll,Rr=map(int,input().split())
z=100000
S=[]
for i in range(1,z+1):
    if i%Ll==0 and i%Rr==0:
        S.append(i)
print(min(S))
