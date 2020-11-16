#crear la funcion primos quie sera una funcion generadora de primos entre el 0 y 100

numeros_primos = [2,3,5,7,11,13,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

def primos(maximo):
	for numero in range(maximo):
		if (numero in numeros_primos): # obtiene numeros hasta el 50 y verifica
			yield numero # genera ese numero con respuesta a la funcion
		if (numero > 100):  # si supera al 100 se acaba el bucle
			break
			
maximo = 50
for numero in primos(maximo):
	print(numero)

