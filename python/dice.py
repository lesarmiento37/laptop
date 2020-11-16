import math
var = []

print("ingrese")
entr = input()
entr2 = int(entr)
for n in range(0,entr2):
	entra = input()
	entra2 = float(entra)
	entra3 = entra2*6 + 1
	entra4 = math.floor(entra3)
	var.append(entra4)
print(*var,sep=' ')
