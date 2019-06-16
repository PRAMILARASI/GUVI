n=str(input())
d=1
for i in range(len(n)-1):
    a=int(n[i]+n[i+1])
    if(a<=26 and n[i]!="0"):
        d=d+1
if(d==3):        
    print(d)
else:
    print(d+(d-1)//2) 
