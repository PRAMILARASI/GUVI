s= input()
x1=""
x2=""
for i in range(0,len(s)):
  if(i%2!=0):
    x1=x1+s[i]
  else:
    x2=x2+s[i]
print(x2,x1)
