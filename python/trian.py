var = []

def triangle(a,b,c):
	if (b + c > a) and (a + b > c) and (a + c > b):
		var.append(1)
	else:
		var.append(0)

print("ingrese")
entr = input()
entr2 = int(entr)
for n in range(0, entr2):
	entra = input()
	entra2 = entra.split()
	for i in range(0, len(entra2)):
		entra2[i] = int(entra2[i])
	triangle(entra2[0],entra2[1],entra2[2])
print(*var, sep=' ')
