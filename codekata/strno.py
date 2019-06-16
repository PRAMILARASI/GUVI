ab=list(input().split())
c=0
q = list(ab[0])
w = list(ab[1])
for i in range(0,min(len(q),len(w))):
    if q[i]!=w[i]: c=c+1
c=c+(len(q)-len(w))
if c==int(ab[2]):
  print("yes")
else:
  print("no")
