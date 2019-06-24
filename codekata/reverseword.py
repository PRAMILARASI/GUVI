aa1 = input().split()

for i in range(0,len(aa1)):

    if i == 0 or (len(aa1) -1) == i:

        print(aa1[i],end=' ')

    else:

        print(aa1[i][::-1],end=' ')

        
