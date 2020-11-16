print("ingrese")
var = []
entr = int(input())

for n in range(0,entr):
	n1,n2 = input().split()
	n1,n2 = int(n1),int(n2)
	n3 = n1 % 6 + 1
	n4 = n2 % 6 + 1 
	n5 = n3 + n4
	var.append(n5)
print(*var, sep=' ')
