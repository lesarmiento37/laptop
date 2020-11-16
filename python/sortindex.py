var = []
entradas = []
diccionario = {}
entradasp = []
salida = []

print("ingrese")
entra = int(input())
entrada = input().split()
for n in range(0,entra):
	entrada[n] = int(entrada[n])
	entradas.append(entrada[n])
	entradasp.append(entrada[n])
sort = False
num = 0
while not sort:
	sort = True
	for i in range(0,entra - 1):
		if(entradas[i] > entradas[i+1]):
			sort = False
			entradas[i],entradas[i + 1] = entradas[i + 1],entradas[i]
print(entradas)
for f in range(1,entra + 1):
	var.append(f)
for n in range(0,entra):
	diccionario[entradasp[n]] = var[n]
for h in range(0,entra):
	salida.append(diccionario[entradas[h]])
print(*salida,sep=' ')
#print(diccionario)
