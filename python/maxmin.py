arreglo = []
print("Ingresar:")
entrada = input()
entrada2 = entrada.split()
for i in range(0,len(entrada2)):
      entrada2[i] = int(entrada2[i])
      arreglo.append(entrada2[i])
maximo = max(arreglo)
minimo = min(arreglo)
print(f"{maximo}  {minimo}")

