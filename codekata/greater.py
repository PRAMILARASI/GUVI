x=int(input(""))
y=int(input(""))
z=int(input(""))
if((x>y)&(x>z)):
  greater=x
  print(greater)
elif((y>x)&(y>z)):
  greater=y
  print (greater)
else:
  greater=z
  print(greater)
