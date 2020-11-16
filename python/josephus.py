import numpy as np
print("ingrese")
n,k = input().split()
n,k = int(n),int(k)
vec = np.arange(1,n+1)
vec = list(vec)
orga = False
cont = 0

while not orga:
	if len(vec) == 1:
		print(vec[0])
		orga = True
	for i in vec[:]:
		cont += 1
		if (cont == k):
			vec.remove(i)
			cont = 0			


