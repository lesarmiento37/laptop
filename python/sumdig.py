ent2 = []
sumas = []
print("ingrese")
num = input()
num2 = int(num)
for i in range(0,num2):
	entrada = input()
	entrada2 = entrada.split()
	suma = 0
	for n in range(0,len(entrada2)):
		entrada2[n] = int(entrada2[n])
	num = entrada2[0]*entrada2[1] + entrada2[2]
	ent = str(num)
	for l in range(0,len(ent)):
		suma += int(ent[l])
	sumas.append(suma)
	print(*sumas, sep=' ')
	
