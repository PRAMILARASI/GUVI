a=input() 
kj=a[0]
for i in a:
  if(a.count(kj)<=a.count(i)):
    kj=i
print(kj)
