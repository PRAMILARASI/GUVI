n1=int(input())
r1=[]
aa1=0
count=0
for i in range(n1):
  c=input()
  r1.append(c)
for i in r1:
  for j in i:
    aa1+=ord(j)
  if(aa1==612):
    count+=1
  aa1=0
print(count)
