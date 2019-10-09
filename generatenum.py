import random
f = filter(lambda x : round(x - int(x),1) in [0.7,-0.7,0.8,-0.8,0.9,-0.9], [round(random.uniform(-10,10),1) for i in range(10)])

print(*f)
