conta = []
print("ingrese datos")
num = input()
num2 = int(num)
for i in range(0,num2):
	vocal = input()
	count = 0
	for n in range(0,len(vocal)):
		if (vocal[n] == 'a') or (vocal[n] == 'e') or (vocal[n] == 'i') or (vocal[n] == 'o') or (vocal[n] == 'u') or (vocal[n] == 'y') :
			print(count)
			count += 1
	conta.append(count)
print(*conta , sep=(' '))
