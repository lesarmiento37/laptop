import math
print("ingrese")
var = []
entra = int(input())
for n in range(0,entra):
	x1,y1,x2,y2,x3,y3 = input().split()
	x1,y1,x2,y2,x3,y3 = int(x1),int(y1),int(x2),int(y2),int(x3),int(y3)
	a = math.sqrt((abs(x2-x1)**2 + abs(y2-y1)**2))
	b = math.sqrt((abs(x3-x2)**2 + abs(y3-y2)**2))
	c = math.sqrt((abs(x3-x1)**2 + abs(y3-y1)**2))
	are = (1/4)*math.sqrt(4*math.pow(a,2)*math.pow(b,2)-(a**2+b**2-c**2)**2)
	#abajo esta la linea que pone el formato de los floats
	arer = '{0:.7f}'.format(are).rstrip('0').rstrip('.')
	var.append(arer)
print(*var,sep=' ')
