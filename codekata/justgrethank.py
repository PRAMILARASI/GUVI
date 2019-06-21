n1,kk=map(int,input().split())
l=[int(x) for x in input().split()]
l.sort()
for i in l:
    if i>kk:
        print(i)
        break
