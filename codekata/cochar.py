n=input()
co=0
for i in n:
  if(i.isalnum() or (i==' ')):
    co+=0
  else:
    co+=1
print(co)
