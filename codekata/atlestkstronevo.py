#s
n,k=map(int,input().split())
l=[]
a=['a','e','i','o','u']
cd=1
for i in range(n):
	s=input()
	l.append(s)
	if k!=0:
		for i in s:
			if i in a:
				cd=1
				break
			else:
				cd=0
		k=k-1
	    
if cd==1:
    print("yes")
else:
    print("no")
