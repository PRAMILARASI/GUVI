x=int(input(""))
y=int(input(""))
z=int(input(""))
if((x>y)&(x>z)):
  largest=x
  print(largest)
elif((y>x)&(y>z)):
  largest=y
  print (largest)
else:
  largest=z
  print(largest)
