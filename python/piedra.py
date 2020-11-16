import numpy as np
var = []
print("ingrese")
def ppt(ent):
	cont1 = 0
	cont2 = 0
	for i in range(0,len(ent)):
		if((ent[i] == 'SS')or(ent[i] == 'PP')or(ent[i] == 'RR')):
			cont1 += 0
			cont2 += 0
		elif((ent[i] == 'PR')or(ent[i] == 'SP')or(ent[i] == 'RS')):
			cont1 += 1
			cont2 += 0
		elif((ent[i] == 'RP')or(ent[i] == 'PS')or(ent[i] == 'SR')):
			cont1 += 0
			cont2 += 1
	return cont1,cont2
	cont1 = 0
	cont2 = 0

entra = int(input())
for n in range(0,entra):
	entr = input().split()
	j1,j2 = ppt(entr)
	if(j1 < j2):
		var.append("2")
	else:
		var.append("1")

print(*var,sep=' ')
