import numpy as np
var = []
def operacion(ent,esc):
	if (ent > 0):
		variable = list(esc)
		variable2 = variable[ent:len(variable)] + variable[0:ent]
		varia = ""
		return (varia.join(variable2))
	else:
		variable3 = list(esc)
		variable4 = variable3[ent:] + variable3[0:ent]
		varia2 = ""
		return (varia2.join(variable4))
	
print("input:")
nume = int(input())
for n in range(0,nume):
	rawvar = input().split()
	rawvari = int(rawvar[0])
	rawvars = rawvar[1]
	var.append(operacion(rawvari,rawvars))
print(*var,sep=' ')
	

