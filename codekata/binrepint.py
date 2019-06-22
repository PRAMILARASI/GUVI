n1,pk=map(int,input().split())
r=n1*pk
s=bin(r)[2::]
a=s[1:]
b=a.index("1")
print(b+2)
