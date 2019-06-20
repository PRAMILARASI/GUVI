aa2= int(input())
aa3 = list(map(int,input().split()))
x=aa3[0]
for i in range(1,len(aa3)):
x= x | aa3[i]
print(x)
