def fact(x):

    a=1

    for i in range(1,x+1):

        a=a*i

    return a





aa1 = list(map(int,input().split()))

print(int(fact(aa1[0])/fact(aa1[1])))
