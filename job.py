import random
size = 20
#n = int(input("Enter a number: "))
database = [i+1 for i in range(1000)]
#print database
jobdata = [[database.pop(random.randint(0,len(database)-1))] for i in range(size)]
#print jobdata
for i in range(len(jobdata)):
	name = chr(random.randint(65,90))
	for j in range(2):
		name += chr(random.randint(97,122))
	jobdata[i].append(name)
	jobdata[i].append(random.randint(1,24))
	jobdata[i].append(random.randint(10,100))
	#print jobdata[i]
for i in range(size): 
	for j in range(size - 1 - i): 
		if jobdata[j][3] < jobdata[j + 1][3]: 
			jobdata[j], jobdata[j + 1] = jobdata[j + 1], jobdata[j] 
print jobdata
print '****************'
arr = [[0 for i in range(3)] for j in range(24)]
flag = 0
#flag = [0] * len(jobdata) 
for i in range(len(jobdata)):
	for j in range(3):
		if arr[jobdata[i][2]-1][j]==0:
			arr[jobdata[i][2]-1][j] = jobdata[i][3]
			flag = 1
			break
	if flag==0:
		for k in range(i,0):
			for j in range(3):
				if arr[jobdata[i][2]-1][j]==0:
					arr[jobdata[i][2]-1][j] = jobdata[i][3]
					flag = 1
					break
	flag = 0		
result = 0
for i in range(24):
	for j in range(3):
		result = result + arr[i][j]

print result




