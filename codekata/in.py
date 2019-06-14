aa=list(input())
if len(aa)%2==0:
   aa[int(len(aa/2))] ='*'
   aa[int(len(aa)/2)-1] = '*'
else:
   aa[int(len(aa)/2)]='*'
for i in range(0,len(aa)):
    print(aa[i],end='')
    

