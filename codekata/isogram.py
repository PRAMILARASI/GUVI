zaa=input()
zaa=list(zaa)
aa=0
for i in zaa:
      if(zaa.count(i)==2):
          aa=aa+1
if(aa==0):
     print("Yes")
else:
     print("No")
