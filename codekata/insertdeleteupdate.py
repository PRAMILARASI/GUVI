na1,na2=input().split()

t=abs(len(na1)-len(na2))

for v in range(len(na1)):

    if len(na2)==1 and na2[v] in n1:

        break

    if na1[v]!=na2[v]:

        t+=1

print(t)
