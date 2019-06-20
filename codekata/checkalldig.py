aa1 = input().split()

if max(list(map(int,list(aa1[0][0:int(aa1[1])-1])))) < int(aa1[1]):
    print("yes")
else:
    print("no")
