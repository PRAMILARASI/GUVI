na1=int(input())

l=[]

s=1

k=1

for i in range(0,na1):

    l.append(list(map(int,input().split())))

for i in range(0,na1):

    for j in range(0,na1):

        if i==j:

            s=s*l[i][j]

        if i+j==na1-1:

            k=k*l[i][j]

print(s+k)
