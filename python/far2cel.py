import math
print("ingrese valor")
grado = input()
grado2 = grado.split()
grado3 = []
for i in range(0,len(grado2)):
	grado4 = 0
	grado2[i] = int(grado2[i])
	grado4 = (grado2[i] - 32)/1.8
	grado3.append(round(grado4))
print(*grado3 , sep=(' '))
