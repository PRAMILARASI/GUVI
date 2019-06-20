from collections import Counter
aa1 = list(input())
aa  = Counter(aa1)
if max(list(aa.values())) > 1:
    print("yes")
else:
    print("no")
