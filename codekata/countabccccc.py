aa1 = input()
if (aa1.count('a')+aa1.count('b') == len(aa1)) or aa1.count('a') == len(aa1) or aa1.count('b') == len(aa1) or (len(aa1)) -(aa1.count('a')+aa1.count('b')) == 1:
    print("yes")
else:
    print("no")
