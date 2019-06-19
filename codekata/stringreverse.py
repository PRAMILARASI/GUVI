s, i = list(map(str,input().split()))
i = int(i)
for j in range(i):
  s1 = ""
  s1 += s[-1]
  for j in range(len(s)-1):
    s1 += s[j]
  s = s1
print(s)
