I,J=map(int,input().split())
G=list(map(int,input().split()))
Ln=[]
for j in G:
    if(j%2!=0):
        Ln.append(V)
print(Ln[J-1])
