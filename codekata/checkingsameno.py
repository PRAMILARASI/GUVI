a,b=input().split()
if len(a)==len(b):
	print(a+b)
elif len(a)>len(b):
	cd=a[:len(b)]+b
	print(cd)
else:
	cd=a+b[:len(a)]
	print(cd)
