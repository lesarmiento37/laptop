print("ingrese")
def metodo(inputs):
	var = []
	for n in [int(i) for i in input().split()]:
		cont = 0
		entr = n*n
		s = ''
		arre = [str(n)]
		igual = True

		while igual:
			if cont != 0:
				entr = int(entr)**2

			entr = str(entr)

			while (len(entr) < 8):
				entr = '0' + entr
			entr = entr[2:-2]

			cont += 1
	
			if entr in arre:
				igual = False

			arre.append(entr)
		var.append(str(cont))
         
	print(*var,sep = ' ')

metodo(input())
