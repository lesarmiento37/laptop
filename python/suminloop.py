suma = 0
print("poner")
arreglo = input()
arreglo2 = arreglo.split()
print (arreglo2)

for i in range(0,len(arreglo2)):
    arreglo2[i] = int(arreglo2[i])
    suma += int(arreglo2[i])

print(suma)
  
