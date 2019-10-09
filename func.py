import math 
def fact(n):
	fact = 1
	for i in range(1,n+1):
		fact = fact*i
	return fact

def sins(n):
	return [(-1)**i*(n**(2*i+1))/fact(2*i+1) for i in range(75)]

x = float(input("enter x:")) * (math.pi/180)
print("my sine function ",sum(sins(x)))
print("math sine ",math.sin(x))
