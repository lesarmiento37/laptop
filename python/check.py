print("ingrese")
entr = input()
entr2 = int(entr)

entra = input()
entra2 = entra.split()
result = 0
for i in range(0, len(entra2)):
	entra2[i] = int(entra2[i])
	result = (result + entra2[i])*113
	result %= 10000007
print(result)
	
		
