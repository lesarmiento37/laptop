import numpy as np
print("ingrese")
var = []
resp = 0
entr = int(input())
for n in range (0,entr):
	entrada = input().split()
	entr = np.array(entrada)
	entr2 = entr.astype(int)
	#var.append(entr2)
	resp = entr2[3]
	for n in range(0,entr2[4]):
		resp = (entr2[0]*resp + entr2[1]) % entr2[2]
		print(resp)
	var.append(resp)
	resp = 0
	
print(*var, sep=' ')
