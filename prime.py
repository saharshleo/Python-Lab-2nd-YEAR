n=int(input("enter a no. "))
num=[]
for i in range(n):
	num.append(i+1)
if n==1:
	print("neither prime nor composite")
else:
	for i in range(2,n):
		for j in range(i+1,n):
			if num[j-1]!=0 and j%i==0:
					num[j-1]=0
	for i in range(1,n):
		if num[i]!=0:
			print(i+1,end=" ")	
			
			
			
			
			
			
