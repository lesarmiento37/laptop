va = 0
var = []
var2 = []
var.append(0)
var.append(1)
vari = 0
cont = 0
print(var)
while True:
	#var.append(va)
	vari = var[va] + var[va + 1]
	var.append(int(vari))
	va +=1
	if (va == 1000):
		break

entra = int(input())
for n in range(0,entra):
	entrada = int(input())
	while True:
		if(var[cont] == entrada):
			var2.append(cont)
			break
		else:
			cont +=1
	cont = 0
print(*var2,sep=' ')
