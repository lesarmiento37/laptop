var = []

def body(w,h):
	bmi = w/(h**2)
	if (bmi < 18.5):
		var.append("under")
	elif (18.5 <= bmi) and (bmi < 25):
		var.append("normal")
	elif (25 <= bmi) and (bmi < 30):
		var.append("over")
	else:
		var.append("obese")
	

print("ingrese")
entr = input()
entr2 = int(entr)
for n in range(0, entr2):
	entra = input()
	entra2 = entra.split()
	for i in range(0, len(entra2)):
		entra2[i] = float(entra2[i])
	body(entra2[0],entra2[1])

print(*var, sep=' ')
