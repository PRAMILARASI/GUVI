kd=int(input())
if kd>1:
  for i in range(2,kd):
    if(kd%i)==0:
      print("no")
      break
  else:
      print("yes")
    
else:
   print("no")
