import math
var = []
print("ingrese",end="\n")
entrada = int(input())

for i in range(0,entrada):
	x,nu = input().split()
	x,nu = int(x),int(nu)
	r = 1
	d = x / r
	ent = 0
	dec = 0
	for n in range (0,nu):
		r = (r + d) / 2
		d =  x / r
		dec,ent = math.modf(r)
		#print(ent,dec)
	if(dec == 0.00):
		#print("entero",end="\n")
		var.append(int(r))
	else:
		#print("decimal",end="\n")
		var.append(round(r,9))
	print(*var,sep=' ')
