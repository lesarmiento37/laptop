print("ingrese")
entr = int(input())
var = []
for i in range(0,entr):
	x,y,n = input().split()
	x,y,n = int(x),int(y),int(n)
	cont = 0
	hoja = 0
	contx = 0
	conty = 0
	vecesx = 1
	vecesy = 1
	estado = False
	while not estado:
		cont += 1
		if cont == vecesx*x:
			contx += 1
			vecesx += 1
		if cont == vecesy*y:
			conty += 1
			vecesy += 1
		hoja = contx + conty
		if(hoja >= n):
			estado = True
	var.append(cont)
	cont = 0
	hoja = 0
	vecesx = 1
	vecesy = 1
print(*var,sep=' ')	
