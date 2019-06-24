s1=input()

kk=""

for i in s1:

	if s1.count(i)>1:

		kk=kk+i.upper()

	else:

		kk=kk+i

print(kk)
