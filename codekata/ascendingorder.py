import math
aa4 =list(map(int , input().split()))
aa1 = list(map(int , input().split()))
aa2 = aa1[0:a4[1]]
aa2.sort()
aa3 = aa1[aa4[1]:len(aa1)]
aa3.sort(reverse = True)
print(' '.join(map(str,aa2+aa3)))
