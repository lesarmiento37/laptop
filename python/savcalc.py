import numpy as np
var = []
print("ingrese")
entra = int(input())
for n in range(0,entra):
	entr = input().split()
	entr2 = np.array(entr)
	entr3 = entr2.astype(int)
	cont = 0
	ini = entr3[0]
	fin = entr3[1]
	tasa = entr3[2]*0.01
	while True:
		cont += 1
		ini += ini*tasa
		print(ini)
		if(ini > fin):
			break 
	var.append(cont)
print(*var,sep=' ')
