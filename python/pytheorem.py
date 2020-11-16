var = []
print("ingrese")
entr = int(input())
for n in range(0,entr):
	a,b,c = input().split()
	a,b,c = int(a),int(b),int(c)
	if (((c*c/2) < a**2 + b**2) and (a**2 + b**2 < c**2)):
		var.append("O")
	elif (c**2 == a**2 + b**2):
		var.append("R")
	else:
		var.append("A")
print(*var,sep =' ')		
	


