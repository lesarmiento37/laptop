var = []
print("ingresar")
entr = input()
entra = int(entr)
salida = 0

def operacion(a,b,c):
        suma = 0
        for i in range(c):
                suma += a + i*b
        var.append(suma)


for n in range(0,entra):
	entrada = input()
	entrada2 = entrada.split()
	for f in range(0,len(entrada2)):
		entrada2[f] = int(entrada2[f])
	operacion(entrada2[0],entrada2[1],entrada2[2])
print(*var,sep=' ')

