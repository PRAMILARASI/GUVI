try:

	b,h=map(int,input().split())

	print(int(0.5*b*h))

except ValueError:

	print("invalid")
