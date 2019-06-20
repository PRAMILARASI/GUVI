aax=list(map(int,input().split()))
bbx=list(map(int,input().split()))
x=aax[1]
c=0
for i in range(0,len(bbx)):
    for j in range(i+1,len(bbx)):
        if bbx[i]+bbx[j]==x:
            c=1
            break
if c==1:
    print('yes')
else:
    print('no')
