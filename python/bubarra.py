var = []
print("ingrese")
entra = input()
entra2 = entra.split()
for n in range(0,len(entra2)):
	entra2[n] = int(entra2[n])
	var.append(entra2[n])
	num = 0
	result = 0
	conta = 0
while True:
	if(var[num - 1] < var[num]):
		print("pass")
	else:
		print("swap")
		var[num - 1], var[num] = var[num], var[num - 1]
		conta += 1
	num += 1
	if ( var[num] == -1 ):
		print("end")
		break
for i in range(0, len(var) - 1):
        result = (result + var[i])*113
        result %= 10000007

print("{} {}".format(conta,result))
