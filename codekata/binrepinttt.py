aa1 = int(input())
aa2 = bin(aa1)[2:]
aa2 = aa2[::-1]
print(aa2.index('1')+1)
