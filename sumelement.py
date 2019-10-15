def sum(arr,size):
	s=0
	if size ==2:
		return arr[0]+arr[1]
	else:
		s = arr[size-1]+sum(arr,size-1)	
		return s
	 
size = int(input("enter size:"))
arr = []
for i in range(size):
	arr.append(i)
print("sum is",sum(arr,size))



