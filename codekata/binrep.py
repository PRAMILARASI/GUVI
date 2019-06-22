n1,pk=map(int,input().split())
k=n1*pk
s=bin(pk)
for  i in range(0,len(s)):
    if s[i]=='1':
        print(i+1)
        break
