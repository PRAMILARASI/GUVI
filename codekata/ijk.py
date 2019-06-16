k= int(input())
e= list(map(int,input().split()))
for i in range(0,k-2):
  for j in range(i+1,k-1):
    for k in range(j+1,k):
      if e[i]+e[j] == e[k]:
        print(e[i],e[j],e[k])
