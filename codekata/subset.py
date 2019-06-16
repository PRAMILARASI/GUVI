n,m= map(int,input().split())
s1={int(x) for x in input().split()}
s2={int(y) for y in input().split()}
if((s2.issubset(s1))):
  print("YES")
else:
  print("NO")
