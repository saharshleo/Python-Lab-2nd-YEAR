dataset = []
file = open("avocado.csv", "r")
line = file.readlines()
for l in line:
	word = l.split(",")
	word[-1] = word[-1][:-1]
	dataset.append(word)
for i in dataset:
	print(i)
sum = 0
count = 0
for i in dataset:
	if i == dataset[0]:
		continue
	sum += float(i[2])
	count += 1
avg = sum/count
print("average price: ", avg)
file.close()
