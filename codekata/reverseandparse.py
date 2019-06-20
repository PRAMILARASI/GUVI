ax=input()
bx=''
for i in range(1,len(ax)):
    bx+=ax[-i]+"-"
print(bx+ax[0])
