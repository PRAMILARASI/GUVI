a=int(input())
for i in range(1,a+1):
    if(a%i==0 and i%2!=0):
        print(i,end=" ")
