nk=int(input())
l1=list(map(int,input().split()))
for i1 in range(0,len(l1)):
    if(l1[i1]%2==0 and i1%2!=0):
            print(l1[i1],end=" ")
    elif(l1[i1]%2!=0 and i1%2==0):
            print(l1[i1],end=" ")
