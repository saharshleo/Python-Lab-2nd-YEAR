import sys
x = int(sys.argv[1])
flag = False
if x ==1:
	print("square of 1")
else:
	for a in range(1,x//2 + 1,1):
		if x/a == a:
			flag = True
			break
	if flag == True:
		print("square of", a)
	else:
		print("not a square")
