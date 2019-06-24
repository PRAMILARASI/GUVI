aa3 = int(input())
aa1 = list(map(int , input().split()))
aa2 = list(map(int , input().split()))
aa3 = aa2[:]
aa3.sort()
for i in aa3:
    print(aa1[aa2.index(i)],end=' ')
