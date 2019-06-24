s1=input()

l=['a','e','i','o','u']

ac=[]

bc=[]

for i in s1:

	if i in l:

		ac.append(i)

	else:

		bc.append(i)

print("".join(ac+bc))
