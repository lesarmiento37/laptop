var = []
def media(a,b,c):
	if ((a < b) and (a > c)) or ((a > b) and (a < c)):
		var.append(a)
		#print(a)
	elif ((b < a) and (b > c)) or ((b > a) and (b < c)):
		var.append(b)
		#print(b)
	elif ((c < a) and (c > b)) or ((c > a) and (c < b)):
		var.append(c)
		#print(c)

print("ingrese")
entr = input()
entr2 = int(entr)

for i in range(0,entr2):
	entr3 = input()
	entr4 = entr3.split()
	for n in range(0, len(entr4)):
		entr4[n] = int(entr4[n])
	media(entr4[0],entr4[1],entr4[2])

print(*var, sep=' ')
