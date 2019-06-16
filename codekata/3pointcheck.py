a1=input().split()
b1=input().split()
c1=input().split()
if(a1[0]==b1[0]==c1[0] or a1[1]==b1[1]==c1[1] or (a1[0]==a1[1] and b1[0]==b1[1] and c1[0]==c1[1])):
    print('yes')
else:
    print('no')
