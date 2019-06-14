pp=list(map(int,input().split()))
j=0
k=0
while True:
   if (pp[1] * pp[0])  == (j*j):
       print("yes")
       k=k+1
       break
   if (pp[1] * pp[0]) < (j*j):
       print("no")
       break
   j=j+1
