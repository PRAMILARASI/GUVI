aa1 = int(input())
aa2 = list(map(int,input().split()))
if len(aa2) % 2 ==0:
    for i in range(0,len(aa2),2):
        print(aa2[i+1],aa2[i],end=' ')
else:
    for i in range(0,len(aa2)-2,2):
        print(aa2[i+1],aa2[i],end=' ')
    print(aa2[len(aa2)-1])
