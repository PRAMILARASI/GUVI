an,a=map(str,input().split())

g=abs(len(an)-len(a))

for i in range(len(an)):

        if len(a)==1 and a[i] in n:

            break

        if an[i]!=a[i]:

            g=g+1

print(g)
