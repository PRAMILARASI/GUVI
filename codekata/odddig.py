nk1=input()
c=0
for i in range(0,len(nk1)):
    if int(nk1[i])%2==1:
        c=c+int(nk1[i])
if c%2==0:
    print("E")
else:
    print("O")
