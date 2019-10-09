import sys
n = int(sys.argv[1])
high = n
low = 1
mid = (high+low)//2
for a in range(1,30):
	mid = (high+low)//2
	if mid*mid > n:
		high = mid
	elif mid*mid < n:
		low = mid
	else:
		break
print("square root is" ,mid)
	
	

