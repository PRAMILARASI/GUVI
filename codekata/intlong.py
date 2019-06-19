xy=int(input())
if(xy>=-2**15+1 and xy<=2**15+1):
    print("INT")
elif(xy>=-2**31+1 and xy<=2**31+1):
    print("LONG")
else:
    print("LONG LONG")
