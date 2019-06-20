aa1= int(input())
aa2 = list(map(int,input().split()))
x=aa2[0]
for i in range(1,len(aa2)):
    x= x | aa2[i]
print(x)
