sd1=[]
c=0
b=int(input())
a=input().split()
for i in a:
  sd1.append(int(i))
#print(s1)
for i in range(b-1):
  c=c+sd1[i]+sd1[i+1]
print(c)
