import math
var = []
ave = []
aver = []
def arreglo(a):
	suma = 0
	promedio = 0
	for f in range(0,len(a)):
		suma += a[f]
		promedio = suma/(len(a)-1)
	ave.append(round(promedio))
	print(*ave, sep=' ')
	
print("ingrese")
entr = input()
entr2 = int(entr)
for n in range(0,entr2):
	vari = input()
	vari2 = vari.split()
	for i in range(0, len(vari2)):
		vari2[i] = int(vari2[i])
	arreglo(vari2)		
