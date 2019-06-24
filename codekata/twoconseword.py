aa1 = int(input())
aa2 = []
aa2.append(input())
x=0
for i in range(1,aa1-1):
    aa2.append(input())
    if aa2[i] == aa2[i-1]:
        print("yes")
        x= x+1
        break
if x == 0:
    print("no")
