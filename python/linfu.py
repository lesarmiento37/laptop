var = []
resp = []
print("ingrese")
entr = input()
entr2 = int(entr)

for i in range(0,entr2):
	entra = input()
	print("\n")
	entra2 = entra.split()
	a = 0
	b = 0
	for n in range(0,4):
		entra2[n] = int(entra2[n])
		var.append(entra2[n])
	a = int((var[3] - var[1])/(var[2] - var[0]))
	b = int(var[1] - a*var[0])
	c = str(a)
	d = str(b)
	e = "(" + c + " "+ d + ")"
	resp.append(e)
	var.clear()
	
print(*resp, sep = ' ')
