aa1 = int(input())
aa2 = list(map(int,input().split()))
for i in range(0,len(aa2)-1):
    print(max(aa2[i],aa2[i+1]),end=' ')
