aa1 =list(map(int,input().split()))
aa2 = []
aa2.append(input())
x=1
k=0
for i in range(1,aa1[0]):
    aa2.append(input())
    if aa2[i] == aa2[i-1]:
        x= x+1
    else:
        x = 1
    if x == aa1[1]:
        print("yes")
        k = k+1
        break

if k == 0:
    print("no")
