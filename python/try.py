
def operacion(num1,num2,num3):
	try:
		op = (num2 - num3)/num1
		print(op)
	except:
		print("división por cero")
	finally:
		print("fin del codigo")

print("inicio del codigo")
nume1 = int(input())
nume2 = int(input())
nume3 = int(input())

operacion(nume1,nume2,nume3)
