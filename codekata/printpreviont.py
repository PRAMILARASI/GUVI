aa3 = int(input())
aa2 = list(map(int , input().split()))
for i in range(0,len(aa2)-1):
    if aa2 [i+1] % aa2[i] == 0:
        print(aa2[i+1],end=' ')
