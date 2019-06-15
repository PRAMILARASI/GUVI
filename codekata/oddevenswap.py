st1=input()
for i in range(len(st1)):
    if i%2==0:
        print(st1[i+1],end='')
    else:
        print(st1[i-1],end='')
