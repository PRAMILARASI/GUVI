
i=0
aa1 = int(input())
while True:
    if aa1 == (2**i):
        print("yes")
        break
    if aa1 < (2**i):
        print("no")
        break
    i = i+1
