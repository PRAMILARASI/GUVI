st1=input()

na=len(st1)

c=0

for i in range(len(st1)-1):

    if st1[i]!=st1[na-i-1]:

        c=c+1

if c<=1:

    print('yes')

else:

    print('no')
