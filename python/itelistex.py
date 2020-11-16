import numpy as np
a = np.arange(1,11)
a = list(a)
k = 3
cont = 0
sorted = False

while not sorted:
	if len(a) == 1:
		print(a[0])
		sorted = True
	for  person in a[:]:
		cont += 1
		if cont == k:
			print
			a.remove(person)
			cont = 0
