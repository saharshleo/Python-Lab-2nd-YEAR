import random

n = int(input("Enter a number: "))
database = [[] for i in range(n)]
#for i in  range(n):
	
for i in range(n):
	database[i].append(i+1)
	
	name = chr(random.randint(65,90))
	name += random.choice(['a','e','i','o','u'])
	for j in range(10):
		name += chr(random.randint(97,122))
	database[i].append(name)
	
	email = chr(random.randint(65,122))
	for j in range(9):
		email += chr(random.choice([random.randint(97,122), random.randint(48,57)]))
	email += random.choice(['@gmail.com','@yahoo.in','@facebook.com'])
	database[i].append(email)
	
	age = random.randint(15,60)
	database[i].append(age)
	salary = random.randint(20000,1200000)
	database[i].append(salary)
	
print(database)
print("***************")
#average of salary
avg = reduce(lambda x,y:x+y, [database[i][4] for i in range(n)])
print("average salary is: ",avg/n)
print("***************")
# records with employee name with A
nameA = list(filter(lambda x: x[1][0]=='A', database))
print("names with A")
print(nameA)
print("***************")
#update salaries of age btw 18 -25
database = map(lambda x:x[:4]+[int(x[4] + 0.1*x[4]) if(x[3]>17 and x[3]<26) else x[4]],database)
print("updated salaries of age group 18-25")
print database
print("***************")
#records with max and min salary
max_salary = reduce(lambda x,y:x if(x[4]>y[4]) else y,database)
print("maximum salary record")
print max_salary
print("***************")
min_salary = reduce(lambda x,y:x if(x[4]<y[4]) else y,database)
print("minimum salary record")
print min_salary
print("***************")
#records with @gmail.com
email_update = list(filter(lambda x:(x[2][x[2].index('@'):]=='@gmail.com'), database))
print("records with @gmail.com")
print email_update
print("***************")








