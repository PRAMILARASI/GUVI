aa2 = list(map(int,input().split()))
aa2 = aa2[0] * aa2[1]
aa3 = bin(aa2)[2:]
aa3 = aa3[::-1]
print(aa3.index('1')+1)
