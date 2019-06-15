M=input()
l=[]
for j in M:
    if(j.isdigit())==True:
        l.append(j)
print(*l,sep="")
