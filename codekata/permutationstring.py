from itertools import permutations
sa=str(input())
s1=permutations(sa)
for i in list(set(s1)):
    print(''.join(i)
