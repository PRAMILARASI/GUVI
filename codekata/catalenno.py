def catalan(n1):

  if n1<=1:

    return 1

  else:

    rp=0

    for i in range(n1):

      rp+=catalan(i)*catalan(n1-i-1)

    return rp

n1=int(input())

if n1<=1:

  n1+=1

else:

  n1=n1

li=[]

for i in range(n1):

  li.append(catalan(i))

print(*li)
