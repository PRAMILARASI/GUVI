m,e=input().split()
count=0
for i in range(0,len(m)):
  
  
  if(m[i]!=e[i]):
    count=count+1
if(count==1):
  print("yes")
else:
  print("no")
