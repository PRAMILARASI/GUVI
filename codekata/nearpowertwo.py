wsa=input()

wnb=int(wsa,2)

wx=wnb

while 1:

	if wx&(wx-1):

		wx=wx+1

	else:

		print(wx)

		break
