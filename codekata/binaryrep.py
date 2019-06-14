x=input()
s=0
for i in x:
  if((i=='0')|(i=='1')):
    s=s+1
if(s==len(x)):
  print("yes")
else:
  print("no")
