n=int(input())
M=list(map(int,input().split()))
for i in range(n):
  print(M[i],M.index(M[i]))
