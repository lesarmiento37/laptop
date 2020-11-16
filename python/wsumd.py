var = []
vari = []
entrada = []
ena = []
	

print("ingrese")
entra = input()
entra2 = int(entra)
entr = input()
entr2 = entr.split()
for n in range(0,entra2):
	entrada = entr2[n]
	for f in range(0,len(entr2[n])):
		suma = 0
		multi = 0
		vari = int(entrada[f]) * (f + 1)
		var.append(vari)
	for g in range(0,len(var)):
		suma += var[g]
	ena.append(suma)
	var.clear()
print(*ena, sep=' ')
		
