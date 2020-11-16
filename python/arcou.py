var = []
num = []
nume = []

def entry2(a,b):
	entra = input()
	entra2 = entra.split()
	for i in range (1, int(b)+1):
		nume.append(i)
	for z in range(0, len(nume)):
		conta = 0
		for f in range (0,int(a)):
			entra2[f] = int(entra2[f])
			if(nume[z] == entra2[f]):
				conta += 1
		var.append(conta)
	print(*var, sep = ' ')

print("ingrese")
entr = input()
entr2 = entr.split()

for n in range(0,2):
	num.append(entr2[n])
entry2(num[0],num[1])
