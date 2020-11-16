var = []
print("introduzca")
entr = input()
for n in range(len(entr)-1,-1,-1):
	#print(n)
	entra = entr[n]
	var.append(entra)
#vari = re.sub(' ', '',var)	
print(*var,sep='')
