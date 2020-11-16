import numpy as np
var = []
print("ingrese")
entra = int(input())
for n in range(0,entra):
	entr = input().split()
	entr2 = np.array(entr)
	entr3 = entr2.astype(int)
	t = (entr3[0])/(entr3[1] + entr3[2])
	entr4 = entr3[1]*t
	i,d = divmod(entr4,1)
	if(d == 0):
		var.append(int(entr4))
	else:
		var.append(entr4)
	
print(*var,sep=' ')
