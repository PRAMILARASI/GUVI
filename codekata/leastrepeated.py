import string
abc=input()
abc.split()
abc=abc.replace(" ","")
b=[i for i in abc if abc.count(i)==1]
c=' '.join(b)
print(c.lower())
