string=input()
bb=''
for i in string:
    if i=="X":
        bb+="A"
    elif i=="x":
        bb+="a"
    elif i=="Y":
        bb+="B"
    elif i=="y":
         bb+="b"
    elif i=="Z":
        bb+="C"
    elif i=="z":
        bb+="c"
    else:
        bb+=chr(ord(i)+3)
print(bb)
