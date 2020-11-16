import numpy as np
var = []
entr8 = []
print("ingrese")
entra = int(input())
for n in range(0,entra):
	entr = input().lower()
	entr2 = entr.replace(",","")
	entr3 = entr2.replace(" ","")
	entr4 = entr3.replace("!","")
	entr5 = entr4.replace("-","")
	entr6 = entr5.replace(".","")
	entr7 = list(entr6)
	print(entr7)
	for n in reversed(range(0,len(entr7),1)):
		entr8.append(entr7[n])
	if (np.array_equal(entr7,entr8)):
		print("Y")
		var.append("Y")
	else:
		print("N")
		var.append("N")
	print(entr8)
	entr8.clear()
print(*var,sep=' ')
	
