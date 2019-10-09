V = {1,2,3,4,5,6,7}
E = {(1,3),(2,4),(6,7),(2,5),(1,4),(2,3),(5,7),(2,6)}
#count = 0
ls = []
cycle = 0
for e in E:
	if e[0] in V:
		V.discard(e[0])
		if e[1] in V:
			V.discard(e[1])
			ls.append({e[0],e[1]})
			print(ls)
			#count+=1
		else:
			for s in ls:
				if e[1] in s:
					s = s|{e[0]}
					
	elif e[1] in V:
		for s in ls:
			if e[0] in s:
				s = s|{e[1]}	
	else:
		for s in ls:
			if (e[0] in s) and (e[1] in s):
				cycle+=1
			elif e[0] in s:
				s1 = s
				ls.remove(s)
				for k in ls:
					if e[1] in ls:
						s2 = k
						ls.remove(k)
						ls.append(s1|s2)
print(cycle)
