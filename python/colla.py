var = []
conta = 0

print("ingrese")
numeo = input()
numeo2 = int(numeo)
numero = input()
numero2 = numero.split()
for n in range(0,numeo2):
	num = int(numero2[n])
	while num != 1:
		if ((num % 2) ==  0):
			num /= 2
			conta += 1
		else:
			num = 3*num + 1
			conta += 1
	
		if(num == 1):
                	break

	var.append(conta)
	conta = 0

print(*var, sep = ' ')
