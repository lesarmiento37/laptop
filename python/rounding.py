import math
print("ingresar")
num = input()
num2 = int(num)
nume = []

for i in range(num2):
	variable = input()
	variable2 = variable.split()
	div = 0
	for n in range(0,len(variable2)):
		variable2[n] = int(variable2[n])
	div = round(variable2[0] / variable2[1])
	nume.append(div)
print(*nume, sep=' ')

