def fact(xn):
    a=1
    for i in range(1,xn+1):
        a=a*i
    return a
a1 = list(map(int,input().split()))
print(int(fact(a1[0])/fact(a1[0]-a1[1])))
