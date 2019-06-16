aa1 = list(map(int,input().split()))
aa2 = list(map(int,input().split()))
for i in range(0,len(aa2)):
    print(aa2[(((len(aa2)-aa1[1])+i)%len(aa2))],end=' ')
