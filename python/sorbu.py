vari = []
print("ingrese")
orga = False
entra = int(input())
entra2 = input().split()
for n in range(0,entra):
	entra2[n] = int(entra2[n])
	vari.append(entra2[n])
	contas = 0
	contap = 0
while not orga:
	orga = True
	for n in range(entra - 1):
		if (vari[n] > vari[n + 1]):
			orga = False
			contas += 1
			vari[n],vari[n + 1] = vari[n + 1], vari[n]
	contap += 1

print("{} {}".format(contap,contas))
