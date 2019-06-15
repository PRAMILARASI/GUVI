nn=int(input())
aa1=list(map(int,input().split()))
for i1 in range (0,nn-1):
    if(aa1[i1]!=i1+1):
        print(i1)
        break
