#Crear la funcion pares que devuelva un array de numeros entre dos valores pasados como parametros aa
#la funcion inicio fin

import numpy as np

def pares(inicio, fin):
	if (inicio % 2 == 0):
		array = np.arange(inicio,fin,2)
	else:
		inicio +=1
		array = np.arange(inicio,fin,2)
	return array

print("numero")	
#pares(1,30)
print(pares(1,30))
print(pares(2,40))
#pares(2,40)
#print(pares)

