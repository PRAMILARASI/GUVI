import math
aa,bb=input().split()
aa=int(aa)
bb=int(bb)
kk=(math.gcd(aa,bb))
print((aa*bb)//kk)
