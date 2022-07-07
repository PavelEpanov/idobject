objects = [1, 2, 1, 2, 3]
L = set()
for obj in objects:
	if obj not in L:
		L.add(id(obj))

print(L)
