import numpy as np
entra = int(input())
var = []
entr = input().split()
entr2 = np.array(entr)
entr3 = entr2.astype(float)
var.append(entr3[0])
for n in range(1,entra - 1):
	vari = (entr3[n-1] + entr3[n] + entr3[n + 1])/3
	#vari2 = np.round(vari,2)
	var.append(vari)
var.append(entr3[entra - 1])
print(*var,sep=' ')
