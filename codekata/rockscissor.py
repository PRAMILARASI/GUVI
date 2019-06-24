aa1,ba=map(str,input().split())

if aa1==ba:

	print("D")

elif (aa1=="R" and ba=="P") or (aa1=="P" and ba=="R"):

	print("P")

elif (aa1=="S" and ba=="P") or (aa1=="P" and ba=="S"):

	print("S")

elif (aa1=="S" and ba=="R") or (aa1=="R" and ba=="S"):

	print("R")
