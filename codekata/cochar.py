n=input()
count=0
for i in n:
  if(i.isalnum() or (i==' ')):
    count+=0
  else:
    count+=1
print(count)
