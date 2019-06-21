aa1 = input().split()
for i in range(0,len(aa1[0]),int(aa1[1])):
    print(aa1[0][int(aa1[1])+i-1],end=' ')
