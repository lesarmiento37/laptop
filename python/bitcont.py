import numpy as np
print("ingrese")
var = []
entra = int(input())
entrada = input().split()
entrada2 = np.array(entrada)
entrada3 = entrada2.astype(int)
cont = 0
for n in range(0,entra):
	if(entrada3[n] < 0):
		entr = entrada3[n] % 0x100000000
		entr6 = format(entr,'b')
		entr2 = str(entr6)
		entr5 = entr2.replace("-","1")
		entr3 = entr5.rjust(32,'1')
		entr4 = list(entr3)
		print(entr3)
		for i in range(0,len(entr4)):
			if(entr4[i] == '1'):
				cont += 1
		var.append(cont)
	else:
		entr = bin(entrada3[n]).replace("0b","")
		entr2 = str(entr)
		entr3 = entr2.rjust(32,'0')
		entr4 = list(entr3)
		print(entr3)
		for i in range(0,len(entr4)):
			if(entr4[i] == '1'):
				cont += 1
		var.append(cont)
	cont = 0	

print(*var, sep=' ')
