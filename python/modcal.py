var = []
vari = []
print("ingrese")
num = int(input())
nume = num
while True:
	
	nano = input()
	nano2 = nano.split()
	for n in range(0,len(nano2)):
		vari.append(nano2[n])
	if (vari[0] == "+"):
		nume += int(vari[1])
	elif (vari[0] == "-"):
		nume -= int(vari[1])
	elif (vari[0] == "*"):
		nume *= int(vari[1])
	elif (vari[0] == "%"):
                nume %= int(vari[1])
	print(nume)
	vari.clear()
	if (nano == ""):
		break

