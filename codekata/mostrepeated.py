sk=input()
p=[]
for i in sk:
    p.append(sk.count(i))
k=max(p)
out=[]
for i in range(len(p)):
    if p[i]==k:
        o=i
        out.append(sk[o])

out=set(out)
print(k,end=" ")
for i in out:
    print(i,end="")
