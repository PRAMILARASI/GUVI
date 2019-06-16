str=input()
l=list(str)
if(l[0]=='(' and l[-1]==')'):
    if(l.count('(')==l.count(')')):
        print("yes")
    else:
        print("no")
else:
    print("no")
