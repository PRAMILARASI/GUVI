g=input()
u=0
for i in range(0,len(g)):
  if g[i].isdigit():
    u=u+1
    break
for i in range(0,len(g)):
  if g[i].isalpha():
    u=u+1
    break
if(u==2):
  print("Yes")
else:
  print("No")
